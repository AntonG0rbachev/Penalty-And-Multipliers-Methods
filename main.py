# ПРОГОНКА ДВУХ СПОСОБОВ ПРОСТОГО И СЛОЖНОГО
from SimpleAlgorithm import simple_penalty_method
from Algorithm import penalty_method
import sys


def limit_function(x):
    return x[0] + x[1] - 2


r = [1, 2, 10, 100, 1000, 1e10]
eps = 0.001

print(f'advanced:\n{penalty_method(r, [limit_function], [], eps)}')
print('\nsimple:\n', simple_penalty_method(r, eps))
