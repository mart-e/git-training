#!/usr/bin/env python2


def fibonacci(n):
    """inefficiant implementation of fibonacci using recursion"""
    if n==1 or n==2:
        return 1
    return fibonacci(n-1)+fibonacci(n-2)

if __name__ == '__main__':
    print fibonacci(30)
