# Program Analisis Nilai Mahasiswa
# Pertemuan 09 - Algoritma dan Pemrograman

nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]
batas_lulus = 60

def hitung_rata_rata(data):
    return sum(data) / len(data)

def analisis_kelulusan(data, batas):
    lulus = []
    tidak_lulus = []

    for n in data:
        if n >= batas:
            lulus.append(n)
        else:
            tidak_lulus.append(n)

    return lulus, tidak_lulus

# Menghitung statistik
jumlah = sum(nilai)
banyak_data = len(nilai)
tertinggi = max(nilai)
terendah = min(nilai)
rata_rata = hitung_rata_rata(nilai)

# Menganalisis kelulusan
lulus, tidak_lulus = analisis_kelulusan(nilai, batas_lulus)

# Menampilkan hasil
print("=== ANALISIS NILAI MAHASISWA ===")
print("Daftar nilai:", nilai)
print("Jumlah seluruh nilai:", jumlah)
print("Banyak data:", banyak_data)
print("Nilai tertinggi:", tertinggi)
print("Nilai terendah:", terendah)
print("Rata-rata nilai:", round(rata_rata, 2))
print("Batas kelulusan:", batas_lulus)
print("Nilai yang lulus:", lulus)
print("Nilai yang tidak lulus:", tidak_lulus)
print("Jumlah yang lulus:", len(lulus))
print("Jumlah yang tidak lulus:", len(tidak_lulus))