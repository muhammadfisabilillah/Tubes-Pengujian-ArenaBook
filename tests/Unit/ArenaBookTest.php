<?php

require_once __DIR__ . '/../../ArenaBook.php';

// Path 1: Jam < 3, Bukan Member (Expected: 200000)
test('Path 1: hitung biaya sewa di bawah 3 jam untuk non-member', function () {
    // Arrange
    $arena = new ArenaBook();
    
    // Act
    $result = $arena->hitungBiayaSewa(2, false);
    
    // Assert
    expect($result)->toBe(200000);
});

// Path 2: Jam >= 3, Bukan Member (Expected: 250000)
test('Path 2: hitung biaya sewa 3 jam atau lebih untuk non-member', function () {
    // Arrange
    $arena = new ArenaBook();
    
    // Act
    $result = $arena->hitungBiayaSewa(3, false);
    
    // Assert
    expect($result)->toBe(250000);
});

// Path 3: Jam < 3, Adalah Member (Expected: 180000)
test('Path 3: hitung biaya sewa di bawah 3 jam untuk member', function () {
    // Arrange
    $arena = new ArenaBook();
    
    // Act
    $result = $arena->hitungBiayaSewa(2, true);
    
    // Assert
    expect($result)->toBe(180000.0);
});