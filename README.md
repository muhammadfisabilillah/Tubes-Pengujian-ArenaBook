# 🏸 ArenaBook - Automated Testing Project

[cite_start]Project ini berisi implementasi pengujian otomatis (*automated testing*) untuk sistem informasi pemesanan lapangan olahraga **ArenaBook**[cite: 5, 23]. [cite_start]Pengujian dilakukan menggunakan dua pendekatan utama: **Unit & Feature Testing (Backend)** menggunakan PEST Framework (PHP)[cite: 122], serta **UI Automation Testing (Front-end)** menggunakan Selenium WebDriver (Python).

---

## 🚀 Fitur Utama yang Diuji
1. [cite_start]**Autentikasi Pengguna (Login):** Validasi format email pada form login[cite: 38].
2. [cite_start]**Input Durasi Sewa:** Pengujian batas atas dan bawah durasi penyewaan lapangan (1-12 jam)[cite: 38].
3. [cite_start]**Kalkulasi Biaya & Diskon:** Pengujian logika perhitungan harga normal dan potongan untuk member[cite: 38].
4. [cite_start]**Status Pemesanan:** Validasi perubahan state transaksi dari *Menunggu Pembayaran* menjadi *Lunas*[cite: 38].
5. [cite_start]**Dashboard Jadwal:** Verifikasi keterpakaian slot lapangan secara *real-time* setelah pembayaran sukses[cite: 38].

---

## 🛠️ Prasyarat & Struktur Folder

Sebelum menjalankan testing, pastikan komputermu sudah terinstall:
* PHP >= 8.1 & Composer (Untuk PEST Framework)
* Python 3.x & pip (Untuk Selenium)
* Google Chrome (Untuk UI Testing)

### Struktur Project
```text
TUBES IMPLENTASI/
├── tests/
│   ├── Unit/
│   │   └── ArenaBookTest.php         # File pengujian unit logika bisnis (Bab 4.1)
│   └── Feature/
│       └── ArenaBookFeatureTest.php  # File pengujian fitur input & login (Bab 4.2)
├── ArenaBook.php                      # Logika backend utama sistem
├── index.html                         # Mockup UI Dashboard terintegrasi (Bab 5)
├── ui_test.py                         # Script otomatisasi Selenium (Python)
└── vendor/                            # Folder dependency Composer
