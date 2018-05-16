from src.auto.auto_model import AutoModel
from src.auto.waiting import Waiting


def test_AutoModel():
    auto = AutoModel()
    assert auto.state == Waiting()
