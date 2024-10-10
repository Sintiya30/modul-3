def jenis_segitiga(a, b, c):
    # Mengecek apakah bisa membentuk segitiga
    if a + b > c and a + c > b and b + c > a:
        # Segitiga sama sisi
        if a == b == c:
            return "Segitiga Sama Sisi"
        # Segitiga sama kaki
        elif a == b or a == c or b == c:
            return "Segitiga Sama Kaki"
        # Segitiga siku-siku
        elif a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return "Segitiga Siku-Siku"
        # Segitiga sembarang
        else:
            return "Segitiga Sembarang"
    else:
        return "Ini bukan merupakan segitiga"

# Program utama
print("========Selamat Datang di Segitiga Detektor==========")

# Input sisi-sisi segitiga
a = int(input("Isi sisi a: "))
b = int(input("Isi sisi b: "))
c = int(input("Isi sisi c: "))

# Menentukan jenis segitiga
hasil = jenis_segitiga(a, b, c)

# Menampilkan hasil
print("\nJenis segitiga:", hasil)
print("========Terimakasih========")

