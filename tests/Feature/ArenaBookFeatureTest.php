<?php

require_once dirname(__DIR__, 2) . '/ArenaBook.php';

// ==========================================
// FEATURE 1: Autentikasi Pengguna (Login)
// ==========================================
test('EP Valid: Format email sesuai', function () {
    $arena = new ArenaBook();
    $result = $arena->login('user@arenabook.com');
    expect($result)->toBe('Berhasil login');
});

test('EP Invalid 1: Email tidak mengandung @', function () {
    $arena = new ArenaBook();
    $result = $arena->login('userarenabook.com');
    expect($result)->toBe('Format email salah');
});

test('EP Invalid 2: Email dikosongkan', function () {
    $arena = new ArenaBook();
    $result = $arena->login('');
    expect($result)->toBe('Email wajib diisi');
});

// ==========================================
// FEATURE 2: Input Durasi Sewa
// ==========================================
test('EP Valid: Durasi angka bulat 1-12', function () {
    $arena = new ArenaBook();
    $result = $arena->validasiDurasi(4);
    expect($result)->toBe('Durasi valid');
});

test('EP Invalid 1: Durasi angka negatif atau 0', function () {
    $arena = new ArenaBook();
    $result = $arena->validasiDurasi(-2);
    expect($result)->toBe('Durasi minimal 1 jam');
});

test('EP Invalid 2: Durasi lebih dari 12', function () {
    $arena = new ArenaBook();
    $result = $arena->validasiDurasi(15);
    expect($result)->toBe('Durasi maksimal 12 jam');
});