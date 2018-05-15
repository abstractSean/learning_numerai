from abs_state import AbsState
from src.tools import utils

class GettingData(AbsState):

    def get_data(self):
        self._model.logger.info('Getting data.')
        self._model.df = utils.load_data()

        self._model.X_train = self._model.df.loc[
                                self._model.df['data_type']=='train',
                                'feature1':'feature50']
        self._model.y_train = self._model.df.loc[
                    self._model.df['data_type']=='train',
                    'target']


    def train(self):
        self._model.state = self._model.training


