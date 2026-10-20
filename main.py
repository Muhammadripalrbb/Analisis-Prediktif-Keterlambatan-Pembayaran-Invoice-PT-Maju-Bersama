import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# ==========================================
# TAHAP 1: SIMULASI DATA (Sesuai Konteks PT Maju Bersama)
# ==========================================
np.random.seed(42)
n_data = 4000 # Jumlah invoice

# Membuat dataset tiruan berdasarkan materi
data = {
    'id_invoice': range(1, n_data + 1),
    'nilai_tagihan': np.random.randint(1000000, 50000000, n_data),
    'metode_pembayaran': np.random.choice(['Transfer Bank', 'Kartu Kredit', 'Cek', 'Tempo 30 Hari'], n_data),
    'riwayat_telat_sebelumnya': np.random.randint(0, 5, n_data), # Jumlah telat sebelumnya
    'kategori_customer': np.random.choice(['Retail', 'Korporat', 'Distributor'], n_data),
    
    # Kolom ini berpotensi menyebabkan Data Leakage (harus dibuang nanti)
    'lama_hari_telat_aktual': np.random.randint(0, 60, n_data), 
}

df = pd.DataFrame(data)

# Membuat target class berdasarkan hari telat (>30 hari dianggap Late)
# 1 = Late, 0 = Not Late
df['status_pembayaran'] = np.where(df['lama_hari_telat_aktual'] > 30, 1, 0)

# ==========================================
# TAHAP 2: DATA PREPARATION & MENCEGAH DATA LEAKAGE
# ==========================================
print("Mempersiapkan data dan membuang fitur yang menyebabkan kebocoran data...")
# Membuang ID dan kolom yang bocor (lama_hari_telat_aktual)
df_bersih = df.drop(columns=['id_invoice', 'lama_hari_telat_aktual'])

# Encoding data kategorikal menjadi numerik agar bisa dibaca mesin
le = LabelEncoder()
df_bersih['metode_pembayaran'] = le.fit_transform(df_bersih['metode_pembayaran'])
df_bersih['kategori_customer'] = le.fit_transform(df_bersih['kategori_customer'])

# ==========================================
# TAHAP 3: PARTISI DATA (Train-Test Split)
# ==========================================
# X = Fitur (Variabel Independen), y = Target (Variabel Dependen)
X = df_bersih.drop(columns=['status_pembayaran'])
y = df_bersih['status_pembayaran']

# Membagi data: 80% untuk melatih model (training), 20% untuk pengujian (testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# ==========================================
# TAHAP 4: PEMODELAN (Modeling)
# ==========================================
print("Melatih model Random Forest (seperti yang didemonstrasikan di KNIME)...")
# Pemateri mencontohkan penggunaan Random Forest Learner
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Melakukan prediksi pada data testing
y_pred = rf_model.predict(X_test)

# ==========================================
# TAHAP 5: EVALUASI (Scorer)
# ==========================================
print("\n=== HASIL EVALUASI MODEL ===")
akurasi = accuracy_score(y_test, y_pred)
print(f"Tingkat Akurasi (Accuracy) : {akurasi * 100:.2f}%")
print("\nLaporan Klasifikasi Detail:")
print(classification_report(y_test, y_pred, target_names=['Not Late (0)', 'Late (1)']))