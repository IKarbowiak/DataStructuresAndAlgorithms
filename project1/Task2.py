import csv
from collections import defaultdict


with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

telephone_call_times = defaultdict(int)
for call in calls:
    call_time = int(call[3])
    telephone_call_times[call[0]] += call_time
    telephone_call_times[call[1]] += call_time


telephone_number = None
longest_total_time = 0
for phone_number, total_time in telephone_call_times.items():
    if total_time > longest_total_time:
        telephone_number = phone_number
        longest_total_time = total_time

print(
    f"{telephone_number} spent the longest time, {longest_total_time} seconds, "
    "on the phone during September 2016."
)
