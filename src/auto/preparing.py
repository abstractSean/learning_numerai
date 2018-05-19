from .abs_state import AbsState


class Preparing(AbsState):

    def prepare_submission(self):
        m = self._model
        m.logger.info('Create submission')

        if m.test:
            self._model.state = self._model.submitting
            return

        round_number = m.napi.get_current_round()
        m.filename = 'predictions_RFC_{}.csv'.format(round_number)
        self.create_submission_file(m.df_predict, m.filename)

        self._model.state = self._model.submitting

    def create_submission_file(self, df, filename):
        df['id'] = df.index
        df = df.loc[:, ['id','probability']]
        df.to_csv(filename, index=False)
