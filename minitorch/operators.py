"""
Collection of the core mathematical operators used throughout the code base.
"""


import math

# ## Task 0.1

# Implementation of a prelude of elementary functions.


def mul(x, y):
    ":math:`f(x, y) = x * y`"
    # TODO: Implement for Task 0.1.
    return float(x * y)


def id(x):
    ":math:`f(x) = x`"
    # TODO: Implement for Task 0.1.
    return float(x)


def add(x, y):
    ":math:`f(x, y) = x + y`"
    # TODO: Implement for Task 0.1.
    return float(x+y)


def neg(x):
    ":math:`f(x) = -x`"
    # TODO: Implement for Task 0.1.
    return float(-x)


def lt(x, y):
    ":math:`f(x) =` 1.0 if x is less than y else 0.0"
    # TODO: Implement for Task 0.1.
    return float(x < y)


def eq(x, y):
    ":math:`f(x) =` 1.0 if x is equal to y else 0.0"
    # TODO: Implement for Task 0.1.
    return float(x == y)


def max(x, y):
    ":math:`f(x) =` x if x is greater than y else y"
    # TODO: Implement for Task 0.1.
    return float(x) if x > y else float(y)


def is_close(x, y):
    ":math:`f(x) = |x - y| < 1e-2` "
    # TODO: Implement for Task 0.1.
    return float(abs(x-y) < 1e-2)


def sigmoid(x):
    r"""
    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}`

    (See `<https://en.wikipedia.org/wiki/Sigmoid_function>`_ .)

    Calculate as

    :math:`f(x) =  \frac{1.0}{(1.0 + e^{-x})}` if x >=0 else :math:`\frac{e^x}{(1.0 + e^{x})}`

    for stability.

    Args:
        x (float): input

    Returns:
        float : sigmoid value
    """
    # TODO: Implement for Task 0.1.
    return 1/ (1 + exp(-x))


def relu(x):
    """
    :math:`f(x) =` x if x is greater than 0, else 0

    (See `<https://en.wikipedia.org/wiki/Rectifier_(neural_networks)>`_ .)

    Args:
        x (float): input

    Returns:
        float : relu value
    """
    # TODO: Implement for Task 0.1.
    return float(max(x, 0))


EPS = 1e-6


def log(x):
    ":math:`f(x) = log(x)`"
    return math.log(x + EPS)


def exp(x):
    ":math:`f(x) = e^{x}`"
    return math.exp(x)


def log_back(x, d):
    r"If :math:`f = log` as above, compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    return d * (1/x) 


def inv(x):
    ":math:`f(x) = 1/x`"
    # TODO: Implement for Task 0.1.
    return 1/x


def inv_back(x, d):
    r"If :math:`f(x) = 1/x` compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    return -( 1/ (x*x)) * d
    


def relu_back(x, d):
    r"If :math:`f = relu` compute d :math:`d \times f'(x)`"
    # TODO: Implement for Task 0.1.
    if x > 0:
        return d
    else :
        return 0.0


# ## Task 0.3

# Small library of elementary higher-order functions for practice.


def map(fn):
    """
    Higher-order map.

    .. image:: figs/Ops/maplist.png


    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (one-arg function): Function from one value to one value.

    Returns:
        function : A function that takes a list, applies `fn` to each element, and returns a
        new list
    """
    def wrapper(*args, **kwargs):
        return [ fn(val) for val in args[0] ]
    return wrapper

def negList(ls):
    "Use :func:`map` and :func:`neg` to negate each element in `ls`"
    # TODO: Implement for Task 0.3.
    higher_order_neg = map(neg)
    return higher_order_neg(ls)


def zipWith(fn):
    """
    Higher-order zipwith (or map2).

    .. image:: figs/Ops/ziplist.png

    See `<https://en.wikipedia.org/wiki/Map_(higher-order_function)>`_

    Args:
        fn (two-arg function): combine two values

    Returns:
        function : takes two equally sized lists `ls1` and `ls2`, produce a new list by
        applying fn(x, y) on each pair of elements.

    """
    # TODO: Implement for Task 0.3.
    def wrapper(*args, **kwargs):
        list_1, list_2 = args
        return [ fn(x,y) for x,y in zip(list_1, list_2) ]
    return wrapper


def addLists(ls1, ls2):
    "Add the elements of `ls1` and `ls2` using :func:`zipWith` and :func:`add`"
    # TODO: Implement for Task 0.3.
    add_zipped = zipWith(add)
    return add_zipped( ls1, ls2 )


def reduce(fn, start):
    r"""
    Higher-order reduce.

    .. image:: figs/Ops/reducelist.png


    Args:
        fn (two-arg function): combine two values
        start (float): start value :math:`x_0`

    Returns:
        function : function that takes a list `ls` of elements
        :math:`x_1 \ldots x_n` and computes the reduction :math:`fn(x_3, fn(x_2,
        fn(x_1, x_0)))`
    """
    
    def wrapper(*args, **kwargs):
        value_list = args[0]

        output = value_list[0]    
        for val in value_list[1:]:
            output = fn( val, output )        
        return output

    return wrapper


def sum(ls):
    "Sum up a list using :func:`reduce` and :func:`add`."
    # TODO: Implement for Task 0.3.
    if len(ls) == 0:
        return 0 
    reduce_sum = reduce(add, ls[0] )
    return reduce_sum(ls)


def prod(ls):
    "Product of a list using :func:`reduce` and :func:`mul`."
    # TODO: Implement for Task 0.3.
    if len(ls) == 0:
        return 0
    reduce_prod = reduce(mul, ls[0])
    return reduce_prod(ls)