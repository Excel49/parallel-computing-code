import time

N = 5_000_000
start = time.perf_counter_ns()
total = sum(i * i for i in range(1, N + 1))
elapsed = time.perf_counter_ns() - start

print(f"Total sum: {total}\nTime taken: {elapsed} nanoseconds")
