def process_all_at_once(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()

    total = 0
    for line in lines:
        total += len(line)
    return total

def process_as_generator(filepath):
    def line_generator():
        with open(filepath, 'r') as f:
            for line in f:
                yield line
    
    total = 0
    for line in line_generator():
        total += len(line)
    return total

import tracemalloc

tracemalloc.start()
result1 = process_all_at_once("orders_large.csv")
peak1 = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

tracemalloc.start()
result2 = process_as_generator("orders_large.csv")
peak2 = tracemalloc.get_traced_memory()[1]
tracemalloc.stop()

print(f"Both produced the same result: {result1 == result2}")
print(f"Load-all-at-once peak memory: {peak1 / 1024:.1f} KB")
print(f"Generator peak memory:        {peak2 / 1024:.1f} KB")
print(f"Generator used {round(peak1 / peak2, 1)}x less memory")