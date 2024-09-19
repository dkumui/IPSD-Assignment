def min_coin_change(amount):
    coins = [1, 5, 10, 25]
    coins.sort(reverse=True)
    result = {}

    for coin in coins:
        if amount >= coin:
            num_coins = amount // coin
            amount -= num_coins * coin
            result[coin] = num_coins

    return result


print("Koin yang tersedia: 1, 5, 10, 25")
amount = int(input("Masukkan jumlah uang: "))
result = min_coin_change(amount)

print("Koin yang digunakan:")

for coin, count in result.items():
    print(f"Koin {coin}: {count} buah")

print("Total koin yang digunakan:", sum(result.values()))
