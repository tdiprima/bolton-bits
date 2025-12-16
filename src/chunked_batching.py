# chunked_batching.py
# Uses boltons.iterutils.chunked to split lists into fixed-size batches.
# Useful for API rate limiting, batch processing, or file uploads without
# manual slicing logic.

from boltons.iterutils import chunked

items = [1, 2, 3, 4, 5, 6, 7]
batches = chunked(items, 3)  # Split into groups of 3
print(list(batches))  # [[1, 2, 3], [4, 5, 6], [7]]
