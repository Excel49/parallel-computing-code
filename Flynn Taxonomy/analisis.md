# Flynn's Taxonomy

Folder ini berisi demonstrasi **Flynn's Taxonomy** (SISD, SIMD, MISD, MIMD) menggunakan studi kasus yang sama: menghitung jumlah kuadrat (*sum of squares*).

Semua skrip dijalankan dengan **N = 1.000.000** dan menghasilkan hasil yang sama:

`Total sum = 333333833333500000`

## Apa yang Diwakili Setiap Skrip

### SISD (Single Instruction, Single Data)
- Satu aliran instruksi dieksekusi atas satu aliran data.
- Implementasi: Python `sum()` generator expression menghitung `i*i`.

### SIMD (Single Instruction, Multiple Data)
- Satu instruksi yang sama diterapkan ke banyak elemen data sekaligus.
- Implementasi: NumPy vectorization menggunakan dot product `x @ x`.

### MISD (Multiple Instruction, Single Data)
- Secara teori: beberapa aliran instruksi beroperasi pada aliran data yang sama.
- Implementasi: dua "aliran instruksi" berbeda menghitung hasil matematika yang sama:
	- metode loop (generator expression), dan
	- rumus tertutup $n(n+1)(2n+1)/6$ (lambda)
	kemudian dibandingkan untuk verifikasi kebenaran.

### MIMD (Multiple Instruction, Multiple Data)
- Beberapa aliran instruksi beroperasi pada beberapa aliran data (paralelisme sejati).
- Implementasi: membagi range menjadi chunk dan menggunakan banyak proses.

## Hasil Pengujian

| Flynn | Script | N | Workers | Time (ns) | Time (ms) | Speedup vs SISD |
|-------|--------|--:|--------:|----------:|----------:|-----------------:|
| SISD | `sisd.py` | 1.000.000 | 1 | 50.109.300 | 50,11 | 1,00× |
| SIMD | `simd.py` | 1.000.000 | (vectorized) | 2.776.000 | 2,78 | 18,05× |
| MISD | `misd.py` | 1.000.000 | 2 threads | 60.135.000 | 60,14 | 0,83× |
| MIMD | `mimd.py` | 1.000.000 | 12 | 226.657.000 | 226,66 | 0,22× |

