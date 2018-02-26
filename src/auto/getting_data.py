from abs_state import AbsState

class GettingData(AbsState):

    def train(self):
        self._model.state = self._model.training
