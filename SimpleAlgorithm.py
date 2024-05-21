# ЧАСТНЫЙ СЛУЧАЙ МЕТОДА ШТРАФОВ
# ЭТО МЕТОД ЧТОБЫ ПОДСТАВИТЬ СВОИ ЗНАЧЕНИЯ Х1 и Х2 И ПОСЧИТАТЬ
import math
import sys


# вычисление х1 по формуле из примеров
def x1(rk):
    return -(1 / 3) + 5 * x2(rk)


# х2
def x2(rk):
    return (7 / 3 * rk - 1 / 3) / (9 + 6 * rk)


# функция со штрафом Р(х, r)
def F(_x1, _x2, rk):
    return _x1 ** 2 + 7 * _x2 ** 2 - _x1 * _x2 + _x1 + P(_x1, _x2, rk)


# сама функция штрафа
def P(_x1, _x2, rk):
    return (rk / 2) * (_x1 + _x2 - 2) ** 2


# тупа прогонка через цикл по всем r и выход если меньше epsilon
def simple_penalty_method(rk, epsilon):
    x_min = []
    for _rk in rk:
        _x1 = x1(_rk)
        _x2 = x2(_rk)
        _F = F(_x1, _x2, _rk)
        _P = P(_x1, _x2, _rk)
        if _P < epsilon:
            x_min = [_x1, _x2]
            break
    return {'x_min': x_min}


''' 
входные данные

r = [1, 2, 10, 100, 1000, sys.maxsize]
eps = 0.001

print(simple_penalty_method(r, eps))
'''
