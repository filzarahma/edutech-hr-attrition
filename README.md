# 🚀 Proyek Akhir: HR Attrition Prediction untuk Perusahaan Edutech

## 📑 Daftar Isi

* [Business Understanding](#business-understanding)

  * [Permasalahan Bisnis](#permasalahan-bisnis)
  * [Cakupan Proyek](#cakupan-proyek)
  * [Persiapan Data](#persiapan-data)
* [Struktur Repository](#struktur-repository)
* [Business Dashboard](#business-dashboard)

  * [Dashboard HR & Informasi Pekerjaan](#dashboard-hr--informasi-pekerjaan)
  * [Dashboard Demografi](#dashboard-demografi)
  * [Cara Menjalankan Dashboard Metabase](#cara-menjalankan-dashboard-metabase)
* [Machine Learning & Metodologi](#machine-learning--metodologi)

  * [Preprocessing Data](#preprocessing-data)
  * [Algoritma yang Digunakan](#algoritma-yang-digunakan)
  * [Penanganan Data Tidak Seimbang](#penanganan-data-tidak-seimbang)
  * [Evaluasi & Optimasi Model](#evaluasi--optimasi-model)
  * [Menjalankan Aplikasi Prediksi](#menjalankan-aplikasi-prediksi)
* [Kesimpulan & Rekomendasi](#kesimpulan--rekomendasi)
* [Environment & Dependencies](#environment--dependencies)

---

## 🏢 Business Understanding

Perusahaan Edutech adalah perusahaan teknologi pendidikan yang berkembang dengan fokus pada Research & Development (R\&D), Sales, dan Human Resources. Saat ini, perusahaan menghadapi tantangan besar dalam mempertahankan talenta terbaiknya, khususnya karena tingginya tingkat **attrition** (pengunduran diri karyawan), terutama di departemen Sales serta pada posisi Sales Representative dan Laboratory Technician.

### ❓ Permasalahan Bisnis

Data internal menunjukkan **tingkat attrition mencapai 16,92%**, jauh di atas standar industri yang ideal (5–10%). Hal ini membuat perusahaan perlu memahami faktor-faktor penyebab dan mengembangkan strategi prediktif dan preventif yang berbasis data.

### 📋 Cakupan Proyek

1. **Analisis Data Karyawan**
   Analisis komprehensif untuk memahami faktor-faktor attrition.
2. **Pembangunan Model Prediktif**
   Model machine learning untuk memprediksi kemungkinan resign.
3. **Pengembangan Aplikasi Prediksi**
   Streamlit app untuk tim HR memprediksi risiko attrition.
4. **Visualisasi Data**
   Dashboard interaktif di Metabase.
5. **Rekomendasi Strategi Retensi**
   Rekomendasi berbasis data untuk mengurangi attrition.

---

## 📁 Struktur Repository

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
## ⚙️ Persiapan Data

* **Sumber data**: Dataset [karyawan](https://raw.githubusercontent.com/dicodingacademy/dicoding_dataset/main/employee/employee_data.csv) yang digunakan berasal dari Dicoding, terdiri dari 1.470 data karyawan dengan 35 variabel penting, seperti data demografi, riwayat pekerjaan, dan tingkat kepuasan kerja. Target utama pada dataset adalah kolom Attrition (0 = tidak resign, 1 = resign).
* **Penjelasan fitur**: Lihat pada dokumentasi [berikut](https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/README.md).
* **Setup environment**:


---

## 📊 Business Dashboard

### 1. Dashboard HR & Informasi Pekerjaan

* **Overview attrition**: 179 resign dari 1058 karyawan (16.92%)
* **Distribusi**: Berdasarkan departemen, job role, job level, stock option, income band, dan overtime
* **Key Insight**:

  * Sales department & Sales Rep = attrition tertinggi
  * Entry level & stock option 0 = risiko resign tinggi
  * Overtime = risiko resign lebih tinggi (31%)

![Dashboard HR](https://github.com/filzarahma/edutech-hr-attrition/blob/main/filzrahma-dashboard/Edutech%20HR%20Dashboard_page-0001.jpg)

### 2. Dashboard Demografi

* **Distribusi**: Pendidikan, gender, status pernikahan, total tahun kerja, survey score, usia
* **Key Insight**:

  * Pria = attrition lebih tinggi (17.4%)
  * Sarjana terbanyak, masa kerja 10 tahun = risiko tinggi
  * Work-life balance dinilai baik oleh mayoritas

![Dashboard Demografi](https://github.com/filzarahma/edutech-hr-attrition/blob/main/filzrahma-dashboard/Edutech%20HR%20Dashboard_page-0002.jpg)

### 🖥️ Cara Menjalankan Dashboard Metabase

**Prasyarat:**

* Minimal 1GB RAM
* File `metabase.db.mv.db`
* Docker

**Langkah:**

1. Install [Docker](https://www.docker.com/products/docker-desktop/)
2. Siapkan direktori & copy file database ke lokal

   ```bash
   mkdir C:\metabase-data
   copy "path\to\metabase.db.mv.db" C:\metabase-data\
   ```
3. Jalankan Metabase dengan Docker:

   ```bash
   docker run -d -p 3000:3000 --name metabase -v C:/metabase-data:/metabase-data -e "MB_DB_FILE=/metabase-data/metabase.db.mv.db" metabase/metabase
   ```
4. Buka [http://localhost:3000](http://localhost:3000)
   Login:

   * Email: `admin@metabase.local`
   * Password: `metabase123`
5. Klik menu "Dashboard" untuk melihat visualisasi.

---

## 🤖 Machine Learning & Metodologi

### Preprocessing Data

1. **Drop** missing value pada target (`Attrition`)
2. **Hapus fitur non-variatif/tidak relevan**: EmployeeCount, Over18, StandardHours, Age\_Bin, YearsAtCompany\_Bin
3. **Encoding** data kategorikal (`LabelEncoder`)
4. **Scaling** numerik (`MinMaxScaler`)
5. **Feature Engineering**: Potential Monthly Salary = 80 × HourlyRate

### Algoritma yang Digunakan

* **ExtraTreesClassifier**

  * Keunggulan: Randomisasi tinggi, atasi overfitting, cocok untuk fitur berkorelasi
* **BalancedRandomForestClassifier**

  * Untuk data tidak seimbang (minoritas = resign)
  * Keunggulan: Fokus pada kelas minoritas, performa lebih baik pada recall/F1 minoritas

### Penanganan Data Tidak Seimbang

* **Tanpa SMOTE**: Data asli, distribusi tidak diubah
* **Dengan SMOTE**: Oversampling minoritas (resign)

### Evaluasi & Optimasi Model

* **F1-score kelas minoritas** (utama)
* **Optimasi threshold** untuk konversi probabilitas ke kelas
* **Analisis Feature Importance**

**Model terbaik:**
ExtraTreesClassifier tanpa SMOTE (F1-score: 0.59, Akurasi: 0.849)

### 🚀 Menjalankan Aplikasi Prediksi

#### Prasyarat

* Python 3.8+
* Semua package di `requirements.txt`
* File model di folder `/model`

#### Langkah-langkah

1. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```
2. Jalankan aplikasi

   ```bash
   streamlit run prediction.py
   ```
3. Akses di browser via `http://localhost:8501`

#### Fitur Aplikasi

* Form input data karyawan
* Hasil prediksi (probabilitas, status, visual gauge chart)
* Rekomendasi tindakan & insight faktor risiko
* Visualisasi fitur paling berpengaruh

**Akses aplikasi demo:**
[https://edutech-attrition-prediction.streamlit.app](https://edutech-attrition-prediction.streamlit.app)

---

## 📝 Kesimpulan & Rekomendasi

### Insight Utama

* **Overtime**: Risiko resign 3x lipat
* **Job Role**: Sales Rep = attrition 43.1%, Lab Technician = 26.1%
* **Usia Muda**: Risiko resign paling tinggi (38%)
* **Entry Level**: Lebih berisiko resign
* **Work-Life Balance**: Buruk = attrition 32.1%

### Rekomendasi Action Items

* **Review kebijakan lembur** terutama untuk Sales & Lab Technician
* **Program pengembangan karir** untuk entry/junior
* **Benchmark & revisi kompensasi** pada posisi rentan resign
* **Retensi usia muda** (18–30 thn): Pelatihan, rotasi, fleksibilitas kerja
* **Penguatan work-life balance**
* **Review program stock option** untuk memperluas kepemilikan
* **Monitoring berkelanjutan** melalui dashboard

---

## 🛠️ Environment & Dependencies

Gunakan package berikut pada `requirements.txt`:

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
