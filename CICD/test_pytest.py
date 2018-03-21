# File must start with test_

# Its run just by calling pytest in the console
"""
pytest will run all files of the form test_*.py or *_test.py in the current directory and its subdirectories. 
More generally, it follows standard test discovery rules.

https://docs.pytest.org/en/latest/goodpractices.html#goodpractices

"""
import pytest
import source
from hypothesis import given
import hypothesis.strategies as st

@pytest.fixture
def data():
	return [1,2,3]

@pytest.fixture
def answer():
	return 2

@given(st.lists(st.floats()))
def means_the_same(xs):
    # This will generate lists of arbitrary length (usually between 0 and
    # 100 elements) whose elements are integers.

	if len(xs)>0:
	    assert source.my_mean(xs) == source.np_mean(xs)
	else:
		assert True

def test_mymean(data,answer):
	assert source.my_mean(data) == answer