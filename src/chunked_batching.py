"""
Chunk a List into Batches
Processing in batches? chunked is your friend.
API rate limits or file processing? Batch uploads/downloads
without manual slicing.
"""

from boltons.iterutils import chunked

items = [1, 2, 3, 4, 5, 6, 7]
batches = chunked(items, 3)  # Split into groups of 3
print(list(batches))  # [[1, 2, 3], [4, 5, 6], [7]]
