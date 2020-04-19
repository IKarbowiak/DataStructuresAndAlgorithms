# Explanation & time and space complexity analysis

## Explanation
I decided to use dict as a cache, because it is the best data structure for mapping
key to values and it has O(1) time complexity in average case.

## Time complexity
To ensure that all operations has O(1) complexity I decided to use double linked list
to keep the order of the last recently used elements. It couldn't be single linked-list
because in this case removing element in worst case take O(n).

## Space complexity
Space complexity is O(n) where n is number of elements in cache. We need to keep data
about all elements.
