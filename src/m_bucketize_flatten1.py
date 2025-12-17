# Flip it - bucketize first:
from boltons.iterutils import bucketize, flatten

from m_bucketize_flatten import user_messages

# Collect all messages
msgs = list(flatten(user_messages.values()))

# Bucketize by whose message it is (we can pre-annotate)
annotated = [
    (user, msg) for user, mlist in user_messages.items() for sub in mlist for msg in sub
]

buckets = bucketize(annotated, key=lambda pair: pair[0])  # bucket by user

# Now flatten messages per user:
for user, pairs in buckets.items():
    user_msgs = [msg for _, msg in pairs]
    print(f"{user}: {list(flatten(user_msgs))}")
