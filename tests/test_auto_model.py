import pytest

from src import AutoModel
from src.auto import Waiting
from src.auto import GettingData
from src.auto import Training
from src.auto import Checking
from src.auto import Ensembling
from src.auto import Preparing
from src.auto import Submitting
from src.auto import Staking


@pytest.fixture(scope='function', name='auto')
def auto_fixture():
    auto = AutoModel(test=True)
    return auto

def test_AutoModel(auto):
    assert type(auto.state) == type(Waiting(None))
    
    auto.check()
    assert type(auto.state) == type(GettingData(None))
    auto.get_data()
    assert type(auto.state) == type(Training(None))
    auto.train()
    assert type(auto.state) == type(Checking(None))
    auto.check()
    assert type(auto.state) == type(Ensembling(None))
    auto.prepare_submission()
    assert type(auto.state) == type(Preparing(None))
    auto.submit()
    assert type(auto.state) == type(Submitting(None))
    auto.stake()
    assert type(auto.state) == type(Staking(None))
    
