from .abs_state import AbsState
from src.tools import utils

class GettingData(AbsState):

    def get_data(self):
        model = self._model
        model.logger.info('Getting data.')

        if model.test:
            self._model.state = self._model.training
        else:
            model.df = utils.load_data()

            model.X_train = self._model.df.loc[
                                    self._model.df['data_type']=='train',
                                    'feature1':'feature50']
            model.y_train = self._model.df.loc[
                        self._model.df['data_type']=='train',
                        'target']



