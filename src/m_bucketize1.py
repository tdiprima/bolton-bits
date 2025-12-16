# You've got a list of people with ages, and you want "minors" vs "adults"
from boltons.iterutils import bucketize

people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 23},
    {"name": "Cara", "age": 15},
    {"name": "David", "age": 30},
]

buckets = bucketize(people, key=lambda p: "minor" if p["age"] < 18 else "adult")

# Output:
# {
#   'minor': [{'name': 'Alice', 'age': 17}, {'name': 'Cara', 'age': 15}],
#   'adult': [{'name': 'Bob', 'age': 23}, {'name': 'David', 'age': 30}]
# }
print(buckets)
