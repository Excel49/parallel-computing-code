# Nama: Muhamad Lingga Darmawan
# NIM: 152024042

# Serial vs Paralel Computing

Kode ini menunjukkan apakah komputasi paralel benar-benar meningkatkan performa dibanding serial.

## Parameter
1. **Proses**: Sum of squares (jumlah kuadrat)
2. **Jumlah data (N)**: 5.000.000
3. **Jumlah proses paralel**: 4

## Hasil Pengujian

| Mode | Script | N | Proses | Time (ns) | Time (ms) |
|------|--------|--:|-------:|----------:|----------:|
| Serial | `serial.py` | 5.000.000 | 1 | 264.777.200 | 264,78 |
| Paralel | `paralel.py` | 5.000.000 | 4 | 231.122.700 | 231,12 |

**Total sum**: `41666679166667500000` ✅ (kedua metode menghasilkan hasil yang sama)

**Selisih waktu**: 33.654.500 ns (~33,65 ms) — paralel **12,7% lebih cepat**.

## Penjelasan Skrip

### `serial.py`
- Menggunakan `sum()` generator expression untuk menghitung jumlah kuadrat secara sekuensial.
- Satu proses, satu aliran eksekusi.

### `paralel.py`
- Menggunakan `ProcessPoolExecutor` untuk membagi pekerjaan ke 4 proses.
- Data dibagi menjadi chunk menggunakan list comprehension, lalu setiap chunk dihitung secara paralel.

## Interpretasi

- Komputasi **paralel lebih cepat** dari serial untuk N = 5.000.000.
- Selisih waktu (~33 ms) relatif kecil karena overhead spawning proses di Windows cukup signifikan dibanding total waktu komputasi.
- Untuk workload yang lebih besar, keuntungan paralel akan semakin terasa.

## Catatan

- Variasi waktu antar run adalah normal.
- Untuk benchmark yang lebih akurat, jalankan beberapa kali dan ambil rata-rata/median.

&copy; 152024003 - Malendra Rizky
