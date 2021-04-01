import pytest


def pytest_addoption(parser):
    parser.addoption("--bear_id", action="store", default="1")


@pytest.fixture()
def bear_id(pytestconfig):
    return pytestconfig.getoption("bear_id")
