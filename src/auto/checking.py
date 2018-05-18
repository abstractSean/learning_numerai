from .abs_state import AbsState

class Checking(AbsState):

    def check(self):
        self._model.state = self._model.preparing

