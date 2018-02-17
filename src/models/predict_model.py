#!/home/sean/virtualenvs/numerai/bin/python

import logging
import os
import random
import sys
sys.path.append('../..')

from dotenv import load_dotenv, find_dotenv
from numerapi import numerapi

from src.tools import numerai_api, utils
from src.models import train_RFC
from src.models.manage_model_files import *

def predict_with_noise(df, model, features, noise=0.0):
    df_predict = df.loc[(df['data_type'] == 'validation') |
                        (df['data_type'] == 'test') |
                        (df['data_type'] == 'live'), :]
    drop_columns = ['era','data_type', 'target']
    df_features = df_predict.drop(drop_columns, axis=1).iloc[:,features]
    df_predict.loc[:,'probability'] = model.predict_proba(df_features)[:,1]
    df_predict.loc[:,'probability'] = df_predict.loc[:,'probability'] + random.uniform(-noise,noise)
                                      
    return df_predict

def create_submission_file(df, filename):
    df.loc[:,'id'] = df.index
    df = df.loc[:, ['id','probability']]
    df.to_csv(filename, index=False)


def get_napi():
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)
    public_id = os.environ.get('NUMERAI_SUBMIT_ID')
    secret_key = os.environ.get('NUMERAI_SUBMIT_KEY')
    
    return numerapi.NumerAPI(public_id, secret_key, verbosity='info')

def main(noise=0.0):
    logger.info('Get data')
    df = utils.load_data()
    
    X_train = df.loc[df['data_type']=='train','feature1':'feature50']
    y_train = df.loc[df['data_type']=='train', 'target'] 

    logger.info('Train model')
    try:
        model, features = load_model('rfc_filtered') 
    except FileNotFoundError:
        model, features = train_RFC.train_rfc_filtered(X_train, y_train)
        save_model((model, features),'rfc_filtered')

    logger.info('Predict')
    df_predict = predict_with_noise(df, model, features, float(noise))

    round_number = numerai_api.get_current_round()
    filename = 'predictions_RFC_{}.csv'.format(round_number)
    logger.info('Create submission')
    create_submission_file(df_predict, filename)

    napi = get_napi()

    logger.info('Submit')
    napi.upload_predictions(filename)


if __name__ == '__main__':
        # setup logger
    log_fmt = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)
    logger = logging.getLogger()
    try:
        main(sys.argv[1])
    except IndexError:
        main()

