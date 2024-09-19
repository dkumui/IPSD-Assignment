def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def factorial_sequence(n):
    if n < 1:
        return []

    sequence = factorial_sequence(n - 1)
    sequence.append(factorial(n))
    return sequence


def input_genap():
    while True:
        try:
            n = int(input("Masukkan bilangan genap: "))
            if n % 2 == 0:
                return n
            else:
                print("Input tidak valid, masukkan bilangan genap.")
        except ValueError:
            print("Input tidak valid, masukkan angka bulat.")


n = input_genap()
print(factorial_sequence(n))
