# Program menentukan bilangan terbesar dari tiga bilangan

# Input tiga bilangan dari pengguna
a = float(input("100: "))
b = float(input("33: "))
c = float(input("66: "))

# Menentukan bilangan terbesar
if a >= b and a >= c:
    terbesar = a
if b >= a and b >= c:
    terbesar = b
else:
    terbesar = c

# Menampilkan hasil
print(f"Bilangan terbesar adalah: {terbesar}")
