from .abs_state import AbsState


class Waiting(AbsState):

    def check(self):
        m = self._model
        m.logger.info('Checking for new round')
        if (m.napi.check_new_round()
            or m.test):
            m.logger.info('New round available')
            self._model.state = self._model.getting_data
            m.new_round = True
        else:
            m.logger.info('No new round')
            m.new_round = False

    def stop_waiting(self):
        self._model.state = self._model.getting_data

