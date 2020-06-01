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
incomingNumbers = [calls[i][1] for i in range(len(calls))]

textNumbers = []
for i in range(len(texts)):
    for j in range(2):
        if(texts[i][j]) not in textNumbers:
            textNumbers.append(texts[i][j])

possibleTelemarketers = []
for i in range(len(calls)):
    callerNumber = calls[i][0]
    if (callerNumber not in possibleTelemarketers and 
      callerNumber not in incomingNumbers and
      callerNumber not in textNumbers):
        possibleTelemarketers.append(callerNumber)

possibleTelemarketers.sort()

nl = '\n'
print(f'These numbers could be telemarketers: {nl}{nl.join(possibleTelemarketers)}')



