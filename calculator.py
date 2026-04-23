import statistics

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def average(numbers):
    return statistics.mean(numbers)

def std_deviation(numbers):
    return statistics.stdev(numbers)

def get_summary(numbers):
    return {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "stdev": statistics.stdev(numbers),
        "variance": statistics.variance(numbers)
    }
