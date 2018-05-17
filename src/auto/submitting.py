from .abs_state import AbsState

class Submitting(AbsState):

    def check(self):
        self._model.state = self._model.checking

    def submit(self):
        self._model.state = self._model.staking

    def wait(self):
        self._model.state = self._model.waiting
