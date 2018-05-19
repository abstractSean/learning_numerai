import abc

STATE_TRANSITION_ERROR = 'Transition not implemented in state {}'

class AbsState(metaclass=abc.ABCMeta):
    def __init__(self, context):
        self._model = context

    def wait(self):
        self._transition_error()

    def get_data(self):
        self._transition_error()

    def train(self):
        self._transition_error()
    
    def predict(self):
        self._transition_error()

    def check(self):
        self._transition_error()

    def ensemble(self):
        self._transition_error()
        
    def prepare_submission(self):
        self._transition_error()

    def submit(self):
        self._transition_error()

    def stake(self):
        self._transition_error()

    def randomize(self):
        self._transition_error()

    def _transition_error(self):
        raise NotImplementedError(
            STATE_TRANSITION_ERROR.format(
                self._model.state.__class__.__name__))
