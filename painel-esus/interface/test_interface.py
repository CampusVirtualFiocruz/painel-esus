from .__main__ import extract_tabs
from .env import ENV


def test_tabs():
    tabs = extract_tabs(ENV)
    assert len(tabs) == 3
    print(tabs)
