from src import AutoModel
from src.auto import Waiting


def test_AutoModel():
    auto = AutoModel()
    assert type(auto.state) == type(Waiting(None))
