# bucketize: Sort items into buckets
# Say you have a bunch of numbers, and you wanna group them by "even" and "odd."
from boltons.iterutils import bucketize

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

buckets = bucketize(numbers, key=lambda x: "even" if x % 2 == 0 else "odd")

print(buckets)
# Output: {'odd': [1, 3, 5, 7, 9], 'even': [2, 4, 6, 8, 10]}
