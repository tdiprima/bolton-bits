# remap_drop_nones.py
# Uses boltons.iterutils.remap to recursively clean nested data structures
# by removing None values from lists, dicts, and tuples without writing
# custom recursive walkers.

from boltons.iterutils import remap

data = [1, None, {"key": "value", "empty": None}, [2, None, 3]]


def drop_nones(path, key, value):
    return value is not None  # Filter function


cleaned = remap(data, visit=drop_nones)
print(cleaned)  # [1, {'key': 'value'}, [2, 3]]
