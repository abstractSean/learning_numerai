from src.models import train_RFC
from src.models.manage_model_files import load_model, save_model

from .abs_state import AbsState

class Training(AbsState):

    def train(self):
        model = self._model
        model.logger.info('Training model')

        if not model.test:
            try:
                model, features = load_model('rfc_filtered')
            except FileNotFoundError:
                model, features = train_RFC.train_rfc_filtered(
                                                X_train, y_train)
                save_model((model, features),'rfc_filtered')
                                        

        self._model.state = self._model.checking
    

