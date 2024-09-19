saldo_awal = 500000
pin_terdaftar = "1234"
max_attempts = 3


def atm_simulation():
    attempts = 0
    while attempts < max_attempts:
        pin = input("Masukkan PIN Anda: ")
        if pin == pin_terdaftar:
            print("PIN Benar.")
            break
        else:
            attempts += 1
            print(
                f"PIN Salah. Anda memiliki {max_attempts - attempts} percobaan lagi.")

        if attempts == max_attempts:
            print("Anda telah melebihi batas percobaan PIN. Transaksi diblokir.")
            return

    global saldo_awal
    try:
        jumlah_tarik = int(input("Masukkan jumlah penarikan: "))
    except ValueError:
        print("Input tidak valid, masukkan angka.")
        return

    if jumlah_tarik > saldo_awal:
        print("Saldo tidak mencukupi untuk melakukan penarikan.")
        return
    else:
        saldo_awal -= jumlah_tarik
        print(f"Penarikan berhasil. Saldo akhir Anda: Rp{saldo_awal}")


atm_simulation()
