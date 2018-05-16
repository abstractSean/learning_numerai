import pytest

from src import AutoModel
from src.auto import Waiting

@pytest.fixture(scope='function', name='auto')
def auto_fixture():
    auto = AutoModel()
    return auto

def test_AutoModel(auto):
    assert type(auto.state) == type(Waiting(None))
