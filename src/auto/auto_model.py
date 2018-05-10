from waiting import Waiting
from getting_data import GettingData
from training import Training
from checking import Checking
from ensembling import Ensembling
from preparing import Preparing
from submitting import Submitting
from staking import Staking


class AutoModel:
    def __init__(self):
        self.waiting = Waiting(self)
        self.getting_data = GettingData(self)
        self.training = Training(self)
        self.checking = Checking(self)
        self.ensembling = Ensembling(self)
        self.preparing = Preparing(self)
        self.submitting = Submitting(self)
        self.staking = Staking(self)

        self.state = self.waiting

    def wait(self):
        self.state.wait()

    def get_data(self):
        self.state.get_data()

    def train(self):
        self.state.train()

    def check(self):
        self.state.check()

    def ensemble(self):
        self.state.ensemble()

    def prepare_submission(self):
        self.state.prepare_submission()

    def submit(self):
        self.state.submit()
    
    def stake(self):
        self.state.stake()

    def randomize(self):
        self.state.randomize()

