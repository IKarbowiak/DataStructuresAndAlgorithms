# Explanation & time and space complexity analysis

## Explanation
To find two numbers which sum is maximum I decided to first sort list with use
of merge sort algorithm and then create numbers.

## Time complexity
In my solution I first sort items with use of merge sort, which time complexity is O(nlogn), 
and space complexity is O(n). After sort I also iterate through every element in list
to create numbers, so here time complexity is O(n). As a result time complexity
of the solution is O(n) + O(nlogn) which approximates to O(nlogn), where n is numbers
of elements in list.

## Space complexity
Space complexity is O(n), because we need to keep call stack during merge sort.
