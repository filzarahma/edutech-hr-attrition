import joblib
import pandas as pd
import numpy as np
import streamlit as st
import os
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# Define paths to saved model and encoders
MODEL_PATH = 'model/model.joblib'
ENCODERS_PATH = 'model/label_encoders.joblib'
SCALER_PATH = 'model/scaler.joblib'

@st.cache_resource
def load_resources():
    """
    Load the trained model, label encoders, and scaler from disk
    """
    try:
        # Load model, encoders and scaler
        model = joblib.load(MODEL_PATH)
        encoders = joblib.load(ENCODERS_PATH)
        scaler = joblib.load(SCALER_PATH)
        return model, encoders, scaler
    except FileNotFoundError as e:
        st.error(f"❌ Error: Model files not found. {e}")
        return None, None, None

def create_feature_importance_chart(model, feature_names):
    """Create a feature importance chart"""
    importances = model.feature_importances_
    feat_importances = pd.Series(importances, index=feature_names)
    sorted_feat_importances = feat_importances.sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sorted_feat_importances.head(10).plot(kind='barh', ax=ax)
    plt.title("🔝 10 Fitur Terpenting", fontsize=14)
    plt.xlabel("Nilai Kepentingan Fitur")
    plt.ylabel("Fitur")
    plt.gca().invert_yaxis()  # Untuk menampilkan fitur dengan kepentingan tertinggi di atas
    plt.tight_layout()
    
    return fig

def main():
    st.set_page_config(
        page_title="Prediksi Attrition Karyawan",
        page_icon="👥",
        layout="wide"
    )
    
    # Load model, encoders, and scaler
    model, encoders, scaler = load_resources()
    if model is None or encoders is None or scaler is None:
        st.stop()
    
    # Header
    st.title("👥 Sistem Prediksi Attrition Karyawan")
    st.write("---")
    
    st.sidebar.header("📋 Panduan Penggunaan")
    st.sidebar.info("""
    1️⃣ Masukkan data karyawan pada form
    2️⃣ Klik tombol 'Prediksi' untuk melihat hasil
    3️⃣ Hasil akan menampilkan probabilitas resign dan rekomendasi
    """)
    
    with st.expander("ℹ️ Tentang Aplikasi"):
        st.write("""
        Aplikasi ini menggunakan model machine learning untuk memprediksi kemungkinan karyawan akan resign (attrition) berdasarkan berbagai faktor.
        
        🤖 Model dilatih menggunakan ensemble learning dengan algoritma tree-based yang menghasilkan tingkat akurasi tinggi dalam mengidentifikasi faktor-faktor yang mempengaruhi keputusan karyawan untuk resign.
        
        💡 Gunakan aplikasi ini sebagai alat pendukung keputusan untuk mengembangkan strategi retensi karyawan yang lebih efektif.
        """)
        
    
    # Create form for input
    st.header("👤 Data Karyawan")
    
    # Use columns to organize the form
    col1, col2, col3 = st.columns(3)
    
    with st.form("employee_data_form"):
        st.subheader("👤 Data Demografis")
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("🧓 Usia (tahun)", min_value=18, max_value=80, value=35)
            gender = st.selectbox("👫 Jenis Kelamin", ["Female", "Male"])
            marital_status = st.selectbox("💍 Status Pernikahan", ["Single", "Married", "Divorced"])
        
        with col2:
            distance = st.number_input("🏠 Jarak dari Rumah ke Kantor (km)", min_value=0, max_value=100, value=10)
            education = st.slider("🎓 Tingkat Pendidikan", min_value=1, max_value=5, value=3, 
                                help="1=Under College, 2=College, 3=Bachelor, 4=Master, 5=Doctor")
            education_field = st.selectbox("📚 Bidang Pendidikan", 
                                         ["Life Sciences", "Medical", "Marketing", "Technical Degree", "Human Resources", "Other"])
        
        st.subheader("💼 Pengalaman Kerja")
        col1, col2 = st.columns(2)
        with col1:
            num_companies = st.number_input("🏢 Jumlah Perusahaan Sebelumnya", min_value=0, max_value=20, value=2)
            total_working_years = st.number_input("⏳ Total Pengalaman Kerja (tahun)", min_value=0, max_value=50, value=10)
            training_times = st.number_input("📚 Jumlah Pelatihan Tahun Lalu", min_value=0, max_value=10, value=3)
        
        with col2:
            years_at_company = st.number_input("🏢 Lama di Perusahaan Ini (tahun)", min_value=0, max_value=40, value=5)
            years_in_role = st.number_input("👔 Lama di Posisi Saat Ini (tahun)", min_value=0, max_value=20, value=3)
            years_since_promotion = st.number_input("🚀 Waktu Sejak Promosi Terakhir (tahun)", min_value=0, max_value=15, value=1)
            years_with_manager = st.number_input("👨‍💼 Lama dengan Manajer Saat Ini (tahun)", min_value=0, max_value=17, value=3)
        
        st.subheader("🏢 Informasi Pekerjaan")
        col1, col2 = st.columns(2)
        with col1:
            department = st.selectbox("🏢 Departemen", ["Human Resources", "Research & Development", "Sales"])
            job_level = st.slider("📊 Level Jabatan", min_value=1, max_value=5, value=2)
            job_role = st.selectbox("👔 Peran Pekerjaan", 
                                  ["Healthcare Representative", "Human Resources", "Laboratory Technician", 
                                   "Manager", "Manufacturing Director", "Research Director", 
                                   "Research Scientist", "Sales Executive", "Sales Representative"])
        
        with col2:
            business_travel = st.selectbox("✈️ Frekuensi Perjalanan Bisnis", 
                                         ["Non-Travel", "Travel_Rarely", "Travel_Frequently"])
            overtime = st.selectbox("⏰ Apakah Melakukan Lembur?", ["No", "Yes"])
        
        st.subheader("💰 Kompensasi dan Benefit")
        col1, col2 = st.columns(2)
        with col1:
            daily_rate = st.number_input("💵 Tarif Harian", min_value=100, max_value=1500, value=800)
            hourly_rate = st.number_input("⏱️ Tarif per Jam", min_value=30, max_value=100, value=65)
            monthly_income = st.number_input("💰 Pendapatan Bulanan", min_value=1000, max_value=20000, value=6500)
        
        with col2:
            monthly_rate = st.number_input("📅 Tarif Bulanan", min_value=2000, max_value=27000, value=14000)
            percent_salary_hike = st.number_input("📈 Persentase Kenaikan Gaji Terakhir", min_value=0, max_value=25, value=15)
            stock_option = st.slider("📊 Level Opsi Saham", min_value=0, max_value=3, value=1)
        
        st.subheader("😊 Kepuasan dan Kinerja")
        col1, col2 = st.columns(2)
        with col1:
            job_satisfaction = st.slider("😊 Tingkat Kepuasan Kerja", min_value=0, max_value=5, value=3)
            environment_satisfaction = st.slider("🌟 Tingkat Kepuasan Lingkungan", min_value=0, max_value=5, value=3)
            relationship_satisfaction = st.slider("👥 Tingkat Kepuasan Relasi", min_value=0, max_value=5, value=3)
        
        with col2:
            job_involvement = st.slider("💼 Tingkat Keterlibatan Kerja", min_value=0, max_value=5, value=3)
            work_life_balance = st.slider("⚖️ Keseimbangan Kerja-Hidup", min_value=0, max_value=5, value=3)
            performance_rating = st.slider("⭐ Penilaian Kinerja", min_value=0, max_value=5, value=3)
        
        submitted = st.form_submit_button("🚀 Prediksi Attrition")
    
    # Handle form submission
    if submitted:
        # Collect data
        employee_data = {
            'Age': age,
            'Gender': gender,
            'MaritalStatus': marital_status,
            'DistanceFromHome': distance,
            'Education': education,
            'EducationField': education_field,
            'NumCompaniesWorked': num_companies,
            'TotalWorkingYears': total_working_years,
            'TrainingTimesLastYear': training_times,
            'Department': department,
            'JobLevel': job_level,
            'JobRole': job_role,
            'BusinessTravel': business_travel,
            'OverTime': overtime,
            'DailyRate': daily_rate,
            'HourlyRate': hourly_rate,
            'MonthlyIncome': monthly_income,
            'MonthlyRate': monthly_rate,
            'PercentSalaryHike': percent_salary_hike,
            'StockOptionLevel': stock_option,
            'YearsAtCompany': years_at_company,
            'YearsInCurrentRole': years_in_role,
            'YearsSinceLastPromotion': years_since_promotion,
            'YearsWithCurrManager': years_with_manager,
            'JobSatisfaction': job_satisfaction,
            'EnvironmentSatisfaction': environment_satisfaction,
            'JobInvolvement': job_involvement,
            'WorkLifeBalance': work_life_balance,
            'RelationshipSatisfaction': relationship_satisfaction,
            'PerformanceRating': performance_rating
        }
        
        # Feature Engineering
        employee_data['PotentialMonthlySalary'] = 80 * employee_data['HourlyRate']
        
        # Convert to DataFrame
        input_df = pd.DataFrame([employee_data])
        
        # Preprocess data
        # 1. Encode categorical variables
        for col, encoder in encoders.items():
            if col in input_df.columns:
                try:
                    input_df[col] = encoder.transform(input_df[col])
                except ValueError as e:
                    st.error(f"❌ Error encoding {col}: {e}")
                    st.stop()
        
        # 2. Apply scaling to numerical columns
        numeric_columns = ['Age', 'DailyRate', 'DistanceFromHome', 'HourlyRate', 
                          'MonthlyIncome', 'MonthlyRate', 'NumCompaniesWorked', 
                          'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear',
                          'YearsAtCompany', 'YearsInCurrentRole', 
                          'YearsSinceLastPromotion', 'YearsWithCurrManager', 
                          'PotentialMonthlySalary']
        
        input_df[numeric_columns] = scaler.transform(input_df[numeric_columns])
        
        # Make prediction
        # Fix: Ensure features are in the correct order expected by the model
        expected_columns = model.feature_names_in_  # Get the column names the model expects
        
        # Make sure the DataFrame has all expected columns in the right order
        for column in expected_columns:
            if column not in input_df.columns:
                st.error(f"❌ Missing feature: {column}")
                st.stop()
        
        # Reorder the DataFrame to match the expected feature order
        input_df = input_df[expected_columns]
        
        # Now make the prediction
        attrition_prob = model.predict_proba(input_df)[:, 1][0]
        prediction = 1 if attrition_prob >= 0.5 else 0
        
        # Display results
        st.write("---")
        st.header("📋 Hasil Prediksi")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Probabilitas Attrition")
            
            # Create gauge chart for probability
            
            fig, ax = plt.subplots(figsize=(5, 3))  # Increased figure size for better visibility
            
            # Create a simple gauge
            gauge_colors = ['green', 'yellowgreen', 'gold', 'orange', 'red']
            bounds = [0, 0.2, 0.4, 0.6, 0.8, 1.0]
            norm = plt.Normalize(0, 1)
            
            # Create color bar as gauge
            sm = plt.cm.ScalarMappable(cmap=plt.cm.RdYlGn_r, norm=norm)
            sm.set_array([])
            
            ax.set_xlim(0, 1)
            ax.set_ylim(-0.5, 0.5)  # Adjusted y-limits to center the gauge
            ax.set_aspect('equal')
            ax.add_patch(plt.Circle((0.5, 0), 0.4, color='white', zorder=0))
            for i in range(len(bounds)-1):
                ax.add_patch(plt.Rectangle((bounds[i], 0), bounds[i+1]-bounds[i], 0.1, 
                                         color=gauge_colors[i], zorder=1))
            
            # Add needle
            angle = (1 - attrition_prob) * np.pi
            needle_length = 0.4
            ax.add_patch(plt.Circle((0.5, 0), 0.05, color='black', zorder=2))
            ax.plot([0.5, 0.5 + needle_length * np.cos(angle)], 
                  [0, 0 + needle_length * np.sin(angle)], 
                  color='black', linewidth=4, zorder=3)
            
            # Remove axes
            ax.set_axis_off()
            
            # Add text below the gauge (adjusted positions)
            risk_level = ""
            if attrition_prob < 0.2:
                risk_level = "✅ SANGAT RENDAH"
            elif attrition_prob < 0.4:
                risk_level = "✅ RENDAH"
            elif attrition_prob < 0.6:
                risk_level = "⚠️ SEDANG"
            elif attrition_prob < 0.8:
                risk_level = "🔴 TINGGI"
            else:
                risk_level = "🚨 SANGAT TINGGI"
                
            ax.text(0.5, -0.25, f"Probabilitas: {attrition_prob:.2%}", ha='center', fontsize=12, fontweight='bold')
            ax.text(0.5, -0.35, f"Tingkat Risiko: {risk_level}", ha='center', fontsize=14, 
                   color='red' if attrition_prob > 0.5 else 'green', fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig)
            
        with col2:
            st.subheader("📝 Hasil & Rekomendasi")
            
            if prediction == 1:
                st.error("❌ Karyawan diprediksi: **AKAN RESIGN**")
                st.markdown("""
                ### 🚨 Rekomendasi:
                1. 🎯 Segera lakukan interview untuk mengetahui alasan potensial
                2. 💰 Pertimbangkan untuk memberikan insentif retensi
                3. ⚖️ Periksa beban kerja dan keseimbangan hidup-kerja karyawan
                4. 💵 Evaluasi gaji dan tunjangan dibandingkan dengan standar industri
                """)
            else:
                st.success("✅ Karyawan diprediksi: **TIDAK AKAN RESIGN**")
                st.markdown("""
                ### ✅ Rekomendasi:
                1. 📈 Tetap pantau tingkat kepuasan dan keterlibatan kerja
                2. 🚀 Berikan kesempatan pengembangan karir yang berkelanjutan
                3. 📋 Lakukan evaluasi berkala untuk memastikan karyawan tetap termotivasi
                """)
                
        st.write("---")
        
        # Display important factors that might be influencing this prediction
        st.subheader("⚠️ Faktor-faktor yang Mungkin Mempengaruhi Prediksi")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if overtime == "Yes":
                st.warning("⚠️ Karyawan melakukan lembur")
            
            if job_satisfaction < 3:
                st.warning("😕 Tingkat kepuasan kerja rendah")
                
            if work_life_balance < 3:
                st.warning("⚖️ Keseimbangan kerja-hidup kurang baik")
        
        with col2:
            if stock_option < 1:
                st.warning("💰 Tidak memiliki opsi saham")
            
            if monthly_income < 3000:
                st.warning("💵 Gaji relatif rendah")
                
            if years_since_promotion > 3:
                st.warning("📊 Lama tidak mendapatkan promosi")
        
        with col3:
            if distance > 15:
                st.warning("🏠 Jarak ke kantor jauh")
            
            if environment_satisfaction < 3:
                st.warning("🏢 Tingkat kepuasan lingkungan rendah")
                
            if job_involvement < 3:
                st.warning("💼 Keterlibatan kerja rendah")

if __name__ == "__main__":
    main()
