# Latihan 4: Agregasi Nilai

nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

# Menghitung jumlah seluruh nilai
jumlah = sum(nilai)

# Menghitung banyaknya data
banyak_data = len(nilai)

# Menentukan nilai tertinggi dan terendah
nilai_tertinggi = max(nilai)
nilai_terendah = min(nilai)

# Menghitung rata-rata
rata_rata = jumlah / banyak_data

# Menampilkan hasil
print("Daftar nilai:", nilai)
print("Jumlah seluruh nilai:", jumlah)
print("Banyak data:", banyak_data)
print("Nilai tertinggi:", nilai_tertinggi)
print("Nilai terendah:", nilai_terendah)
print("Rata-rata nilai:", round(rata_rata, 2))