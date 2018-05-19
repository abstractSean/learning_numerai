from .abs_state import AbsState

class Ensembling(AbsState):

    def prepare_submission(self):
        self._model.state = self._model.preparing

    def check(self):
        self._model.state = self._model.checking

    def train(self):
        self._model.state = self._model.training
        
        
