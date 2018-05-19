from src.models import train_RFC
from src.tools.manage_model_files import load_model, save_model

from .abs_state import AbsState


class Training(AbsState):

    def train(self):
        m = self._model
        m.logger.info('Training model')

        if m.test:
            self._model.state = self._model.predicting
            return

        try:
            m.model, m.features = load_model('rfc_filtered')
        except FileNotFoundError:
            m.model, m.features = train_RFC.train_rfc_filtered(
                                            m.X_train, m.y_train)
            save_model((m.model, m.features),'rfc_filtered')

        self._model.state = self._model.predicting



