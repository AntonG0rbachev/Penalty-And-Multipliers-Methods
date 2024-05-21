# МЕТОД МНОЖИТЕЛЕЙ
import sys


def x2(rk, lk):
    return (7 / 3 * rk - 1 / 3 - lk) / (9 + 6 * rk)


def x1(rk, lk):
    return -(1 / 3) + 5 * x2(rk, lk)


def P(_x1, _x2, rk, lk):
    return (rk / 2) * (_x1 + _x2 - 2) ** 2 + lk * (_x1 + _x2 - 2)


def F(_x1, _x2, rk, lk):
    return _x1 ** 2 + 7 * _x2 ** 2 - _x1 * _x2 + _x1 + P(_x1, _x2, rk, lk)


def method(rk, lk, epsilon):
    x_min = []
    for _rk in rk:
        _x1 = x1(_rk, lk)
        _x2 = x2(_rk, lk)
        _F = F(_x1, _x2, _rk, lk)
        _P = P(_x1, _x2, _rk, lk)
        print(f'x1 = {_x1}, x2 = {_x2}, F = {_F}, P = {_P}, rk = {_rk}, lk = {lk}')
        if _P < epsilon:
            x_min = [_x1, _x2]
            break
        lk = lk + _rk * (_x1 + _x2 - 2)
        print(f'lk = {lk}')
    return {'x_min': x_min}


r = [1, 2, 10, 100, 1000, sys.maxsize]
l0 = 0

print(method(r, l0, 0.001))
