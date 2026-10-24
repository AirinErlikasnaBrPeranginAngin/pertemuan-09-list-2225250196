# Latihan 5: Filter Kelulusan

nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

batas_lulus = 60

# Menyiapkan list untuk menyimpan hasil
nilai_lulus = []
nilai_tidak_lulus = []

# Memeriksa setiap nilai
for n in nilai:
    if n >= batas_lulus:
        nilai_lulus.append(n)
    else:
        nilai_tidak_lulus.append(n)

# Menampilkan hasil
print("Daftar nilai:", nilai)
print("Nilai yang lulus:", nilai_lulus)
print("Nilai yang tidak lulus:", nilai_tidak_lulus)
print("Jumlah mahasiswa lulus:", len(nilai_lulus))
print("Jumlah mahasiswa tidak lulus:", len(nilai_tidak_lulus))