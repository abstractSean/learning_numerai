import sched, time

from .abs_state import AbsState

day_length = 86400 # seconds
week_length = 7 # days


class Waiting(AbsState):

    def get_data(self):
        self._model.state = self._model.getting_data
        self._model.get_data()

    def auto_wait(self, seconds=5):
        self._model.logger.info('Waiting for new round')
        time.sleep(seconds)
        
        if (self._model.napi.check_new_round()
            or self._model.test):
            self._model.logger.info('New round available')
            self.get_data()
        else:
            self.auto_wait()

