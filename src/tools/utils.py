
def create_submission(df_predict_features, model, filename='predictions.csv'):
    df_predict_features['probability'] = model.predict_proba(
                                                df_predict_features)[:,1]
    df_predict_features['id'] = df_predict_features.index
    df_predict_features.to_csv(filename, 
                               columns=['id','probability'], 
                               index=None,
                              )


def get_validation_log_loss(df, model):
    features = [feat for feat in df.columns if 'feature' in feat]
    df_val_predict_feat = df.loc[df['data_type'] == 'validation', features]
    df_val_target = df.loc[df['data_type'] == 'validation','target']
    df_val_prediction = model.predict_proba(df_val_predict_feat)
    return log_loss(df_val_target, df_val_prediction)
    
