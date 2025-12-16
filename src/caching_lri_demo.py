# caching_lri_demo.py
# Demonstrates boltons.cacheutils for memoization with LRI (Least Recently
# Inserted) eviction policy. Caches expensive function calls with configurable
# limits and thread-safe operation.

from boltons.cacheutils import LRI, cached  # LRI = Least Recently Inserted


@cached(LRI(3))  # Cache up to 3 items, evict least recently inserted
def expensive_calc(x):
    print(f"Calculating for {x}...")  # This prints only on cache miss
    return x * x


print(expensive_calc(2))  # Calculating for 2... \n 4
print(expensive_calc(2))  # 4 (cached, no print)
print(expensive_calc(3))  # Calculating for 3... \n 9
