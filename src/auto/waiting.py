import sched, time

from .abs_state import AbsState

day_length = 86400 # seconds
week_length = 7 # days


class Waiting(AbsState):

    def auto_wait(self, seconds=5):
        self._model.logger.info('Waiting for new round')
        time.sleep(seconds)
        
        if (self._model.napi.check_new_round()
            or self._model.test):
            self._model.logger.info('New round available')
            self.get_data()
        else:
            self.auto_wait()

    def check(self):
        if (self._model.napi.check_new_round()
            or self._model.test):
            self._model.logger.info('New round available')
            self._model.state = self._model.getting_data
            return True
        else:
            self._model.logger.info('No new round')
            return False
