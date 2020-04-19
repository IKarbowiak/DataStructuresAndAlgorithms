# Explanation & time and space complexity analysis

## Explanation
To solve problem 6, I used recursion to go through element in lists.

## Time complexity
For union method, the time complexity in worst case is O(n^2), and in average case is O(n)
where n is the sum of nodes from both lists.
We need to iterate thought both of them to find the answer which is O(n) complexity,
but we also need to check if value is in visited set, the operation "in" on set takes
O(1) in average case and O(n) in worst case.

For intersection method, the time complexity is O(n^3) in worst case and O(n) in average case,
where n we be approximated to number of nodes from longer list. 
Here we also need to iterate thought both of them which is O(n) complexity, but during
second iteration we do double check: 
if element was in first list and then if was already added to linked list. Both of them
in worst case take O(n) and in average O(1), because this checks are nested the time complexity of this part
is accordingly O(n^2) or O(1).
Because this checks are called inside iteration the total time complexity is accordingly:
for the worst case O(n^3) and O(n) for average.

## Space complexity
For both method, space complexity in worst case is also O(n) where n is sum of elements
of both linked lists. We need to keep in memory elements from both lists.
 