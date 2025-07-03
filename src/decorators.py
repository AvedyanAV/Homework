from time import time


def log(filename=None):
    def decorator(func):
        def wrapper(*args):




@log(filename="mylog.txt")
def my_function(x, y):
    return x + y

my_function(1, 2)
