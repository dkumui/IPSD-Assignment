def kalimat_terbalik(n):
    kata1 = n.split()
    list_kalimat_terbalik = [kata2[::-1] for kata2 in kata1]
    
    return list_kalimat_terbalik

kalimat = input("Masukkan sebuah kalimat: ")
output = kalimat_terbalik(kalimat)
print(output)