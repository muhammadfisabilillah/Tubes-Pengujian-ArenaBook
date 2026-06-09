<?php

class ArenaBook {
    // Fungsi Bab 3 & Bab 4.1 (Unit Test)
    public function hitungBiayaSewa($jam, $isMember) {
        $hargaPerJam = 100000;
        $totalBiaya = $jam * $hargaPerJam;
        if ($jam >= 3) {
            $totalBiaya = $totalBiaya - 50000;
        }
        if ($isMember == true) {
            $totalBiaya = $totalBiaya * 0.9;
        }
        return $totalBiaya;
    }

    // Fungsi Bab 4.2 (Feature Test - Fitur 1: Autentikasi)
    public function login($email) {
        if (empty($email)) return "Email wajib diisi";
        if (!strpos($email, '@')) return "Format email salah";
        return "Berhasil login";
    }

    // Fungsi Bab 4.2 (Feature Test - Fitur 2: Input Durasi)
    public function validasiDurasi($jam) {
        if ($jam < 1) return "Durasi minimal 1 jam";
        if ($jam > 12) return "Durasi maksimal 12 jam";
        return "Durasi valid";
    }
}