LAB_SOURCE_FILE = __file__


def double_eights(n):
    """Returns whether or not n has two digits in row that
    are the number 8.

    >>> double_eights(1288)
    True
    >>> double_eights(880)
    True
    >>> double_eights(538835)
    True
    >>> double_eights(284682)
    False
    >>> double_eights(588138)
    True
    >>> double_eights(78)
    False
    >>> # ban iteration
    >>> from construct_check import check
    >>> check(LAB_SOURCE_FILE, 'double_eights', ['While', 'For'])
    True
    """
    if n < 10:
        return False
    elif n % 10 == 8 and ( n // 10) % 10 == 8:
        return True
    else: 
        return double_eights(n // 10)


def summation(n, term):
    """Return the sum of numbers 1 through n (including n) wíth term applied to each number.

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1)     # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x)      # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    >>> # ban iteration
    >>> from construct_check import check
    >>> check(LAB_SOURCE_FILE, 'summation', ['While', 'For'])
    True
    """
    assert n >= 1
    if n == 1:
        return term(1)
    else:
      return term(n) + summation(n - 1, term)


def ten_pairs(n):
    """Return the number of ten-pairs within positive integer n.

    >>> ten_pairs(7823952)
    3
    >>> ten_pairs(55055)
    6
    >>> ten_pairs(9641469)
    6
    >>> # ban iteration
    >>> from construct_check import check
    >>> check(LAB_SOURCE_FILE, 'ten_pairs', ['While', 'For'])
    True
    """
    last_value = n % 10
    if n == 0:
        return 0
    else:
        return count_digit(n // 10, 10 - last_value) + ten_pairs(n // 10)
    


def count_digit(n, digit):
    """Return how many times digit appears in n.

    >>> count_digit(55055, 5)
    4
    >>> from construct_check import check
    >>> # ban iteration
    >>> check(LAB_SOURCE_FILE, 'count_digits', ['While', 'For'])
    True
    """
    if n == 0:
        return 0
    elif n % 10 == digit:
        return 1 + count_digit(n // 10, digit)
    else:
        return count_digit(n // 10, digit)
    

