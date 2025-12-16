# iterutils_demo.py
# Demonstrates boltons.iterutils bucketize and flatten functions for grouping
# and flattening data structures. Shows even/odd grouping, age-based bucketing,
# nested list flattening, and combining both techniques.

from boltons.iterutils import bucketize, flatten

# 1. bucketize: even / odd
numbers = list(range(1, 11))
buckets_numbers = bucketize(numbers, key=lambda x: "even" if x % 2 == 0 else "odd")
print("Even/Odd buckets:", buckets_numbers)

# 2. bucketize: minors / adults
people = [
    {"name": "Alice", "age": 17},
    {"name": "Bob", "age": 23},
    {"name": "Cara", "age": 15},
    {"name": "David", "age": 30},
]
buckets_people = bucketize(people, key=lambda p: "minor" if p["age"] < 18 else "adult")
print("Minors / Adults buckets:", buckets_people)

# 3. flatten a nested list
nested = [[1, 2, 3], [4, 5], [6], [], [7, 8, 9]]
flat_numbers = list(flatten(nested))
print("Flattened numbers:", flat_numbers)

daily_messages = [
    ["Hi!", "Don't forget the meeting."],
    ["Lunch at 1?", "Sure!"],
    ["Reminder: Submit report."],
]
flat_messages = list(flatten(daily_messages))
print("All messages:", flat_messages)

# 4. combine flatten + bucketize
user_messages = {
    "Alice": [["Hi"], ["How are you?", "Let's meet"]],
    "Bob": [["Yo!"], ["Got it", "Thanks"], []],
    "Cara": [["Hey"]],
}

# a) Flatten all messages
all_msgs = list(flatten(user_messages.values()))
print("Flatten all user messages:", all_msgs)

# b) Bucketize these messages by length: short vs long
buckets_msg_length = bucketize(
    all_msgs, key=lambda m: "short" if len(m) < 5 else "long"
)
print("Messages by length:", buckets_msg_length)

# c) Bucketize per user, then flatten per user
annotated = [(u, msg) for u, mls in user_messages.items() for sub in mls for msg in sub]
buckets_by_user = bucketize(annotated, key=lambda pair: pair[0])
print("Buckets by user:", buckets_by_user)

print("Flattened per user:")
for user, pairs in buckets_by_user.items():
    user_msgs = [msg for _, msg in pairs]
    print(f"  {user}: {list(flatten(user_msgs))}")
