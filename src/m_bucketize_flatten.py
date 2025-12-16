# Combine them: bucketize + flatten
from boltons.iterutils import bucketize, flatten

# You've got messages categorized by user preference:
user_messages = {
    'Alice': [["Hi"], ["How are you?", "Let's meet"]],
    'Bob': [["Yo!"], ["Got it", "Thanks"], []],
    'Cara': [["Hey"]]
}

if __name__ == "__main__":
    # Want: All messages flattened across all users.

    flatten_all = list(flatten(user_messages.values()))
    print(flatten_all)
    # Output: ["Hi", "How are you?", "Let's meet", "Yo!", "Got it", "Thanks", "Hey"]

    # Now—use bucketize afterward if you want to regroup differently. Example:

    # Flatten as above
    msgs = list(flatten(user_messages.values()))

    # Then bucketize by message length: short vs long
    buckets = bucketize(
        msgs,
        key=lambda m: 'short' if len(m) < 5 else 'long'
    )

    print(buckets)
    # Could produce something like:
    # {
    #   'short': ['Hi', 'Yo!', 'Hey'],
    #   'long': ["How are you?", "Let's meet", "Got it", "Thanks"]
    # }
