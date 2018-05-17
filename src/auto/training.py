from .abs_state import AbsState

class Training(AbsState):

    def train(self):
        self._model.state = self._model.checking
    
    def check(self):
        self._model.state = self._model.checking

    def ensemble(self):
        self._model.state = self._model.ensembling

