from abs_state import AbsState

class Training(AbsState):

    def train(self):
        self._model.state = self._model.training
    
    def check(self):
        self._model.state = self._model.checking
