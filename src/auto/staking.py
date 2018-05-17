from .abs_state import AbsState

class Staking(AbsState):

    def stake(self):
        self._model.state = self._model.waiting
