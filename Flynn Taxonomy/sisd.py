import sys, time

def main():
	n = int(sys.argv[1]) if len(sys.argv) >= 2 else 1_000_000
	start = time.perf_counter_ns()
	total = sum(i * i for i in range(1, n + 1))
	elapsed = time.perf_counter_ns() - start
	print(f"Flynn: SISD\nN: {n}\nTotal sum: {total}\nTime taken: {elapsed} nanoseconds")

if __name__ == "__main__":
	main()
