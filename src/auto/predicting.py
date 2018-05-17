from .abs_state import AbsState


class Predicting(AbsState):

    def predict(self):
        self._model.state = self._model.checking
        
