# Explanation & time and space complexity analysis

## Explanation
I used binary search to find the answer. Every time I choose middle element, calculate the square
and compare if result is equal, bigger or less than target. Then I repeat the process
for bigger or less half.

## Time complexity
Time complexity of my solution in worse case is O(logn) where n is number. In every iteration
middle element is chosen and then there is check if target is equal, less or bigger than square of chosen number.
Then the process is repeated for one of the half, bigger or less. If the result is equal 
to the target we get the result.

## Space complexity
Space complexity is O(1), we keep only start, end and previous values. Space complexity
is constant, nothing is accumulated.
