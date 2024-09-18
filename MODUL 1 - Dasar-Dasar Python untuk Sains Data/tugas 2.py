def gabung_indeks_ganjil_urut(list1, list2):
    # Ambil elemen dengan indeks ganjil dari kedua list
    list_ganjil_1 = [list1[i] for i in range(1, len(list1), 2)]
    list_ganjil_2 = [list2[i] for i in range(1, len(list2), 2)]
    
    # Gabungkan kedua list
    list_gabungan = list_ganjil_1 + list_ganjil_2
    
    # Urutkan secara menurun
    list_gabungan.sort(reverse=True)
    
    return list_gabungan

list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 9, 8, 7, 6, 5]
hasil = gabung_indeks_ganjil_urut(list1, list2)
print(hasil)