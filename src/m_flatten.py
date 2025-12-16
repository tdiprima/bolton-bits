# flatten: Squash nested stuff into one flat list
from boltons.iterutils import flatten

nested = [[1, 2, 3], [4, 5], [6], [], [7, 8, 9]]

flat = list(flatten(nested))
print(flat)
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
