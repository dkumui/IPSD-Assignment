saldo_awal = 1000000
pin_terdaftar = "1234"
batas_percobaan = 3


def atm_simulation():
    percobaan = 0
    while percobaan < batas_percobaan:
        pin = input("Masukkan PIN Anda: ")
        if pin == pin_terdaftar:
            print("PIN Benar.")
            break
        else:
            percobaan += 1
            print(
                f"PIN Salah. Anda memiliki {batas_percobaan - percobaan} percobaan lagi.")

        if percobaan == batas_percobaan:
            print("Anda telah melebihi batas percobaan PIN. Transaksi diblokir.")
            return

    global saldo_awal
    print(f"Saldo Anda: Rp{saldo_awal}")
    while True:
        try:
            jumlah_tarik = int(input("Masukkan jumlah penarikan: "))
            break
        except ValueError:
            print("Input tidak valid, masukkan angka.")

    if jumlah_tarik > saldo_awal:
        print("Saldo tidak mencukupi untuk melakukan penarikan.")
    else:
        saldo_awal -= jumlah_tarik
        print(f"Penarikan berhasil. Saldo akhir Anda: Rp{saldo_awal}")


atm_simulation()
