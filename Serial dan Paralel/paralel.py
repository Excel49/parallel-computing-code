from concurrent.futures import ProcessPoolExecutor
import time

N = 5_000_000
NUM_PROC = 4

def sum_sq(bounds):
    return sum(i * i for i in range(bounds[0], bounds[1] + 1))

if __name__ == "__main__":
    cs = N // NUM_PROC
    chunks = [(p * cs + 1, (p + 1) * cs if p < NUM_PROC - 1 else N) for p in range(NUM_PROC)]

    start = time.perf_counter_ns()
    with ProcessPoolExecutor(max_workers=NUM_PROC) as pool:
        total = sum(pool.map(sum_sq, chunks))
    elapsed = time.perf_counter_ns() - start

    print(f"Processes: {NUM_PROC}\nTotal sum: {total}\nTime taken: {elapsed} nanoseconds")
