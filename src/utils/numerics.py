from numpy import ceil, floor, pi

EPSILON = 0.000001


def force_between_0_and_2pi(a:float) -> float:
    while a<0:
        a += 2*pi
    while a>=2*pi:
        a -= 2*pi
    return a


def force_zero_for_small_numbers(x:float|int) -> float|int:
    if abs(x)<EPSILON:
        return 0
    else:
        return x
    

def force_integers_on_exactly_round(x:float|int) -> float|int:
    int_x = int(round(x))
    if int_x==x:
        return int_x
    return x


def force_integers_on_close_to_round(x:float|int) -> float|int:
    int_x = int(round(x))
    if abs(int_x-x)<EPSILON:
        return int_x
    return x


def furthest_absolute_integer(x:float|int) -> int:
    if x<0:
        return int(floor(x))
    else:
        return int(ceil(x))

def force_near_pure_complex(x:complex) -> complex|float|int:
    if abs(x.imag)<EPSILON:
        x = force_integers_on_close_to_round(x.real)
    if abs(x.real)<EPSILON:
        x = 1j*force_integers_on_close_to_round(x.imag)
    return x