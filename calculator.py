from utils import validate_inputs

def add(a, b):
    validate_inputs(a, b)
    return a + b

def subtract(a, b):
    validate_inputs(a, b)
    return a - b

def multiply(a, b):
    validate_inputs(a, b)
    return a * b
