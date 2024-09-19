def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:

        mid = (high + low) // 2

        if arr[mid] < x:
            low = mid + 1

        elif arr[mid] > x:
            high = mid - 1

        else:
            return mid

    return -1


def input_genap():
    while True:
        try:
            n = int(input("Masukkan bilangan genap yang ingin dicari: "))
            if n % 2 == 0:
                return n
            else:
                print("Input tidak valid, masukkan bilangan genap.")
        except ValueError:
            print("Input tidak valid, masukkan angka bulat.")


arr = [2, 3, 4, 10, 40, 50, 61, 75, 80, 90, 100]
print(arr)
x = input_genap()
result = binary_search(arr, x)

if result != -1:
    print(f"Angka {x} ditemukan pada index ke-", str(result))
else:
    print("Angka tidak ditemukan")
