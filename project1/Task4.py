"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

not_telemarketers = set()
possible_telemarketers = set()

for text in texts:
    sender = text[0]
    receiver = text[1]
    if sender.startswith("140"):
        not_telemarketers.add(sender)
    if receiver.startswith("140"):
        not_telemarketers.add(receiver)

for call in calls:
    caller = call[0]
    receiver = call[1]
    if caller.startswith("140"):
        possible_telemarketers.add(caller)
    if receiver.startswith("140"):
        not_telemarketers.add(receiver)

telemarketers = possible_telemarketers - not_telemarketers

print("These numbers could be telemarketers: ")
for telemarketer in sorted(telemarketers):
    print(telemarketer)
