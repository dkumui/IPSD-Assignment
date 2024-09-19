import random

angka_rahasia = random.randint(1, 100)

print('=' * 60)
print('Angka sudah ditentukan, silahkan tebak dengan kesempatan 5x!')
print('=' * 60)

batas_percobaan = 5
for percobaan in range(batas_percobaan):
    jawaban = int(input(f'\n[Percobaan {percobaan + 1}] Masukkan angka: '))

    if jawaban == angka_rahasia:
        print('Buseettt bisa bener gitu tebaknya!')
        break
    else:
        if jawaban < angka_rahasia:
            print('Tebakanmu terlalu kecil')
        else:
            print('Tebakanmu terlalu besar')
else:
    print(
        f'\nYahhhh, kamu sudah salah menebak sebanyak {batas_percobaan}x!')