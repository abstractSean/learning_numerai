from learning_numerai import AutoModel
from learning_numerai import Waiting


def test_AutoModel():
    auto = AutoModel()
    assert auto.state == Waiting()
