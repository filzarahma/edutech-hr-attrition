# 🚀 Proyek Akhir: HR Attrition Prediction untuk Perusahaan Edutech

---

## 📑 Daftar Isi

1. [Business Understanding](#business-understanding)
       • Permasalahan Bisnis
       • Cakupan Proyek
2. [Struktur Repository](#struktur-repository)
3. [Persiapan Data](#persiapan-data)
4. [Business Dashboard](#business-dashboard)
       • Dashboard HR & Informasi Pekerjaan
       • Dashboard Demografi
       • Cara Menjalankan Dashboard Metabase
5. [Machine Learning & Metodologi](#machine-learning--metodologi)
6. [Kesimpulan & Rekomendasi](#kesimpulan--rekomendasi)

---

## 🏢 1. Business Understanding

### Permasalahan Bisnis

Perusahaan Edutech mengalami **tingkat attrition (pengunduran diri karyawan) sebesar 16,92%**, jauh di atas rata-rata industri (5–10%). Tingginya tingkat attrition ini paling banyak terjadi pada departemen Sales, khususnya posisi Sales Representative dan Laboratory Technician.
**Tujuan utama:** Memahami faktor penyebab attrition dan mengembangkan strategi prediktif dan preventif berbasis data.

### Cakupan Proyek

1. **Analisis Data Karyawan:**
   Memahami faktor-faktor utama yang memengaruhi attrition.
2. **Pembangunan Model Prediktif:**
   Menggunakan machine learning untuk memprediksi risiko resign.
3. **Pengembangan Aplikasi Prediksi:**
   Aplikasi Streamlit untuk tim HR melakukan prediksi attrition.
4. **Visualisasi Data:**
   Dashboard interaktif di Metabase.
5. **Rekomendasi Strategi Retensi:**
   Saran actionable untuk menurunkan attrition.

---

## 📁 2. Struktur Repository

```
hrd-attrition-prediction/
│
├── notebook.ipynb             # Analisis & pembuatan model
├── prediction.py              # Aplikasi Streamlit untuk prediksi attrition
├── README.md                  # Dokumentasi proyek
├── requirements.txt           # Daftar package Python
├── metabase.db.mv.db          # Database untuk Metabase dashboard
└── model/
    ├── model.joblib           # Model ML terlatih (ExtraTrees)
    ├── label_encoders.joblib  # Encoder data kategorikal
    └── scaler.joblib          # Scaler untuk normalisasi numerik
```

---

## ⚙️ 3. Persiapan Data

* **Sumber data:**
  Dataset [employee\_data.csv](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv) dari Dicoding, berisi 1.470 karyawan dan 35 variabel terkait demografi, riwayat kerja, dan kepuasan kerja.
  Target utama: Kolom `Attrition` (0 = tidak resign, 1 = resign).

* **Penjelasan fitur:**
  Lihat [dokumentasi fitur](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/README.md).

* **Setup environment:**
  Gunakan Python 3.8+ dan dependencies di `requirements.txt`.

  ```bash
  # Membuat environment baru dan mengaktifkannya
  conda create --name main-ds python=3.9
  conda activate main-ds

  # Instalasi dependencies
  pip install -r requirements.txt
  ```

* **Menjalankan aplikasi prediksi:**

  ```bash
  streamlit run prediction.py
  ```

  Akses aplikasi di browser:
  `http://localhost:8501`
  [Demo Online](https://edutech-attrition-prediction.streamlit.app)

---

## 📊 4. Business Dashboard

### a. Dashboard HR & Informasi Pekerjaan

* **Statistik Attrition:**

  * 179 resign dari 1.058 karyawan (16.92%)
* **Distribusi:**

  * Berdasarkan departemen, job role, job level, stock option, income band, dan overtime.
* **Key Insight:**

  * Attrition tertinggi: Sales department & Sales Rep
  * Entry level & stock option = 0 → risiko resign tinggi
  * Overtime = risiko resign lebih tinggi (31%)

![Dashboard HR](https://github.com/filzarahma/edutech-hr-attrition/blob/main/filzrahma-dashboard/Edutech%20HR%20Dashboard_page-0001.jpg)

### b. Dashboard Demografi

* **Distribusi:**
  Pendidikan, gender, status pernikahan, total tahun kerja, survey score, usia
* **Key Insight:**

  * Pria = attrition lebih tinggi (17.4%)
  * Sarjana terbanyak, masa kerja 10 tahun = risiko tinggi
  * Work-life balance dinilai baik mayoritas

![Dashboard Demografi](https://github.com/filzarahma/edutech-hr-attrition/blob/main/filzrahma-dashboard/Edutech%20HR%20Dashboard_page-0002.jpg)

### c. Cara Menjalankan Dashboard Metabase

#### Prasyarat

* Minimal RAM 1GB
* File database `metabase.db.mv.db`
* [Docker](https://www.docker.com/products/docker-desktop/)

#### Langkah Menjalankan

1. Install Docker
2. Siapkan direktori & salin file database ke lokal

   ```bash
   mkdir C:\metabase-data
   copy "path\to\metabase.db.mv.db" C:\metabase-data\
   ```
3. Jalankan Metabase via Docker

   ```bash
   docker run -d -p 3000:3000 --name metabase -v C:/metabase-data:/metabase-data -e "MB_DB_FILE=/metabase-data/metabase.db.mv.db" metabase/metabase
   ```
4. Buka [http://localhost:3000](http://localhost:3000)
   **Login:**

   * Email: `admin@metabase.local`
   * Password: `metabase123`
5. Klik menu "Dashboard" untuk melihat visualisasi.

---

## 🤖 5. Machine Learning & Metodologi

### a. Preprocessing Data

1. **Drop** missing value pada target (`Attrition`)
2. **Hapus fitur tidak relevan:**
   `EmployeeCount`, `Over18`, `StandardHours`, `Age_Bin`, `YearsAtCompany_Bin`
3. **Encoding** data kategorikal (`LabelEncoder`)
4. **Scaling** fitur numerik (`MinMaxScaler`)
5. **Feature Engineering:**
   Tambah fitur `Potential Monthly Salary = 80 × HourlyRate`

### b. Algoritma yang Digunakan

* **ExtraTreesClassifier:**
  Cocok untuk fitur berkorelasi, randomisasi tinggi, atasi overfitting.
* **BalancedRandomForestClassifier:**
  Khusus untuk penanganan data tidak seimbang, lebih fokus pada kelas minoritas (resign).

### c. Penanganan Data Tidak Seimbang

* **Tanpa SMOTE:** Data asli, distribusi tidak diubah
* **Dengan SMOTE:** Oversampling minoritas (resign)

### d. Evaluasi & Optimasi Model

* **F1-score kelas minoritas** sebagai metrik utama
* **Optimasi threshold** untuk probabilitas ke kelas
* **Analisis Feature Importance**

**Model Terbaik:**
ExtraTreesClassifier tanpa SMOTE (F1-score: 0.59, Akurasi: 0.849)

### e. Fitur Aplikasi

* Form input data karyawan
* Hasil prediksi (probabilitas, status, visual gauge chart)
* Rekomendasi tindakan & insight faktor risiko
* Visualisasi fitur paling berpengaruh

---

## 📝 6. Kesimpulan & Rekomendasi

### Insight Utama

* **Overtime:** Risiko resign 3x lipat
* **Job Role:** Sales Rep = attrition 43.1%, Lab Technician = 26.1%
* **Usia Muda:** Risiko resign paling tinggi (38%)
* **Entry Level:** Lebih berisiko resign
* **Work-Life Balance:** Buruk = attrition 32.1%

### Rekomendasi Actionable

* **Review kebijakan lembur** (utamanya Sales & Lab Technician)
* **Program pengembangan karir** bagi entry/junior
* **Benchmark & revisi kompensasi** pada posisi rentan resign
* **Retensi usia muda** (18–30 thn) baik melalui pelatihan, rotasi, maupun fleksibilitas kerja
* **Penguatan work-life balance**
* **Review program stock option** agar lebih inklusif
* **Monitoring berkelanjutan** lewat dashboard
