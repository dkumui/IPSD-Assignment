def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def generate_primes(n):
    """Fungsi untuk menghasilkan bilangan prima sebanyak n buah."""
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

def generate_pattern(rows):
    """Fungsi untuk menghasilkan pola angka prima sesuai jumlah baris."""
    current_count = 0  # Menghitung total bilangan prima yang sudah ditampilkan
    for row in range(1, rows + 1):
        # Menghitung total bilangan prima yang dibutuhkan hingga baris ini
        total_primes_needed = current_count + row
        
        # Mengambil bilangan prima sebanyak yang diperlukan untuk baris ini
        primes = generate_primes(total_primes_needed)
        
        # Menampilkan bilangan prima yang sesuai baris ini
        print(" ".join(map(str, primes[current_count:total_primes_needed])))
        
        # Update total bilangan prima yang sudah ditampilkan
        current_count = total_primes_needed

# Contoh penggunaan:
rows = 5  # Misalnya kita ingin menampilkan 5 baris
generate_pattern(rows)