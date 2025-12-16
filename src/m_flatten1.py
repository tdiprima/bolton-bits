# You have messages from different days, like:
from boltons.iterutils import flatten

daily_messages = [
    ["Hi!", "Don't forget the meeting."],
    ["Lunch at 1?", "Sure!"],
    ["Reminder: Submit report."],
]

all_messages = list(flatten(daily_messages))
print(all_messages)
# Output: ["Hi!", "Don't forget the meeting.", "Lunch at 1?", "Sure!", "Reminder: Submit report."]
