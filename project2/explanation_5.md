# Explanation & time and space complexity analysis

## Explanation
To create BlockChain I create double linked list where reference to head and tail element is kept. 
To Block class I added next attribute to keep data about next and previous block in chain. 

## Time complexity
Time complexity of append in is O(1), because element just need to be added to the tail.
Space complexity for append is O(1), we don't have keep any additional data
which depends on input size.

The same situation is in pop method. Time complexity is O(1), because we just need to take
element from tail and set previous element as a tail.

## Space complexity
For searched method it doesn't change, still in worst case we need to go through all
block in block chain, so time complexity will be O(n) in worst case,
where n is number of blocks.

Space complexity of block chain is O(n) where n is number of elements added to block chain. 
We need to keep data about all elements.
What about methods their space complexity is O(1), we don't have keep any additional data
which depends on input size, we operate on created block chain.
