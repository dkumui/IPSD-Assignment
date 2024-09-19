def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def masuk_list(n):
    prima = []
    num = 2

    for i in range(1, n+1):
        while len(prima) < sum(range(1, i+1)):
            if is_prime(num):
                prima.append(num)
            num += 1
        print(*prima[-i:])


masuk_list(5)
