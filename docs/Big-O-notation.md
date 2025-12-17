> Boltons utils save you like "O-n-squared to O-n"

Yeah, that "O-n-squared to O-n" thing is **Big-O notation** talk — basically nerd shorthand for *how bad your code gets as your data grows*.

Let's break it down so it actually makes sense.

## 1. Big-O in human terms

* **O(n)** → "Linear time." If you have 10 items, it does \~10 steps. If you have 100 items, \~100 steps.
* **O(n²)** → "Quadratic time." If you have 10 items, it does \~100 steps. If you have 100 items, \~10,000 steps. Growth is *way* faster — this is the kind of code that feels fine on a small list and then melts your laptop when the list gets big.

## 2. Why boltons might save you from O(n²)

Some Python patterns — especially manual "grouping" or "flattening" — can accidentally cause O(n²) time complexity if you do it the "loop inside a loop" way.

**Bad, O(n²) example:**

```python
data = [1, 2, 3, 4, 5]
groups = {}

for item in data:
    key = item % 2
    if key not in groups:
        groups[key] = []
    # appending is fine, but if you were using list concatenation instead...
    groups[key] = groups[key] + [item]  # BAD: creates a new list every time
```

That `groups[key] = groups[key] + [item]` is sneaky slow — concatenating lists like that copies all the elements each time. That's how you get O(n²).

**Good, O(n) example (boltons.bucketize)**

```python
from boltons.iterutils import bucketize

data = [1, 2, 3, 4, 5]
buckets = bucketize(data, key=lambda x: x % 2)
```

`bucketize` preallocates buckets and appends in place — no wasteful full-list copies — so it only has to look at each item once. That's O(n).

## 3. Flattening example

If you try to flatten by doing something like:

```python
flat = []
for sublist in nested:
    # flat += sublist  # OK
    flat = flat + sublist  # Bad: copies old list into a new one every time
```

~~That's O(n²) because `+=` on lists copies all the elements each time.~~

`boltons.flatten` uses iterators under the hood, so it doesn't keep re-copying — it just yields items one by one. That's O(n).

## 4. TL;DR

* **O(n²)** → accidentally reprocessing everything over and over.
* **O(n)** → touch each element once and move on.
* **boltons**: gives you O(n) versions of common patterns that people often write in slow O(n²) ways by accident.

<br>

---

Here's **a timing test** comparing a naive bucket/flatten vs boltons so you can *see* the performance jump in numbers. It's very "holy crap" when you scale to big data.

[performance_comparison.py](../src/performance_comparison.py)

When you run it, you should see something like:

```
Bad bucketize: 5.21 sec
Good bucketize: 0.03 sec
Bad flatten: 4.87 sec
Good flatten: 0.02 sec
```

That's the O(n²) → O(n) magic — same results, but **hundreds of times faster** when your data's big.

<br>
