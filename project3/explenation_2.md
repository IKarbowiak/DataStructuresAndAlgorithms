# Explanation & time and space complexity analysis

## Explanation
I used modified binary search to find the answer. Modified, because in this case
values in list are not properly sorted, array is rotated in some point. Because
of that more checks are needed, when changing start and end index.

## Time complexity
Time complexity of my solution in worst case is O(logn), where n is number of elements in input list.
In every iteration I reduced in half number of elements to check.

## Space complexity
Space complexity is O(n), input data with n element is kept. 
