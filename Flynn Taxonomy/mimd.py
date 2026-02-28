import os, sys, time
from concurrent.futures import ProcessPoolExecutor

def sum_sq(bounds):
	return sum(i * i for i in range(bounds[0], bounds[1] + 1))

def main():
	n = int(sys.argv[1]) if len(sys.argv) >= 2 else 1_000_000
	w = int(sys.argv[2]) if len(sys.argv) >= 3 else (os.cpu_count() or 2)

	cs = n // w
	chunks = [(p * cs + 1, (p + 1) * cs if p < w - 1 else n) for p in range(w)]

	start = time.perf_counter_ns()
	with ProcessPoolExecutor(max_workers=w) as pool:
		total = sum(pool.map(sum_sq, chunks))
	elapsed = time.perf_counter_ns() - start

	print(f"Flynn: MIMD\nN: {n}\nWorkers: {w}\nTotal sum: {total}\nTime taken: {elapsed} nanoseconds")

if __name__ == "__main__":
	main()
