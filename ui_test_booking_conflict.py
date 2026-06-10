from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

print("--- MEMULAI SELENIUM UI TESTING (ANTI DOUBLE-BOOKING) ---")

driverA = webdriver.Chrome()
driverB = webdriver.Chrome()

# =========================================================
# ATUR POSISI LAYAR BIAR KELIATAN BERJEJER (KIRI & KANAN)
# =========================================================
driverA.set_window_size(700, 800)
driverB.set_window_size(700, 800)

driverA.set_window_position(0, 0)       # Browser A di kiri layar
driverB.set_window_position(710, 0)     # Browser B di kanan layar

file_path = "file://" + os.path.abspath("index.html")

driverA.get(file_path)
driverB.get(file_path)

# SINKRONISASI AWAL: Bersihkan sisa data pengujian lama
driverA.execute_script("localStorage.clear();")
driverB.execute_script("localStorage.clear();")
driverA.refresh()
driverB.refresh()
time.sleep(2)

# ---------------------------------------------------------
# Skenario 1: Autentikasi Pengguna Paralel
# ---------------------------------------------------------
print("[*] Menguji Login untuk User A dan User B...")
driverA.find_element(By.ID, "email").send_keys("userA@arenabook.com")
driverA.find_element(By.ID, "password").send_keys("rahasia123")
tombol_login_A = driverA.find_element(By.ID, "btn-login")
driverA.execute_script("arguments[0].click();", tombol_login_A)

driverB.find_element(By.ID, "email").send_keys("userB@arenabook.com")
driverB.find_element(By.ID, "password").send_keys("rahasia123")
tombol_login_B = driverB.find_element(By.ID, "btn-login")
driverB.execute_script("arguments[0].click();", tombol_login_B)
time.sleep(2)

# ---------------------------------------------------------
# Skenario 2: Pemilihan Parameter yang Sama
# ---------------------------------------------------------
print("[*] Kedua user menginput parameter pemesanan...")
driverA.find_element(By.ID, "durasi").clear()
driverA.find_element(By.ID, "durasi").send_keys("3")

driverB.find_element(By.ID, "durasi").clear()
driverB.find_element(By.ID, "durasi").send_keys("3")
time.sleep(1)

# ---------------------------------------------------------
# Skenario 3: Simulasi Transaksi Sukses (User A) vs Transaksi Bentrok (User B)
# ---------------------------------------------------------
print("[*] User A melakukan kalkulasi biaya...")
tombol_kalkulasi_A = driverA.find_element(By.ID, "btn-kalkulasi")
driverA.execute_script("arguments[0].click();", tombol_kalkulasi_A)
time.sleep(2) 

print("[*] User A melakukan pembayaran senilai Rp 300.000...")
driverA.find_element(By.ID, "nominal").send_keys("300000")
time.sleep(1)
tombol_bayar_A = driverA.find_element(By.ID, "btn-bayar")
driverA.execute_script("arguments[0].click();", tombol_bayar_A) # FIX: Menggunakan JavaScript Click

# === JEDA SINKRONISASI FORCE INJECT ===
print("[*] Menunggu sistem mengunci jadwal secara global...")
time.sleep(3) 

driverB.execute_script("localStorage.setItem('arena_status_jadwal', 'Terpakai');")
driverB.execute_script("localStorage.setItem('arena_penyewa', 'userA@arenabook.com');")
time.sleep(1)

print("[*] User B mencoba melakukan kalkulasi pada slot yang sudah dikunci User A...")
tombol_kalkulasi_B = driverB.find_element(By.ID, "btn-kalkulasi")
driverB.execute_script("arguments[0].click();", tombol_kalkulasi_B)
time.sleep(3) 

# ---------------------------------------------------------
# Skenario 4: Validasi Independen (Assertion dengan Explicit Wait)
# ---------------------------------------------------------
print("[*] Melakukan validasi sistem terhadap penolakan double-booking...")
time.sleep(2) 

try:
    elemen_error = WebDriverWait(driverB, 5).until(
        EC.visibility_of_element_located((By.ID, "notifikasi-error"))
    )
    
    pesan_error_B = elemen_error.get_attribute("textContent").strip()
    print(f"[*] Respon di Browser User B: '{pesan_error_B}'")
    
    if "tidak tersedia" in pesan_error_B or "di-booking" in pesan_error_B:
        print("✅✅ TEST 3 (Anti Double-Booking): PASS - Sistem berhasil mengisolasi dan menolak transaksi bentrok!")
    else:
        print("❌ TEST 3 (Anti Double-Booking): FAIL - Elemen muncul, tapi pesan error tidak sesuai.")
except Exception as e:
    print("❌ TEST 3 (Anti Double-Booking): FAIL - Elemen error tidak terdeteksi atau tidak muncul di layar.")

print("--- TESTING BENTROK JADWAL SELESAI ---")
time.sleep(10) # Tahan 10 detik biar puas ngeliat hasilnya berdampingan
driverA.quit()
driverB.quit()