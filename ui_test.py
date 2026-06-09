from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

print("--- MEMULAI SELENIUM UI TESTING (FULL SKENARIO) ---")

driver = webdriver.Chrome()
file_path = "file://" + os.path.abspath("index.html")
driver.get(file_path)
time.sleep(2)

# ---------------------------------------------------------
# Test 1: Autentikasi Pengguna (Login)
# ---------------------------------------------------------
print("[*] Menguji Form Login...")
input_email = driver.find_element(By.ID, "email")
input_email.send_keys("muhammad@arenabook.com")
time.sleep(1)

driver.find_element(By.ID, "password").send_keys("rahasia123")
time.sleep(1)

driver.find_element(By.ID, "btn-login").click()
time.sleep(2) # Jeda untuk transisi masuk ke Dashboard

# Verifikasi apakah berhasil masuk
user_display = driver.find_element(By.ID, "user-display").text
if "muhammad@arenabook.com" in user_display:
    print("✅ TEST 1 (Login): PASS - Berhasil masuk ke Dashboard")
else:
    print("❌ TEST 1 (Login): FAIL")

# ---------------------------------------------------------
# Simulasi Fitur 2 & 3: Input Durasi & Kalkulasi Biaya
# ---------------------------------------------------------
print("[*] Mengisi durasi sewa dan centang member...")
input_durasi = driver.find_element(By.ID, "durasi")
input_durasi.clear()
input_durasi.send_keys("3")
time.sleep(1)

driver.find_element(By.ID, "isMember").click()
time.sleep(1)

driver.find_element(By.ID, "btn-kalkulasi").click()
time.sleep(1)

tagihan = driver.find_element(By.ID, "total-tagihan").text
print(f"[*] Tagihan hasil kalkulasi: {tagihan}")

# ---------------------------------------------------------
# Test 2: State Transition (Pembayaran & Update Dashboard)
# ---------------------------------------------------------
status_awal = driver.find_element(By.ID, "status").text
print(f"[*] Status Awal: {status_awal}")

print("[*] Melakukan pembayaran...")
input_nominal = driver.find_element(By.ID, "nominal")
input_nominal.send_keys("300000")
time.sleep(1)

driver.find_element(By.ID, "btn-bayar").click()
time.sleep(2)

status_akhir = driver.find_element(By.ID, "status").text
status_jadwal = driver.find_element(By.ID, "status-jadwal").text

print(f"[*] Status Akhir Pembayaran: {status_akhir}")
print(f"[*] Status Akhir Jadwal: {status_jadwal}")

if status_akhir == "Lunas" and status_jadwal == "Terpakai":
    print("✅ TEST 2 (State Transition): PASS - Semua status terupdate dengan benar!")
else:
    print("❌ TEST 2 (State Transition): FAIL")

print("--- TESTING SELESAI ---")
time.sleep(3) # Tahan layar 3 detik di akhir biar cantik saat direkam
driver.quit()