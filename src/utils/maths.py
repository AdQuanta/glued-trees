from typing import Literal
import numpy as np
import math
import functools

Sign = Literal["+", "-"]


@functools.lru_cache(maxsize=128)
def factorial(n:int) -> int:
    return factorial(n-1)*n if n>1 else 1


def _sqrt_factorial_large_n(n):
    # Compute the logarithm of the factorial
    log_factorial = math.lgamma(n + 1)
    
    # Compute the logarithm of the square root of the factorial
    log_sqrt_factorial = log_factorial / 2
    
    # Exponentiate to get the square root of the factorial
    sqrt_factorial = np.exp(log_sqrt_factorial)
    
    return sqrt_factorial


def sqrt_factorial(n:int) -> float:
    if n<15:
        return np.sqrt(factorial(n))
    else:
        return _sqrt_factorial_large_n(n)


def find_closest_int_from_sqrt_including_one_over(x:float, eps:float=1e-5) -> tuple[int, bool, Sign]:
    if x >= 0:
        sign = "+"
    else:
        sign = "-"

    def _matching_int(val:float) -> int|None:
        val_int = int(round(val))
        relative_diff = abs(val - val_int)/val
        if relative_diff < eps:
            return val_int
        return None
    
    # search options:
    val = x*x
    val_int = _matching_int(val)
    if val_int is not None:
        return val_int, False, sign
    
    val = 1/val
    val_int = _matching_int(val)
    if val_int is not None:
        return val_int, True, sign
    
    raise ValueError()


def relu(x:float) -> float:
    return max(0, x)




