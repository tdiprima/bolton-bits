## Pronunciation

Here's how people usually *say* these out loud, plus how they show up in sentences:

### `O(n²)`

**Said as:**

* "big O of n squared"
* "order n squared"
* "quadratic time" (very common)

**In a sentence:**

This algorithm runs in **O(n²)** time, so it gets slow fast as the input size grows.

### `O(n)`

**Said as:**

* "big O of n"
* "order n"
* "linear time" (also very common)

**In a sentence:**

The lookup is **O(n)**, meaning the runtime increases linearly with the number of elements.

Quick vibe check:

* **O(n)** = scales chill 😌
* **O(n²)** = scales kinda yikes 🚨

<br>

---

## Real-world examples

Here are **real-world, non-CS-brain examples** that actually stick:

## **O(n) — linear time**

You do one thing per item. No extra chaos.

**Examples:**

* 📋 **Reading a list of names**  
  You read each name once. Double the list → double the time.

* 🧦 **Matching socks one by one**  
  You pick up each sock and check it. Every sock gets one glance.

* 🔍 **Finding a name in an unsorted contact list**  
  Worst case, the name is last, so you check everyone.

**Sentence:**

Looking through the guest list is **O(n)** because you check each name once.

## **O(n²) — quadratic time**

Every item interacts with every other item. This is where pain begins.

**Examples:**

* 🤝 **Everyone shaking hands with everyone else**  
  10 people → 45 handshakes. Add more people and it explodes.

* 🧦 **Matching every sock with every other sock**  
  You compare sock A with all others, then sock B with all others... oof.

* 👀 **Comparing everyone's schedule with everyone else's**  
  Every person checks conflicts with every other person.

**Sentence:**

The meeting scheduling turned **O(n²)** because everyone had to check availability with everyone else.

### TL;DR

* **O(n)** = "for each thing, do a thing"
* **O(n²)** = "for each thing, do a thing for every other thing"

<br>

---

## How to spot these in code instantly

Here's the **instant pattern-recognition cheat code** 👀

## 🟢 How to spot **O(n)** at a glance

**Rule of thumb:** *One loop over the data.*

### What it looks like

```python
for x in items:
    do_something(x)
```

### Also O(n):

* One `for` / `while` loop
* Recursion that processes **one element per call**
* Loop + constant work inside

### Dead giveaway thoughts:

* "I touch each item once"
* "No looping inside looping"
* "Runtime grows evenly with input size"

## 🔴 How to spot **O(n²)** instantly

**Rule of thumb:** *Loop inside a loop over the same data.*

### What it looks like

```python
for i in range(n):
    for j in range(n):
        do_something(i, j)
```

### Also O(n²):

* Nested loops over the **same list**
* Comparing every item with every other item
* "For each X, check all Y"

### Dead giveaway thoughts:

* "For each element... for each element..."
* "Pairwise comparison"
* "This is gonna cook my CPU"

## ⚡️ Fast mental shortcuts

* **One loop** → probably **O(n)**
* **Two nested loops** → probably **O(n²)**
* **Loop inside a recursive call** → 🚨 re-check carefully
* **Break early sometimes?** Worst case still counts → still **O(n²)**

## 🧠 Common traps (don't get fooled)

### ❌ This is STILL O(n²)

```python
for i in range(n):
    for j in range(i):
        do_something()
```

It *feels* smaller, but it's still quadratic.

**Quadratic** means the runtime grows proportional to n² (n squared).

So if:

* `n = 10` → ~100 operations
* `n = 100` → ~10,000 operations
* `n = 1,000` → ~1,000,000 operations 😬

That curve goes up fast.

Quadratic means the work grows with the square of the input size — double the input, about four times the work.

### ❌ This is NOT O(n²)

```python
for i in range(n):
    print("hello")
for j in range(n):
    print("world")
```

That's **O(n + n) = O(n)**. Loops aren't nested.

## 🧪 Real interview-level tell

If you hear yourself say:

"Well, in the worst case..."

Stop. Count loops. That's the answer.

### Ultra TL;DR

* **One loop** → O(n)
* **Loop inside loop** → O(n²)
* **Worst case always wins**

<br>
