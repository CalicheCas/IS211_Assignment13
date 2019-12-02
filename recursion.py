# src/bin/python3


def fibonacci(n):

    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):

    if b != 0:
        return gcd(b, a % b)
    else:
        return a


def compareTos(s1, s2):

    len_s1 = len(s1)
    len_s2 = len(s2)
    if len_s1 < len_s2:
        length = len_s1
    else:
        length = len_s2

    if length == 0 & len_s1 > 0:
        return -1
    elif length == 0 & len_s2 > 0:
        return 1

    for i in range(length):

        v1 = ord(s1[i])
        v2 = ord(s2[i])

        if v1 == v2:
            return compareTos(s1[1:len_s1], s2[1:len_s2])
        else:
            return v1 - v2
    return 0


if __name__ == "__main__":

    fib = fibonacci(8)
    print(fib)

    g = gcd(8, 12)
    print(g)

    a = compareTos("carlo", "carlo")
    print(a)

    b = compareTos("Michael", "Jo")
    print(b)

    c = compareTos("Jose", "Nathan")
    print(c)

    d = compareTos("", "")
    print(d)





