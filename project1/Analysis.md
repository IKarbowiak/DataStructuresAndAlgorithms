# Time complexity worst Case Big-O Notation

## Task 0
**Answer:**
O(1)

**Explanation:**
There is only get item operation and no other operations.

## Task 1
**Answer:**
O(n), where n is length of the longer file.

**Explanation:**
There are two for loop iterating over files, so in worst scenario n will be length of longer file.
There are two loops so it should be 2n, but 2 is insignificant so the answer is O(n).

## Task 2
**Answer:**
O(n), where n is length of the call file.

**Explanation:**
Here is similar situation as before. We also have two iterations. In first iteration
it will be just n iteration, but in second for loop it could be 2n iteration, because
every call row could give us two new phone numbers. It sums up to 2n + n which gives 3n.
In approximation, it also turns out ot be O(n).

## Task3
**Answer:**
O(nlogn), where n is length of call file.

**Explanation:**
Here we have two loops but also sorted method. Loops has O(n) complexity because every
row in calls file can generate additional phone code. Sorted method has complexity O(nlogn).
Because O(nlogn) has much more impact we can approximate this to O(nlogn).

## Task4
**Answer:**
O(nlogn), where n is length of longer file.

**Explanation:**
Here is similar situation as in task 3. There are two for loops and sorted method.
So, because bottleneck is method which takes longer time, the answer is O(nlogn).
