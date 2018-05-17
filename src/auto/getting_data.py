from .abs_state import AbsState
from src.tools import utils

class GettingData(AbsState):

    def get_data(self):
        model = self._model
        model.logger.info('Getting data.')

        if not model.test:
            model.df = utils.load_data()

            model.X_train = model.df.loc[
                                    model.df['data_type']=='train',
                                    'feature1':'feature50']
            model.y_train = model.df.loc[
                                    model.df['data_type']=='train',
                                    'target']

        self._model.state = self._model.training


