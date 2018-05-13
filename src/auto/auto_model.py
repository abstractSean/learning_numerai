import os

from waiting import Waiting
from getting_data import GettingData
from training import Training
from checking import Checking
from ensembling import Ensembling
from preparing import Preparing
from submitting import Submitting
from staking import Staking

from numerapi.numerapi import NumerAPI
from dotenv import find_dotenv, load_dotenv

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
        self.napi = self.get_napi() 
        
        log_fmt = '%(asctime)s - %(levelname)s - %(message)s'
        logging.basicConfig(level=logging.INFO, format=log_fmt)
        self.logger = logging.getLogger()
    
    def start(self,test=False):
        if test:
            self.state.get_data()
        else:
            self.state.wait(0)
        
        
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
    
    def get_napi(user='NUMERAI'):
        dotenv_path = find_dotenv()
        load_dotenv(dotenv_path)
        public_id = os.environ.get('{}_SUBMIT_ID'.format(user))
        secret_key = os.environ.get('{}_SUBMIT_KEY'.format(user))
        return NumerAPI(public_id, secret_key, verbosity='info')

