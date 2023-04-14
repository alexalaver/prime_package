def prime_factors(number):
    while number > 1:
        for x in range(2, int(number ** 0.5) + 1):
            if number % x == 0:
                break
        else:
            x = number

        number //= x
        yield x

def is_prime(number):
    isp = False
    if number != 2:
        for x in range(2, int(number ** 0.5) + 1):
            if number % x == 0:
                isp = False
                break
            else:
                isp = True
    else:
        isp = True
    return isp

def prime_range(number):
    for x in range(2, number):
        if is_prime(x):
            yield x

if __name__ == "__main__":
    print(is_prime(5))