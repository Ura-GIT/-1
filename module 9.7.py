def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if result == 2 or result % 2 != 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
