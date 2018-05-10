from abs_state import AbsState

class Preparing(AbsState):

    def submit(self):
        self._model.state = self._model.submitting
