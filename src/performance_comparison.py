"""
Benchmarks naive O(n^2) list operations vs boltons O(n) implementations.
Compares bad vs good bucketizing and flattening to demonstrate the
significant performance gains from using optimized boltons utilities.
"""

import time

from boltons.iterutils import bucketize, flatten

# Prepare a large dataset
n = 200_000
# Creates a list of integers from 0 up to n - 1
data = list(range(n))
# Builds a list containing n // 100 sublists, where each sublist is the numbers 0 through 99
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


# --- Not bad flattening 0.0013 sec ---
# def bad_flatten(nested):
#     result = []
#     for sub in nested:
#         result += sub  # list.extend() is actually O(n)
#     return result


# --- BAD flattening (O(n^2)) ---
def bad_flatten(nested):
    result = []
    for sub in nested:
        result = result + sub  # Creates new list each time - truly O(n²)
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

# Bad bucketize: 8.4471 sec
# Good bucketize: 0.0205 sec
# Bad flatten: 0.2959 sec
# Good flatten: 0.0478 sec
# (Times will vary based on machine performance)
