#!usr/bin/env python  
# -*- coding:utf-8 -*-  
""" 
@file: speedUp.py
@version: v1.0 
@author: WeWe 
@time: 2018/10/19 9:23
@lib v: Python 3.6.4 /2.7.14
@description:This file is fro ...  
"""
from numba import jit
import time


def isPrime1(i):
    for test in range(2, i):
        if i % test == 0:
            return False
    return True


def main1():
    t1 = time.clock()

    n_loops = 50000
    n_primes = 0

    for i in range(0, n_loops):
        if isPrime1(i):
            n_primes += 1

    t2 = time.clock()
    print(str(n_primes))
    print("run time:%f s" % (t2 - t1))


@jit
def isPrime2(i):
    for test in range(2, i):
        if i % test == 0:
            return False
    return True


@jit
def tp():
    n_loops = 50000
    n_primes = 0

    for i in range(0, n_loops):
        if isPrime2(i):
            n_primes += 1
    return n_primes


def main2():
    t1 = time.clock()
    n_primes = tp()
    t2 = time.clock()

    print(str(n_primes))

    print("run time:%f s" % (t2 - t1))


if __name__ == "__main__":
    main2()
    pass
