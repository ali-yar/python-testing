import pytest
from compute import divide, multiply

def test_divide():
	x = divide(1,2)
	assert x == pytest.approx(0.5)
	
def test_multiply():
	x = multiply(2,2)
	assert x == 4