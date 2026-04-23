from calculator import add, subtract, multiply, get_summary
import scipy.stats as sp

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(10, 4) == 6

def test_multiply():
    assert multiply(3, 4) == 12

def test_summary():
    result = get_summary([1, 2, 3, 4, 5])
    assert result["mean"] == 3.0

def test_skewness():
    data = [1, 2, 3, 4, 5]
    skew = sp.skew(data)
    assert isinstance(skew, float)
    
