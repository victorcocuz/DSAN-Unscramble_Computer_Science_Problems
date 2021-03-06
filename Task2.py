"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
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
from operator import itemgetter
uniqueNumbers = []
timeOnPhone = {}
for i in range(len(calls)):
    callerTime = calls[i][3]
    for j in range(2):
        callerNumber = calls[i][j]
        if callerNumber not in uniqueNumbers:
            uniqueNumbers.append(callerNumber)
            timeOnPhone[callerNumber] = int(callerTime)
        else:
            timeOnPhone[callerNumber] = timeOnPhone[callerNumber] + int(callerTime)
sortedTime = sorted(timeOnPhone.items(), key=itemgetter(1), reverse=True)
print(f"{sortedTime[0][0]} spent the longest time, {sortedTime[0][1]} seconds, on the phone during September 2016.")