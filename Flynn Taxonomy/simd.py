import sys, time
import numpy as np

def main():
	n = int(sys.argv[1]) if len(sys.argv) >= 2 else 1_000_000
	start = time.perf_counter_ns()
	x = np.arange(1, n + 1, dtype=np.int64)
	total = int(x @ x)  # dot product = sum of squares, no intermediate array
	elapsed = time.perf_counter_ns() - start
	print(f"Flynn: SIMD\nN: {n}\nTotal sum: {total}\nTime taken: {elapsed} nanoseconds")

if __name__ == "__main__":
	main()
