# Explanation & time and space complexity analysis

## Explanation
In problem 3 I decided to use Node class to keep information about char or sum of frequencies
from children nodes. I used it to create Huffman Tree.
To count frequencies of charts I used dict which is the best data structure to keep 
key - value mapping, which in this case are char - frequencies pairs.

## Time and space complexity analysis

### Encode:
The time complexity of encode is O(nlogn), where n is number of chars in string.
This is cause be sorted operation in "get_characters_frequencies".
It is needed because to create Huffman Tree we need sorted data.
Sorting is the most time consuming operation in encode solution. Others operations are
iterations which takes O(n).

The space complexity is in average O(n) where n is number of chars in string.
We need to create dict key-value pair, at the worst case for every char and then
node for every char from string (at the worst case).
We also use stack call in "create_huffman_tree", but it still in the worst case
will be n in deep.

### Decode:
In case of decoding time complexity is O(n) where n is length of decoded data.
In the solution we iterate thought every element from decoded data and based on the value,
going left or right on tree. There is no more iteration.

The space complexity we can approximate to O(n) where n is number of chars in decoded data.
We iterate through decoded data, and generate output string. In worst case, every
encoded data char gives as new char to output string.
