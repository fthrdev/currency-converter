Advanced Currency Converter GUI
Made By ThurZ


📌 Deskripsi

Advanced Currency Converter adalah aplikasi desktop GUI berbasis Python yang memungkinkan pengguna untuk mengkonversi nilai mata uang antar berbagai jenis mata uang populer secara real-time menggunakan ExchangeRate-API.
Dirancang dengan tampilan antarmuka yang sederhana namun elegan menggunakan Tkinter.
✨ Fitur Utama

    ✅ Antarmuka grafis intuitif dan user-friendly (dibuat dengan Tkinter)

    🌐 Mendukung 20+ mata uang populer seperti USD, EUR, IDR, MYR, JPY, THB, dll

    🔃 Tombol Swap Currency untuk membalik pasangan mata uang

    📊 Format hasil sesuai simbol dan desimal mata uang lokal

    🕒 Label waktu otomatis saat konversi dilakukan

    🧮 Menampilkan nilai tukar aktual & konversi langsung

    🚫 Validasi input angka dan pesan error yang informatif

📷 Tampilan GUI

🛠️ Cara Menjalankan
1. Kebutuhan Sistem

    Python 3.8 atau lebih baru

    Koneksi internet (untuk fetch data API)

2. Install Dependencies

pip install requests

3. Clone Repo dan Jalankan

python currency_converter.py

🔑 API Key

Aplikasi ini menggunakan ExchangeRate-API untuk mengambil nilai tukar terkini.
Pastikan untuk mengganti API_KEY di kode dengan milik Anda:

self.API_KEY = 'YOUR_API_KEY_HERE'

🌍 Mata Uang yang Didukung

    USD (US Dollar)

    EUR (Euro)

    GBP (Pound Sterling)

    JPY (Yen Jepang)

    IDR (Rupiah Indonesia)

    MYR (Ringgit Malaysia)

    THB, VND, CNY, KRW, INR, SGD, AUD, CAD, CHF, AED, SAR, PHP, BRL, MXN
    dan banyak lagi...

💡 Catatan Teknis

    Data format mata uang (simbol dan jumlah desimal) telah diatur untuk beberapa mata uang lokal.

    Jika koneksi API gagal atau limit habis, akan muncul pesan error.

    Simbol mata uang dapat berbeda: IDR → Rp, JPY → ¥, KRW → ₩, dll.

📄 Lisensi

Proyek ini berada di bawah lisensi MIT License.
