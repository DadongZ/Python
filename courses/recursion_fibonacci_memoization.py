
def fibonacci(n):
    """Return the nth fibonacci sequence."""
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(list(map(fibonacci, range(1,11))))

"""
The above func works but computationally cost is high.
And we need memoization to cache values.
"""


fibonacci_cache = {}

def fibonacci(n):
    """Return the nth fibonacci sequence using memoization"""
    """If we have cached the value, then return it"""
    if n in fibonacci_cache:
        return fibonacci_cache[n]

    """Compute the Nth term"""
    if n==1:
        return 1
    elif n==2:
        return 1
    elif n>2:
        value = fibonacci(n-1)+fibonacci(n-2)

    fibonacci_cache[n] = value
    return value

print(list(map(fibonacci, range(1,11))))


"""More elegant way using cache"""

from functools import lru_cache

@lru_cache(maxsize=1000)

def fibonacci(n):
    """Return the nth fibonacci sequence."""
    # check numbers
    if type(n) != int:
        raise TypeError("n must be a positive integer")
    if n < 1:
        raise TypeError("n must be a positive integer")
    if n==1:
        return 1
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(list(map(fibonacci, range(1,100))))

ratio = lambda n: fibonacci(n-1) / fibonacci(n)

print(list(map(ratio, range(2,100))))

