
import os
import pandas as pd
import sys
sys.path.append('/home/sean/Projects/numerai/numerai')

from numerapi import numerapi
from src.data import get_raw_data
from src.tools import numerai_api

from sklearn.metrics import log_loss

def check_consistency(df, model):
    eras_passed = 0
    unique_eras = df.loc[df['data_type']=='validation',:].era.unique()

    for era in unique_eras:
        loss = get_validation_log_loss(df.loc[df['era']==era,:], model)

        if loss < 0.693:
            eras_passed += 1

    return eras_passed / len(unique_eras)


def create_submission(df, model, filename='predictions.csv'):
    features = [feat for feat in df.columns if 'feature' in feat]
    df['probability'] = model.predict_proba(df.loc[:,features])[:,1]
    df['id'] = df.index
    df.to_csv(filename, columns=['id','probability'], index=None)


def get_validation_log_loss(df, model):
    features = [feat for feat in df.columns if 'feature' in feat]
    df_val_predict_feat = df.loc[df['data_type'] == 'validation', features]
    df_val_target = df.loc[df['data_type'] == 'validation','target']
    df_val_prediction = model.predict_proba(df_val_predict_feat)
    return log_loss(df_val_target, df_val_prediction)


def load_data(round_number=False):
    if not round_number:
        round_number = numerapi.NumerAPI().get_current_round()
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    raw_data_path = os.path.join(project_dir, 'data','raw')
    raw_data_file = os.path.join(raw_data_path, '{}_numerai_raw.pkl'.format(round_number))
    try:
        return pd.read_pickle(raw_data_file)
    except FileNotFoundError:
        get_raw_data.main(project_dir)
        return pd.read_pickle(raw_data_file)
