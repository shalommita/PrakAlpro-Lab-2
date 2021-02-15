# SHALOMMITA PRANATANTRI
# INFORMATIKA - UNIVERSITAS KRISTEN DUTA WACANA
# LAB-2-VARIABLE, EXPRESSIONS, AND STATEMENTS

# membuat penamaan / pemberian variable dan perhitungan sederhana
print("----------PERHITUNGAN SEDERHANA----------")
print()

# INPUT
# Nama Ayah (Tipe data string)
nama_Ayah = str(input("Masukkan nama ayah Anda = "))
# Umur Ayah
umur_Ayah = int(input("Masukkan umur ayah Anda = "))
# Nama Ibu
nama_Ibu = str(input("Masukkan nama ibu Anda = "))
# Umur Ibu
umur_Ibu = int(input("Masukkan umur ibu Anda = "))

# PROSES
# Melakukan perhitungan : 
# selisih umur ayah dan ibu
selisih = umur_Ayah - umur_Ibu
print(selisih)
# umur ayah - 10
umur_Ayah_10 = umur_ayah - 10
print(umur_Ayah_10)
# rata-rata umur ayah dan ibu
rata_rata = (umur_Ayah + umur_Ibu) / 2
print(rata_rata)

print()
print(selisih + umur_Ayah_10 + rata_rata)

# OUTPUT