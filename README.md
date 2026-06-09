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



💻 Cara Menjalankan Pengujian
1. Backend Testing (PEST Framework - PHP)
Pastikan kamu sudah menginstall vendor dependency terlebih dahulu menggunakan terminal:

Bash
composer install
Menjalankan Unit Test (3 Test Cases - Basis Path):

Bash
./vendor/bin/pest tests/Unit/ArenaBookTest.php
Menjalankan Feature Test (6 Test Cases - Equivalence Partitioning):

Bash
./vendor/bin/pest tests/Feature/ArenaBookFeatureTest.php
2. UI Automation Testing (Selenium - Python)
Install library Selenium terlebih dahulu melalui terminal/command prompt:

Bash
pip install selenium
Jalankan script Python untuk melihat simulasi robot melakukan login, kalkulasi, dan bayar secara otomatis pada browser:

Bash
python ui_test.py
📊 Alur State Transition (UI Testing)
Script Selenium pada project ini berjalan berdasarkan skenario State Transition Diagram berikut:
Initial State ➔ Form Login ➔ Dashboard (Form Sewa) ➔ Menunggu Pembayaran ➔ Final State (Lunas & Terpakai).


---

### Langkah Akhir: Upload ke GitHub
Setelah file `README.md` disimpan, kamu tinggal meng- *upload* perubahan terbaru ini ke repository GitHub yang sudah kita sambungkan tadi dengan mengetikkan perintah ini di terminal VS Code:

```bash
git add README.md
git commit -m "Docs: Menambahkan README untuk panduan project"
git push origin main

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


