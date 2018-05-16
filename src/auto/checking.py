from .abs_state import AbsState

class Checking(AbsState):

    def train(self):
        self._model.state = self._model.training

    def ensemble(self):
        self._model.state = self._model.ensembling
        
    def prepare_submission(self):
        self._model.state = self._model.preparing
