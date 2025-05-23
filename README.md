# 🚀 Proyek Akhir: HR Attrition Prediction untuk Perusahaan Edutech

---

## 📑 Daftar Isi

1. [Business Understanding](#business-understanding)

   * [Permasalahan Bisnis](#permasalahan-bisnis)
     
   * [Cakupan Proyek](#cakupan-proyek)
     
3. [Struktur Repository](#struktur-repository)
4. [Persiapan Data](#persiapan-data)
5. [Business Dashboard](#business-dashboard)
   
    * [Dashboard HR & Informasi Pekerjaan](#dashboard-hr-&-informasi-pekerjaan)
      
    * [Dashboard Demografi](#dashboard-demografi)
      
    * [Cara Menjalankan Dashboard Metabase](#cara-menjalankan-dashboard-metabase)
      
7. [Machine Learning & Metodologi](#machine-learning--metodologi)
8. [Kesimpulan & Rekomendasi](#kesimpulan--rekomendasi)

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
  `http://localhost:8501` atau lihat [Demo Online](https://edutech-attrition-prediction.streamlit.app)
  
  ![image](https://github.com/user-attachments/assets/a98daf35-3afa-44f9-bf5e-c5a0628ebc1d)

---

## 📊 4. Business Dashboard

### a. Dashboard HR & Informasi Pekerjaan

* **Statistik Attrition:**

  * 179 resign dari 1.058 karyawan (16.92%)
* **Distribusi:**

  * Berdasarkan departemen, job role, job level, stock option, income band, dan overtime.
* **Key Insight:**

  * Attrition tertinggi terjadi pada Sales Department dan Role Sales Representative.
  * Entry level dan Junior adalah dua level terendah dalam perusahaan yang menyumbang lebih dari 80% kasus attrition.
  * Karyawan dengan stock option level 0 memiliki risiko resign tinggi dibandingkan level lainnya.
  * Karyawan yang lembur (overtime) memiliki risiko resign 3 kali lipat dibandingkan karyawan yang tidak lembur.

![Dashboard HR](https://github.com/filzarahma/edutech-hr-attrition/blob/main/filzrahma-dashboard/Edutech%20HR%20Dashboard_page-0001.jpg)

### b. Dashboard Demografi

* **Distribusi:**
  Pendidikan, gender, status pernikahan, total tahun kerja, survey score, usia
* **Key Insight:**

  * Pria memiliki attrition rate sedikit lebih tinggi (17.4%) dibandingkan wanita (16.2%).
  * Karyawan dengan status lajang (Single) rentan resign dibandingkan yang sudah menikah atau bercerai.
  * Tingkat pendidikan juga menjadi faktor, dengan lulusan Bachelor dan Master memiliki catatan kasus lebih banyak dibandingkan tingkat pendidikan yang lainnya. Hal ini juga bisa dipertimbangkan karena kebanyakan karyawan memiliki tingkat pendidikan S1 hingga S2.
  * Kelompok usia kurang dari 30 tahun merupakan kelompok yang paling rentan untuk mengundurkan diri.
  * Selain itu, dari hasil survei internal, karyawan dengan skor rendah pada work-life balance, job satisfaction, dan job involvement terutama yang mendapat skor 1 atau 2 memiliki kemungkinan besar untuk resign. 

![Dashboard Demografi](https://github.com/filzarahma/edutech-hr-attrition/blob/main/filzrahma-dashboard/Edutech%20HR%20Dashboard_page-0002.jpg)

### c. Cara Menjalankan Dashboard Metabase

1. **Install Docker**

   * Unduh dan install Docker Desktop dari [https://www.docker.com/products/docker-desktop/](https://www.docker.com/products/docker-desktop/).

2. **Siapkan Direktori dan Unduh File Database**

   * Buat folder khusus, misal `metabase-data`, lalu pindahkan file `metabase.db.mv.db` ke folder tersebut.

3. **Buka Command Prompt/Terminal**

   * Arahkan ke folder tempat file database berada (`metabase-data`).
   * Contoh perintah:

     ```bash
     cd path/to/metabase-data
     ```

4. **Jalankan Metabase dengan Docker**

   * Gunakan perintah berikut (otomatis kompatibel untuk Linux/Mac.
     Untuk Windows PowerShell, pastikan format path benar, atau gunakan `//c/metabase-data`):

     ```bash
     docker run -d -p 3000:3000 --name attrition \
       -v "$(pwd)/metabase.db.mv.db:/metabase.db/metabase.db.mv.db" \
       -e "MB_DB_FILE=/metabase.db/metabase.db.mv.db" \
       metabase/metabase
     ```

     > **Catatan:**
     >
     > * Jika di Windows CMD, ganti `$(pwd)` dengan path lengkap, misal:
     >   `-v "C:\metabase-data\metabase.db.mv.db:/metabase.db/metabase.db.mv.db"`
     > * Untuk PowerShell, bisa pakai:
     >   `-v "${PWD}\metabase.db.mv.db:/metabase.db/metabase.db.mv.db"`

5. **Akses Dashboard**

   * Buka browser ke [http://localhost:3000](http://localhost:3000)
   * **Login:**

     * Email: `filzarahmamuflihah@gmail.com`
     * Password: `SXj3m7MMKnCZzFP`
   * Pilih menu **Our Analytics** > **Dashboards** > **Edutech HR Dashboard** untuk melihat visualisasi.

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

**Hasil Analisis Feature Importance**
![image](https://github.com/user-attachments/assets/ad0d552b-9c5d-4f5d-9148-69dd71989362)


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
