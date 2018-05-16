from src import AutoModel
from src import Waiting


def test_AutoModel():
    auto = AutoModel()
    assert auto.state == Waiting()
