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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
# from operator import itemgetter, attrgetter

uniqueNumbers = []
for i in range(len(calls)):
    for j in range(2):
        number = calls[i][j]
        if number not in uniqueNumbers:
            uniqueNumbers.append(number)
print(f"There are {len(uniqueNumbers)} different telephone numbers in the records.")
