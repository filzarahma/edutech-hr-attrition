# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Perusahaan Edutech merupakan perusahaan teknologi pendidikan yang sedang berkembang dengan fokus utama pada Research & Development (R&D), Sales, dan Human Resources. Dengan total 1470 karyawan yang tersebar di berbagai departemen, perusahaan menghadapi tantangan dalam mempertahankan talenta terbaiknya. Dalam beberapa tahun terakhir, perusahaan mengalami tingkat attrition (pengunduran diri) karyawan yang cukup signifikan, terutama pada departemen Sales dan di posisi-posisi tertentu seperti Sales Representative dan Laboratory Technician.

Tingginya tingkat attrition menyebabkan perusahaan harus mengeluarkan biaya tambahan untuk rekrutmen, pelatihan, dan onboarding karyawan baru. Selain itu, pergantian karyawan juga dapat mempengaruhi produktivitas tim, kepuasan pelanggan, dan akhirnya berdampak pada pendapatan perusahaan.

### Permasalahan Bisnis

1. Bagaimana perusahaan dapat mengidentifikasi karyawan yang berisiko tinggi untuk resign sebelum mereka mengajukan pengunduran diri?
2. Faktor-faktor apa yang paling berpengaruh terhadap keputusan karyawan untuk resign?
3. Bagaimana perusahaan dapat mengembangkan strategi retensi karyawan yang lebih efektif berdasarkan data?
4. Bagaimana cara menurunkan tingkat attrition khususnya pada departemen Sales yang memiliki tingkat attrition tertinggi (20.7%)?
5. Bagaimana cara memantau dan mengukur keberhasilan program retensi karyawan secara berkelanjutan?

### Cakupan Proyek

1. **Analisis Data Karyawan**: Melakukan analisis komprehensif terhadap data karyawan untuk memahami faktor-faktor yang mempengaruhi attrition.
2. **Pembangunan Model Prediktif**: Mengembangkan model machine learning untuk memprediksi probabilitas seorang karyawan akan resign.
3. **Pengembangan Aplikasi Prediksi**: Membuat aplikasi berbasis Streamlit untuk memudahkan tim HR melakukan prediksi attrition.
4. **Visualisasi Data**: Membangun dashboard interaktif menggunakan Metabase untuk memvisualisasikan tren attrition dan metrik karyawan penting lainnya.
5. **Rekomendasi Strategi Retensi**: Menyusun rekomendasi konkret untuk mengurangi tingkat attrition berdasarkan insight dari data.

### Persiapan

Sumber data: Dataset karyawan yang terdiri dari 1470 record dengan 35 variabel yang mencakup informasi demografis, pendidikan, pengalaman kerja, informasi pekerjaan, kompensasi, dan indeks kepuasan karyawan.

Setup environment:

```
joblib==1.3.2
matplotlib==3.7.2
numpy==1.24.3
pandas==2.0.3
scikit-learn==1.3.0
scipy==1.11.1
seaborn==0.12.2
streamlit==1.25.0
sqlalchemy==2.0.20
imbalanced-learn==0.11.0
python-dotenv==1.0.0
psycopg2-binary==2.9.7
Pillow==9.5.0
```

## Business Dashboard

Untuk memvisualisasikan dan memonitor data karyawan serta tren attrition, dibangun dashboard interaktif menggunakan Metabase yang terhubung ke database Supabase. Dashboard terdiri dari dua halaman utama yang memberikan insight komprehensif:

### 1. Dashboard HR & Informasi Pekerjaan

Dashboard ini menampilkan:
- Overview attrition dengan total 179 karyawan resign dari 879 karyawan (16.92%)
- Distribusi attrition berdasarkan departemen (HR, R&D, Sales)
- Distribusi attrition berdasarkan job role dan job level
- Analisis berdasarkan stock option level dan income band
- Perbandingan antara karyawan yang lembur vs tidak lembur

Key insights dari dashboard ini:
- Sales Department memiliki tingkat attrition tertinggi (20.7%)
- Sales Representative adalah job role dengan attrition tertinggi (43.4%)
- Junior level memiliki tingkat attrition tertinggi dibanding level lainnya
- Karyawan dengan stock option level 0 memiliki risiko attrition lebih tinggi
- Karyawan yang sering lembur (overtime) memiliki tingkat attrition lebih tinggi (31%)

### 2. Dashboard Demografi

Dashboard ini menampilkan:
- Distribusi karyawan berdasarkan tingkat pendidikan dan attrition
- Komposisi gender (pria dan wanita) beserta tingkat retensi masing-masing
- Distribusi status pernikahan karyawan
- Analisis attrition berdasarkan total tahun bekerja
- Survey score yang mencakup kepuasan terhadap lingkungan, keterlibatan kerja, kepuasan kerja, kepuasan relasi, dan work-life balance
- Distribusi karyawan berdasarkan kelompok usia

Key insights dari dashboard ini:
- Gender pria memiliki tingkat attrition (17.4%) lebih tinggi dibanding wanita (16.2%)
- Karyawan dengan tingkat pendidikan sarjana memiliki jumlah terbanyak
- Karyawan dengan masa kerja 10 tahun memiliki tingkat attrition tertinggi
- Work-life balance menjadi faktor kepuasan tertinggi dengan 638 karyawan memberi nilai 3 (baik)

### Cara Menjalankan Dashboard Metabase

Dashboard visualisasi dibuat menggunakan Metabase yang terhubung ke database Supabase. Untuk melihat dashboard yang sudah dibuat, ikuti langkah-langkah berikut:

#### Prasyarat
1. Minimal 1GB RAM tersedia
2. File database Metabase (metabase.db.mv.db)
3. Docker 

#### Cara Menjalankan dengan Docker (Direkomendasikan)

Docker menyediakan cara termudah untuk menjalankan Metabase tanpa perlu mengkhawatirkan instalasi Java dan kompatibilitas sistem.

1. **Install Docker**
   - Download dan install Docker dari [website resmi Docker](https://www.docker.com/products/docker-desktop/)
   - Pastikan Docker sudah berjalan di sistem Anda

2. **Siapkan direktori untuk menyimpan data Metabase**
   ```bash
   # Di Windows
   mkdir C:\metabase-data
   
   # Salin file metabase.db.mv.db ke direktori tersebut
   copy "path\to\metabase.db.mv.db" C:\metabase-data\
   ```

3. **Jalankan container Metabase**
   ```bash
   # Jalankan Docker container dengan mounting volume
   docker run -d -p 3000:3000 --name metabase -v C:/metabase-data:/metabase-data -e "MB_DB_FILE=/metabase-data/metabase.db.mv.db" metabase/metabase
   ```

4. **Akses Metabase**
   - Buka browser dan akses `http://localhost:3000`
   - Login menggunakan kredensial:
     * Email: admin@metabase.local
     * Password: metabase123

5. **Melihat Dashboard**
   - Setelah login, klik menu "Dashboard" di navigasi atas

## Machine Learning Algorithms & Metodologi

Dalam proyek ini, model machine learning dibangun untuk memprediksi attrition karyawan menggunakan pendekatan ensemble learning berbasis pohon keputusan (decision tree). Model ini memiliki keunggulan dalam menangani data dengan fitur campuran (numerik dan kategorikal) serta kemampuan mengidentifikasi fitur-fitur paling berpengaruh.

### Algoritma yang Digunakan

1. **ExtraTreesClassifier**
   - Algoritma ensemble yang mirip dengan Random Forest
   - Membangun banyak pohon keputusan dengan randomisasi yang lebih tinggi
   - Keunggulan:
     * Mengurangi overfitting dengan randomisasi yang lebih ekstrim
     * Performa lebih baik untuk fitur yang saling berkorelasi
     * Mampu menangkap pola kompleks dalam data

2. **BalancedRandomForestClassifier**
   - Versi modifikasi dari Random Forest untuk menangani data tidak seimbang
   - Menerapkan teknik under-sampling internal pada kelas mayoritas
   - Keunggulan:
     * Mengatasi masalah ketidakseimbangan kelas secara bawaan
     * Memberikan perhatian lebih pada kelas minoritas (karyawan yang resign)
     * Meningkatkan metric performa yang relevan (recall, F1-score)

### Skema Penanganan Data Tidak Seimbang

Dalam proyek ini, digunakan dua pendekatan untuk menangani ketidakseimbangan kelas:

1. **Tanpa SMOTE**
   - Menggunakan dataset asli tanpa modifikasi
   - Mengandalkan algoritma dan threshold optimal untuk mengatasi ketidakseimbangan
   - Kelebihan: Mempertahankan distribusi data asli

2. **Dengan SMOTE (Synthetic Minority Over-sampling Technique)**
   - Membuat sampel sintetis dari kelas minoritas (karyawan yang resign)
   - Menyeimbangkan proporsi kelas sebelum melatih model
   - Kelebihan: Memberikan lebih banyak "contoh" karyawan resign untuk dipelajari model

### Evaluasi & Optimasi Model

Evaluasi model dilakukan dengan fokus pada:

1. **F1-score Kelas Minoritas**: Metrik yang menyeimbangkan precision dan recall untuk kelas karyawan yang resign
2. **Optimasi Threshold**: Mencari nilai threshold optimal untuk konversi probabilitas menjadi kelas (bukan default 0.5)
3. **Feature Importance Analysis**: Mengidentifikasi fitur-fitur yang paling berpengaruh dalam prediksi attrition

Dari empat kombinasi model yang diuji (dua algoritma × dua skema data), model terbaik adalah **ExtraTreesClassifier dengan skema tanpa SMOTE** yang mencapai **F1-score 0.59** untuk kelas minoritas dan **Akurasi 0.849**, menghasilkan performa optimal dalam mengidentifikasi karyawan berisiko tinggi untuk resign.

## Conclusion

Hasil analisis dan pemodelan machine learning menunjukkan bahwa attrition karyawan di perusahaan Edutech dipengaruhi oleh beberapa faktor utama, yaitu:

1. **Overtime**: Karyawan yang melakukan lembur memiliki tingkat attrition 3 kali lebih tinggi (31%) dibandingkan yang tidak lembur (11%).

2. **Job Role**: Sales Representative memiliki tingkat attrition tertinggi (43.4%), diikuti oleh Laboratory Technician (26.3%).

3. **Usia**: Karyawan muda (18-25 tahun) memiliki risiko resign tertinggi (37%), yang menurun seiring bertambahnya usia.

4. **Job Level**: Karyawan dengan level junior (level 1) memiliki kecenderungan resign lebih tinggi dibandingkan level manajerial.

5. **Work-Life Balance**: Karyawan dengan work-life balance buruk memiliki tingkat attrition 32%.

Model machine learning yang dibangun berhasil memprediksi karyawan yang berisiko resign dengan akurasi yang cukup baik. Aplikasi prediksi berbasis Streamlit memberikan interface yang user-friendly bagi tim HR untuk mengidentifikasi karyawan berisiko tinggi dan membuat strategi retensi yang tepat. Dashboard Metabase menyediakan visualisasi komprehensif untuk monitoring attrition secara berkesinambungan.

### Rekomendasi Action Items

- **Kebijakan Lembur**: Mengevaluasi dan merestrukturisasi kebijakan lembur, terutama di departemen Sales dan untuk posisi Laboratory Technician. Pertimbangkan untuk memberikan kompensasi lembur yang lebih adil atau menambah tenaga kerja untuk mengurangi kebutuhan lembur.

- **Program Pengembangan Karir**: Mengembangkan jalur karir yang jelas dan program mentoring, terutama untuk karyawan junior dan level entry, untuk meningkatkan retensi pada kelompok ini.

- **Revisi Sistem Kompensasi**: Melakukan benchmarking gaji dengan industri dan menyesuaikan paket kompensasi, terutama untuk Sales Representative yang memiliki tingkat attrition tertinggi.

- **Program Retensi Usia Muda**: Merancang program khusus untuk retensi karyawan usia 18-30 tahun, seperti pelatihan pengembangan diri, program rotasi posisi, atau flexible working arrangement.

- **Pengembangan Work-Life Balance**: Implementasi kebijakan yang mendukung keseimbangan kerja-hidup, seperti flexible hours, work from home, atau program wellness perusahaan.

- **Review Stock Option Program**: Merevisi program kepemilikan saham untuk menjangkau lebih banyak karyawan yang saat ini tidak memiliki opsi saham (level 0).

- **Monitoring Berkelanjutan**: Menggunakan dashboard untuk memantau efektivitas program retensi dan melakukan adjustments seperlunya.