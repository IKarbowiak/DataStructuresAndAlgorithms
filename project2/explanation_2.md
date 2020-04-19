# Explanation & time and space complexity analysis

## Explanation
To solve problem 2, I decided to use recursion because it is easy way to go inside the tree.

## Time complexity
Time complexity of my solution is O(n) where n is the total number of files/directories
in the given path. We need to check every file and directory to decided if file path
follow the pattern.

## Space complexity
Space complexity of the solution is O(n*m) where n is number of directories 
and m is number of files. We need to keep stack about directories, until we get the all
files matching the suffix.
