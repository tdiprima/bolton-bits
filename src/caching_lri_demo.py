"""
Cache Expensive Function Calls
Slow API or computation? Cache it!
Python has functools.lru_cache, but boltons' cacheutils adds 
flexible, thread-safe caching with extras like thresholds.
"""

from boltons.cacheutils import LRI, cached  # LRI = Least Recently Inserted


@cached(LRI(3))  # Cache up to 3 items, evict least recently inserted
def expensive_calc(x):
    print(f"Calculating for {x}...")  # This prints only on cache miss
    return x * x


print(expensive_calc(2))  # Calculating for 2... \n 4
print(expensive_calc(2))  # 4 (cached, no print)
print(expensive_calc(3))  # Calculating for 3... \n 9
