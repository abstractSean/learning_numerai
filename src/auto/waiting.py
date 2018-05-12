from abs_state import AbsState
import sched, time

day_length = 86400 # seconds
week_length = 7 # days


class Waiting(AbsState):

    def get_data(self):
        self._model.state = self._model.getting_data
        self._model.get_data()

    def wait(self, seconds=5):
        print('Waiting for new round')
        time.sleep(seconds)
        
        if self._model.napi.check_new_round():
            self.get_data()
        else:
            self.wait()

