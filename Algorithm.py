# МЕТОД ШТРАФОВ
# эта херь типо для всех случаев, но нужно поиграться с x0 в penalty_method() если плохо работает
import math
import sys
import numpy as np
import scipy as sp
from sympy import *
from scipy.optimize import minimize


# твоя функция
def function(x):
    return x[0] ** 2 + 5 * x[1] ** 2 - x[0] * x[1] + x[0]


# функция ограничений
def limit_function(x):
    return x[0] + x[1] - 2


# сама функция штрафа
def penalty_function(x, r, equalities, inequalities):
    result = 0
    for equality in equalities:
        result += equality(x) ** 2
    for inequality in inequalities:
        result += inequality(x) ** 2
    return (r / 2) * result


# функция со штрафом Р(х, r)
def F(x, r, equalities, inequalities):
    return function(x) + penalty_function(x, r, equalities, inequalities)


# алгоритм все тот же проходишь по циклу и все
# minimize взят из scipy и просто чтобы находить минимум
def penalty_method(r_array, equalities, inequalities, epsilon):
    _x = []
    x0 = [0, 0]
    for r in r_array:
        print(f'x0 = {x0}')
        _x = minimize(F, args=(r, equalities, inequalities), x0=np.array(x0)).x
        x0 = _x
        print(f'_x = {_x}, r = {r}')
        _F = F(_x, r, equalities, inequalities)
        _P = penalty_function(_x, r, equalities, inequalities)
        print(r * limit_function(_x), limit_function(_x))
        if _P < epsilon:
            return {'x_min': _x}


'''
входные данные

_r = [1, 2, 10, 100, 1000, sys.maxsize]
eps = 0.001

print(penalty_method(_r, [limit_function], [], eps))
'''
