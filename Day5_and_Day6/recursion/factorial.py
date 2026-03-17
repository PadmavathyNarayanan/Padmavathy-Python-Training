def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
    '''
    5 * factorial(5-1)
        4 * factorial(4-1)
            3 * factorial(3-1)
                2 * factorial(2-1)
                    1 * factorial(1-1)
                        0 * factorial(0-1)
    '''

print(factorial(3))