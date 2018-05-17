from .abs_state import AbsState

class Checking(AbsState):

    def check(self):
        self._model.state = self._model.preparing

    def ensemble(self):
        self._model.state = self._model.ensembling
        
    def prepare_submission(self):
        self._model.state = self._model.preparing
