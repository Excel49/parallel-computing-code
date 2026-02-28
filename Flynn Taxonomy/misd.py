import sys, time
from concurrent.futures import ThreadPoolExecutor

def main():
	n = int(sys.argv[1]) if len(sys.argv) >= 2 else 1_000_000

	start = time.perf_counter_ns()
	with ThreadPoolExecutor(max_workers=2) as pool:
		f_loop = pool.submit(lambda: sum(i * i for i in range(1, n + 1)))
		f_formula = pool.submit(lambda: n * (n + 1) * (2 * n + 1) // 6)
		total_loop, total_formula = f_loop.result(), f_formula.result()
	elapsed = time.perf_counter_ns() - start

	print(f"Flynn: MISD\nN: {n}\nTotal sum (loop): {total_loop}")
	print(f"Total sum (formula): {total_formula}\nMatch: {total_loop == total_formula}")
	print(f"Time taken: {elapsed} nanoseconds")

if __name__ == "__main__":
	main()
