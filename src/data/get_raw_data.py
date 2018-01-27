#!/home/sean/virtualenvs/numerai/bin/python

import logging
import os
import pandas as pd
import sys
sys.path.append('/home/sean/Projects/numerai/numerai/')

from dotenv import find_dotenv, load_dotenv
from io import BytesIO
from requests import Session
from src.tools.numerai_api import get_dataset_url, get_dataset_round
from zipfile import ZipFile


def download_dataset_as_df(dataset_url):
    with Session() as r:
        dataset_download = r.get(dataset_url, stream=True).content
    
        with ZipFile(BytesIO(dataset_download)) as dataset_zip:
            with dataset_zip.open('numerai_training_data.csv') as train_data:
                df_train = pd.read_csv(train_data, index_col='id')
            with dataset_zip.open('numerai_tournament_data.csv') as live_data:
                df_live = pd.read_csv(live_data, index_col='id')
            
    return pd.concat([df_train, df_live])


def main(project_dir):
    
    # get logger
    logger = logging.getLogger(__name__)
    logger.info('Getting raw data')

    dataset_url = get_dataset_url()
    round_number = get_dataset_round(dataset_url)
    dataset_filename = '{}_numerai_raw.csv'.format(round_number)
    raw_data_path = os.path.join(project_dir, 'data', 'raw')    
    raw_data_file = os.path.join(raw_data_path, dataset_filename)
    
    if dataset_filename in [csv for csv in os.listdir(raw_data_path)]:
        logger.info("Dataset for round {} already downloaded as {}".format(
                        round_number, dataset_filename))
    else:
        logger.info("Downloading data for round {}".format(round_number))
        df = download_dataset_as_df(dataset_url)    
        df.to_csv(raw_data_file)
        logger.info("Dataset for round {} downloaded as {}".format(
                        round_number, dataset_filename))
        


if __name__ == '__main__':
    # get project root directory
    project_dir = os.path.join(os.path.dirname(__file__), os.pardir, os.pardir)
    
    # setup logger
    log_fmt = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logging.INFO, format=log_fmt)

    # find .env automatically by walking up directories until it's found
    dotenv_path = find_dotenv()
    # load up the entries as environment variables
    load_dotenv(dotenv_path)

    # call the main
    main(project_dir)
    
    
    
    
