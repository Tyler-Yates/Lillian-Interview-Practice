def fibonacci(num):
    """
    Returns the Fibonacci number for the given input.

    The definition for Fibonacci numbers is as follows:
    fibonacci(0) = 1
    fibonacci(1) = 1
    fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

    Args:
        num (int): the given input

    Returns:
        int: the Fibonacci number
    """
    if num == 0:
        return 1
    elif num == 1:
        return 1
    elif num < 0:
        return 0
    else:
        fib_n_minus_1 = 1
        fib_n_minus_2 = 1
        fib_n = 2
        for x in range (1, num):
            fib_n = fib_n_minus_1 + fib_n_minus_2
            fib_n_minus_2 = fib_n_minus_1
            fib_n_minus_1 = fib_n
    return fib_n
