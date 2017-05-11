from functools import wraps  # for @double_result and @only_even_parameters


def get_next_multiple(n: int, count=1) -> int:
    for i in range(0, count + 1):
        yield count * n
        count += 1


# gen_multiple_of_two = get_next_multiple(2)
# next(gen_multiple_of_two) # 2
# next(gen_multiple_of_two) # 4
# next(gen_multiple_of_two) # 6
# next(gen_multiple_of_two) # 8

# gen_multiple_of_thirteen = get_next_multiple(13)
# next(gen_multiple_of_thirteen) # 13
# next(gen_multiple_of_thirteen) # 26
# next(gen_multiple_of_thirteen) # 39
# next(gen_multiple_of_thirteen) # 52


def is_prime(n: int) -> bool:
    if n == 2:  # first possible prime
        return True
    if n < 2 or n % 2 == 0:
        return False
    # range end at sqrt(n) + 1, count by 2, as multiples of 2 are even
    for i in range(3, int(n**0.5 + 1), 2):
        if n % i == 0:
            return False
    return True


# is_prime(11)  # True
# is_prime(122) # False

def get_next_prime(n=1) -> int:
    for i in range(n + 1, 1000):  # not including 1000, but it is not prime anyway
        if is_prime(i):
            yield i


# gen = get_next_prime()
# gen = get_next_prime(-1)
# gen = get_next_prime(7)
# next(gen)
# next(gen)
# next(gen)
# next(gen)
# next(gen)
# next(gen)


# def double_result(fn):
#     def inner(*args, **kwargs):
#         return fn(*args, **kwargs) * 2
#     return inner

def double_result(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        return fn(*args, **kwargs) * 2
    return inner


def add(a, b):
    return a + b

# add(5, 5)  # 10


@double_result
def add(a, b):
    return a + b

# add(5, 5)  # 20


def only_even_parameters(fn):
    @wraps(fn)
    def inner(*args, **kwargs):
        if any([arg for arg in args if arg % 2 != 0]):
            return "Please add even numbers!"
        return fn(*args)
    return inner


@only_even_parameters
def add(a, b):
    return a + b

# add(5, 5)  # "Please add even numbers!"
# add(4, 4)  # 8


@only_even_parameters
def multiply(a, b, c, d, e):
    return a * b * c * d * e


multiply(5, 5, 5, 5, 5)  # "Please multiply even numbers!"
multiply(2, 2, 2, 2, 2)  # 32


def sum_index(l_or_t):
    return sum(idx for idx, val in enumerate(l_or_t))

# sum_index([1,2,3,4]) # 6


# zip # built in method that takes 2 lists and combines them into tuples
# pairs based on index order
