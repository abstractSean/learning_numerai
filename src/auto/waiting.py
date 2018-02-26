from abs_state import AbsState
import sched, time

day_length = 86400 # seconds
week_length = 7 # days


class Waiting(AbsState):

    def get_data(self):
        self._model.state = self._model.getting_data

    def wait(self):
        pass        
