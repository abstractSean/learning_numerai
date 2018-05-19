from .abs_state import AbsState


class Predicting(AbsState):

    def predict(self):
        m = self._model
        m.logger.info('Predicting')

        if m.test:
            self._model.state = self._model.checking
            return

        m.df_predict = predict_with_noise(
                                   m.df,
                                   m.model,
                                   m.features)

        self._model.state = self._model.checking

    def predict_with_noise(df, model, features, noise=0.0):
        df = df.loc[(df['data_type'] != 'train'),:]
        drop_columns = ['era','data_type', 'target']
        df = df.drop(drop_columns, axis=1).iloc[:,features]
        df['probability'] = model.predict_proba(df)[:,1]
        df['probability'] = df['probability'] + \
                            random.uniform(-noise,noise)
        return df

