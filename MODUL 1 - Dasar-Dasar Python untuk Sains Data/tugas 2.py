def gabungan(x, y):
    list1 = []
    list2 = []
    for i in range(1, len(x)):
        if i % 2 != 0:
            list1.append(x[i])
    for i in range(1, len(y)):
        if i % 2 != 0:
            list2.append(y[i])

    list_gabungan = list1 + list2
    list_gabungan.sort(reverse=True)

    return list_gabungan


x = gabungan([1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12])
print(x)
