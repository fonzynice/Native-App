import pytest


# @pytest.fixture
# def fix():
#     a = 4
#     return a


@pytest.fixture
def supply_url():
    return "https://reqres.in/api"
