# Pertemuan 09 - List dan Pengolahan Data Numerik

**Nama:** Airin Erlikasna Br Perangin Angin  
**NIM:** 2225250196
**Kelas:** 3-B

## Tujuan
Mempelajari penggunaan list dalam Python untuk menyimpan, mengakses, memodifikasi, dan mengolah data numerik.

## Struktur Folder
- `latihan/`: Berisi enam program latihan tentang list dan pengolahan data.
- `praktik/`: Berisi program analisis nilai mahasiswa.
- `.gitignore`: Mengatur file yang tidak perlu disertakan dalam Git.

## Cara Menjalankan
Jalankan program melalui terminal VS Code dari folder utama proyek.

Contoh:
`python praktik/analisis_nilai_mahasiswa.py`

## Hasil Praktik
Program mengolah 10 nilai mahasiswa, menghitung jumlah, rata-rata, nilai tertinggi, nilai terendah, serta mengelompokkan nilai berdasarkan batas kelulusan 60.

## Refleksi
Melalui tugas ini, saya mempelajari penggunaan list, indeks, slicing, perulangan, percabangan, dan fungsi untuk mengolah data numerik menggunakan Python.

## Jawaban Kuis Formatif - Kuis 3

### 1. Mengapa list lebih tepat daripada banyak variabel terpisah untuk menyimpan 30 nilai?
List dapat menyimpan banyak nilai dalam satu variabel sehingga data lebih mudah dikelola, diakses menggunakan indeks, dan diolah menggunakan perulangan.

### 2. Berapa indeks elemen pertama pada list Python?
Indeks elemen pertama adalah 0 karena indeks Python dimulai dari angka 0.

### 3. Apa arti indeks -1?
Indeks -1 digunakan untuk mengakses elemen terakhir dalam list Python.

### 4. Apa hasil [10, 20, 30, 40][1:3]?
Hasilnya adalah [20, 30], karena slicing mengambil elemen dari indeks 1 sampai sebelum indeks 3.

### 5. Apa perbedaan append dan insert?
append() menambahkan elemen ke akhir list, sedangkan insert() menambahkan elemen pada posisi indeks tertentu.

### 6. Apa risiko mengakses indeks yang tidak ada?
Program dapat menghasilkan IndexError karena indeks yang diminta berada di luar jangkauan list.

### 7. Fungsi apa yang digunakan untuk menghitung banyak elemen list?
Fungsi len() digunakan untuk menghitung banyaknya elemen dalam list.

### 8. Bagaimana menghitung rata-rata list numerik dengan sum dan len?
Rata-rata dihitung dengan rumus sum(data) / len(data), yaitu jumlah seluruh nilai dibagi banyaknya elemen.

### 9. Mengapa list kosong perlu diperiksa sebelum pembagian?
List kosong memiliki panjang 0. Jika jumlah nilainya dibagi dengan 0, program akan menghasilkan ZeroDivisionError. Karena itu, list perlu diperiksa sebelum menghitung rata-rata.

### 10. Apa perintah yang digunakan untuk mengirim commit lokal ke GitHub?
Perintah git push digunakan untuk mengirim commit lokal ke repositori remote. Untuk push pertama, dapat digunakan git push -u origin main jika remote bernama origin dan branch yang digunakan adalah main.