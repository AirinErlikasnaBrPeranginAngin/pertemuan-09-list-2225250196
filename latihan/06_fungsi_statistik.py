# Latihan 6: Fungsi Statistik

nilai = [78, 55, 90, 67, 60, 82, 45, 71, 88, 59]

def hitung_rata_rata(data):
    return sum(data) / len(data)

def tampilkan_statistik(data):
    print("Daftar nilai:", data)
    print("Jumlah nilai:", sum(data))
    print("Banyak data:", len(data))
    print("Nilai tertinggi:", max(data))
    print("Nilai terendah:", min(data))
    print("Rata-rata:", round(hitung_rata_rata(data), 2))

tampilkan_statistik(nilai)