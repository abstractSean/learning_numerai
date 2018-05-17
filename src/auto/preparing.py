from .abs_state import AbsState

class Preparing(AbsState):

    def prepare_submission(self):
        self._model.state = self._model.submitting
