def is_prime(number):
    if number <= 1:
        return False

    i = 2
    while i < number:
        if number % i == 0:
            return False
        i += 1

    return True
