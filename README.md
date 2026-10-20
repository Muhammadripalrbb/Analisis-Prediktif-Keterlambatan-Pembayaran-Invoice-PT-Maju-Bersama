Studi Kasus: Analisis Prediktif Keterlambatan Pembayaran Invoice PT Maju Bersama
1. Pemahaman Bisnis (Business Understanding)
Konteks Masalah: PT Maju Bersama mencatatkan tren kenaikan pendapatan (sales revenue) selama 2 tahun terakhir. Namun, laba bersih (net profit) justru turun 14% dan piutang (receivables) meroket hingga 300%. Arus kas operasional juga mengalami penurunan signifikan.

Hipotesis: Tingginya piutang dan terganggunya arus kas disebabkan oleh banyaknya pelanggan yang terlambat membayar tagihan (invoice) lebih dari 30 hari dari tanggal jatuh tempo (due date).

Tujuan Analitik: Membangun model Machine Learning klasifikasi untuk memprediksi apakah sebuah invoice berpotensi mengalami keterlambatan pembayaran (Late Payment) atau tidak.

2. Pemahaman & Persiapan Data (Data Understanding & Preparation)
Data Tersedia: Data historis 4.000 invoice dari 120 customer selama 2 tahun (Juli 2024 - Juni 2026).

Variabel Target: status_pembayaran (1 = Late, 0 = Not Late).

Pencegahan Kebocoran Data (Data Leakage): Pemateri menekankan pentingnya membuang kolom yang bisa membocorkan jawaban ke model (seperti tanggal_pembayaran_aktual atau lama_hari_terlambat). Kolom ini hanya ada setelah kejadian, sehingga tidak boleh dipakai untuk memprediksi masa depan.
