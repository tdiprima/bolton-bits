"""
Clean Up a Nested List (Drop None Values)
Got a messy data structure? Remap it like a pro.
Lists are simple, but boltons adds remap for transforming 
nested structures without recursion headaches.
"""

from boltons.iterutils import remap

data = [1, None, {"key": "value", "empty": None}, [2, None, 3]]


def drop_nones(path, key, value):
    return value is not None  # Filter function


cleaned = remap(data, visit=drop_nones)
print(cleaned)  # [1, {'key': 'value'}, [2, 3]]
