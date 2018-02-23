import pytest

import numpy as np 

from compute import divide, multiply

def test_divide():
	x = divide(1,2)
	assert x == pytest.approx(0.5)
	
def test_multiply():
	x = multiply(2,2)
	assert x == 4
	
def test_divide_zero():
	assert np.isinf(divide(1,0))