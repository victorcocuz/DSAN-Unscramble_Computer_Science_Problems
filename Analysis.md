## Run Time Analysis:

### Note
- The orders below are approximations based on lines of code. This exercise does not attempt to calculate number of operation based on instructions generated from each line of code.
- Orders are calculated considering worst case scenarios.

### Task0
- Breakdown: This algorithm is constant, because there is no relationship between the input and the number of instructions executed
- Order: O(1)

### Task1
- Breakdown: This algorithm loops through all entries and executes 4 lines of code on each cycle. This could be O(5n), but constants can be dropped, because they are negligible over large input sizes
- Order: O(n)

### Task2
- Breakdown (constants and non-dominant terms will be dropped from the order):
O(5) - Single statements  
O(8n) - Loop through all entries and execute 8 lines of code on each cycle.  
O(nlog(n)) - Sort method for phone numbers  
- Order: O(nlog(n))

### Task3
- Breakdown (constants and non-dominant terms will be dropped from the order):
O(6) - Single statements  
O(7n) - Loop through all entries and execute 7 lines of code on each cycle
O(nlog(n)) - Sort method for areas
- Order: O(nlog(n))

### Task4
- Breakdown (constants and non-dominant terms will be dropped from the order):
O(4) - Single statements  
O(8n) - 3 Loops through all entries which execute a total 7 lines of code on each cycle
O(nlog(n)) - Sort method for possible telemarketers
- Order: O(nlog(n))