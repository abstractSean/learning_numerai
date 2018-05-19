from .abs_state import AbsState


class Submitting(AbsState):

    def submit(self):
        m = self._model
        m.logger.info('Submitting')

        if m.test:
            self._model.state = self._model.staking
            return

        m.napi.upload_predictions(m.filename)

        self._model.state = self._model.staking

