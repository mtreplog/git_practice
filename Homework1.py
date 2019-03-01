# https://www.cis.upenn.edu/~cis192/spring2017/html/files/hw/hw1.py


def fizzbuzz(n):

    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    if n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return ""


def snapcrackle(n):

    if n == int(n):
        return "Snap"
    else:
        return "Crackle"


def is_prime(n):
    counter = 0
    prime = []
    while len(prime) < n:

        counter += 1
        new = 0
        for i in range(1, counter):
            if counter % i == 0:
                new += 1
        if new < 2:
            prime.append(counter)

    else:
        return prime


print(is_prime(11))


def nth_prime(n):
    counter = 1
    new = 0
    for i in range(1, n):
        if n % i == 0:
            new += 1
            counter += 1
        elif counter <= i:
            counter += 1
        else:
            return new
    if new > 1:
        return False
    else:
        return True


def gcd_iter(n, m):
    new = 0
    gcd = 0
    if n >= m:
        for i in range(1, n):
            if n % i == 0:
                new = i
                if m % new == 0:
                    gcd = new
        return gcd
    if m > n:
        for x in range(1, m):
            if m % x == 0:
                new = x
                if n % x == 0:
                    gcd = new
        return gcd
