# performance_comparison.py
# Benchmarks naive O(n^2) list operations vs boltons O(n) implementations.
# Compares bad vs good bucketizing and flattening to demonstrate the
# significant performance gains from using optimized boltons utilities.

import time

from boltons.iterutils import bucketize, flatten

# Prepare a large dataset
n = 200_000
data = list(range(n))
nested_data = [list(range(100)) for _ in range(n // 100)]


# --- BAD bucketizing (O(n^2)-ish) ---
def bad_bucketize(data):
    buckets = {}
    for item in data:
        key = item % 10
        if key not in buckets:
            buckets[key] = []
        # BAD: creates a new list every time
        buckets[key] = buckets[key] + [item]
    return buckets


# --- GOOD bucketizing with boltons (O(n)) ---
def good_bucketize(data):
    return bucketize(data, key=lambda x: x % 10)


# --- BAD flattening (O(n^2)-ish) ---
def bad_flatten(nested):
    result = []
    for sub in nested:
        result += sub  # BAD: creates new list each time
    return result


# --- GOOD flattening with boltons (O(n)) ---
def good_flatten(nested):
    return list(flatten(nested))


# Timing tests
start = time.time()
bad_bucketize(data)
bad_bucket_time = time.time() - start

start = time.time()
good_bucketize(data)
good_bucket_time = time.time() - start

start = time.time()
bad_flatten(nested_data)
bad_flatten_time = time.time() - start

start = time.time()
good_flatten(nested_data)
good_flatten_time = time.time() - start

print(f"Bad bucketize: {bad_bucket_time:.4f} sec")
print(f"Good bucketize: {good_bucket_time:.4f} sec")
print(f"Bad flatten: {bad_flatten_time:.4f} sec")
print(f"Good flatten: {good_flatten_time:.4f} sec")
