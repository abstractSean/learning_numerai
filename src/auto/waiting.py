from .abs_state import AbsState


class Waiting(AbsState):

    def check(self):
        self._model.logger.info('Checking for new round')
        if (self._model.napi.check_new_round()
            or self._model.test):
            self._model.logger.info('New round available')
            self._model.state = self._model.getting_data
            return True
        else:
            self._model.logger.info('No new round')
            return False
