
import pickle
import re
import sys
sys.path.append('../..')

from glob import glob

from src.tools import numerai_api


def get_latest_file_id(model_name, round_number=False):
    if not round_number:
        round_number = numerai_api.get_current_round()
    current_round_names = glob('./{}*.pkl'.format(round_number))
    current_type_names = [name for name in current_round_names
                          if model_name in name]
    current_type_ids = [int(number[2:]) for name in current_type_names
                        for number in re.split('[_\.]', name)
                        if 'id' in number
                       ]
    current_type_ids.sort()
    try:
        return current_type_ids[-1]
    except IndexError:
        return 0


def get_id(model_name, id_):
    if id_ == 'last':
        return get_latest_file_id(model_name)
    elif id_ == 'new':
        return get_latest_file_id(model_name) + 1
    else:
        return int(id_)


def get_filename(model_name, id_, round_number=False):
    if not round_number:
        round_number = numerai_api.get_current_round()
    id_ = get_id(model_name, id_)
    return '{}_{}_id{}.pkl'.format(round_number, model_name, id_)


def save_model(model, model_name, id_='new'):
    filename = get_filename(model_name, id_)
    with open(filename, 'wb') as pickle_file:
        pickle.dump(model, pickle_file)
                                       

def load_model(model_name, id_='last', round_number=False):
    filename = get_filename(model_name, id_, round_number)
    with open(filename, 'rb') as pickle_file:
        return pickle.load(pickle_file)
