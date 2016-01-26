#!/usr/bin/env python2


def _recursive_fin(n):
    """inefficiant implementation of fibonacci using recursion"""
    if n==1 or n==2:
        return 1
    return _recursive_fin(n-1)+_recursive_fin(n-2)  # call recursively


def _looping_fin(n):
    """more efficiant fibonacci implementation"""
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


def fibonacci(n):
    """return nth number of the fibonacci sequence"""
    return _looping_fin(n)

if __name__ == '__main__':
    print fibonacci(30)
