
import numpy as np
import sys
sys.path.append('../..')

from sklearn.ensemble import RandomForestClassifier

from src.tools import numerai_api, utils
from src.models.manage_model_files import *

def train_rfc(X_train, y_train):
    rfc = RandomForestClassifier(n_jobs=-1,
                                n_estimators=170,
                                max_leaf_nodes=203,
                                max_features=10,
                                random_state=21,
                                )
    rfc.fit(X_train, y_train)
    return rfc


def get_filtered_features(model, threshold):
    return np.where(model.feature_importances_ > threshold)[0]


def train_rfc_filtered(X_train, y_train, id_='last'):
    try:
        rfc_baseline = load_model('rfc_baseline', id_)
    except FileNotFoundError:
        rfc_baseline = train_rfc(X_train, y_train)
        save_model(rfc_baseline, 'rfc_baseline', id_)
        
    features = get_filtered_features(rfc_baseline, 0.020)
    X_train_filtered = X_train.iloc[:, features]
    return train_rfc(X_train_filtered, y_train), features

