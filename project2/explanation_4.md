# Explanation & time and space complexity analysis

## Explanation
To check if user is in group I decided to use recursion, because to check if user is in
given group we also need to check all groups below given. Users which is in child group
also belong to parent group.

## Time complexity
The time complexity in worst case is O(n * u) where n is number of groups and subgroups
of given group and u is number of users in those groups.

## Space complexity
In the solution we don't keep any data instead of stack call, in the worst case we will
find user in the deepest group, so we need to iterate through all groups and subgroups
and so on. So the space complexity in the worst case will be O(n) where n is the number
of groups and subgroups.
