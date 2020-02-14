import pytest
import requests
import json
from CodeWarriors import *


@pytest.mark.skip
@pytest.mark.math
def test_add(fix):
    assert fix + 6 == 10  # fixture input is in the conftest.py file
    # assert add(2, 3) == 5
    # assert add(-1, -5) == -6
    # assert add(-3, 5) == 2


@pytest.mark.skip
@pytest.mark.warriors
def test_sum_str():
    assert sum_str(4, 4) == 8


@pytest.mark.skip
@pytest.mark.parametrize('num, output', [(1, 2), (2, 4), (3, 6), (4, 8)])
def test_multiply(num, output):
    assert 2 * num == output
    # assert multiply(3, 3) == 9


@pytest.mark.skip
@pytest.mark.parametrize('num, output', [(1, 1), (2, 0), (3, 1), (4, 0), (5, 1), (6, 0)])
def test_divisible_by(num, output):
    assert num % 2 == output


@pytest.mark.skip
@pytest.mark.parametrize('a, output', [([1, 2, 3], 3)])
def test_check(a, output):
    new_list = list((filter(lambda a: a == output, a)))
    assert int(new_list[0]) == output


@pytest.mark.skip
@pytest.mark.parametrize('n, output', [(5, [5, 4, 3, 2, 1]), ([4, [4, 3, 2, 1]])])
def test_reverse_seq(n, output):
    g = [x for x in range(1, n+1)]
    assert list(reversed(g)) == output


@pytest.mark.skip
@pytest.mark.parametrize('para, output', [('my name', 'myname'), ('Good Morning', 'GoodMorning')])
def test_no_space(para, output):
    assert para.replace(' ', '') == output


@pytest.mark.parametrize('user_id, first_name', [(1, 'George'), (2, 'Jane')])
def test_list_valid_user(supply_url, user_id, first_name):
    pass

# def test_list_invaliduser():
# pass