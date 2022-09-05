def square(number):
    if 1 <= number <= 64:
        result = 2 ** (number - 1)
        return result
    else :
        raise ValueError('square must be between 1 and 64')
def total():
    return (2 ** 64) - 1