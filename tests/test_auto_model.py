import pytest

from src import AutoModel
from src.auto import (Waiting,
                      GettingData,
                      Training,
                      Predicting,
                      Checking,
                      Ensembling,
                      Preparing,
                      Submitting,
                      Staking,
                      )


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
    assert type(auto.state) == type(Predicting(None))
    auto.predict()
    assert type(auto.state) == type(Checking(None))
    auto.check()
    assert type(auto.state) == type(Preparing(None))
    auto.prepare_submission()
    assert type(auto.state) == type(Submitting(None))
    auto.submit()
    assert type(auto.state) == type(Staking(None))
    auto.stake()
    assert type(auto.state) == type(Waiting(None))
    
