import pandas as pd

data = pd.read_csv(
    'D:/IPSD/IPSD - Assignment/MODUL 1 - Dasar-Dasar Python untuk Sains Data/nilai.csv')

data_dict = data.to_dict(orient='list')
print(data_dict)

nilai = data_dict.get('nilai', [])
nama = data_dict.get('nama', [])

if nilai:
    rata_rata = sum(nilai) / len(nilai)
    rata_rata_bulat = round(rata_rata, 2)
    print(f"Rata-rata nilai: {rata_rata_bulat}")

    nilai_tertinggi = max(nilai)
    nilai_terendah = min(nilai)

    index_nilai_tertinggi = nilai.index(nilai_tertinggi)
    index_nilai_terendah = nilai.index(nilai_terendah)

    print(
        f"Mahasiswa dengan nilai tertinggi: {nama[index_nilai_tertinggi]} dengan nilai {nilai_tertinggi}")
    print(
        f"Mahasiswa dengan nilai terendah: {nama[index_nilai_terendah]} dengan nilai {nilai_terendah}")
else:
    print("Tidak ada data nilai yang dimasukkan.")
