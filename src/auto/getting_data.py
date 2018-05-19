from .abs_state import AbsState
from src.tools import utils


class GettingData(AbsState):

    def get_data(self):
        m = self._model
        m.logger.info('Getting data')

        if m.test:
            self._model.state = self._model.training
            return

        m.df = utils.load_data()

        m.X_train = m.df.loc[m.df['data_type']=='train',
                             'feature1':'feature50']
        m.y_train = m.df.loc[m.df['data_type']=='train',
                             'target']

        self._model.state = self._model.training

