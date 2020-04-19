import copy


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size


def union(llist_1, llist_2):
    # Your Solution Here
    visited = set()
    union_llist = LinkedList()

    def union_f(node):
        if node:
            if node.value not in visited:
                union_llist.append(node.value)
                visited.add(node.value)
            node = node.next
            union_f(node)

    for l in llist_1, llist_2:
        union_f(l.head)

    return union_llist


def intersection(llist_1, llist_2):
    # Your Solution Here
    values_from_llist_1 = set()
    visited = set()

    intersection_llist = LinkedList()

    def intersection_f(node, check):
        if node:
            if check and node.value in values_from_llist_1:
                if node.value not in visited:
                    intersection_llist.append(node.value)
                    visited.add(node.value)
            elif not check:
                values_from_llist_1.add(node.value)
            node = node.next
            intersection_f(node, check)

    intersection_f(llist_1.head, False)
    intersection_f(llist_2.head, True)

    return intersection_llist


# Test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 21]
element_2 = [6, 32, 4, 9, 6, 1, 11, 21, 1]

for i in element_1:
    linked_list_1.append(i)

for i in element_2:
    linked_list_2.append(i)


print(union(linked_list_1, linked_list_2))
# should return 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 21 -> 32 -> 9 -> 1 -> 11 -> 

print(intersection(linked_list_1, linked_list_2))
# should return 6 -> 4 -> 21 -> 


# Test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3, 2, 4, 35, 6, 65, 6, 4, 3, 23]
element_2 = [1, 7, 8, 9, 11, 21, 1]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

print(union(linked_list_3, linked_list_4))
# should return  3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 

print(intersection(linked_list_3, linked_list_4))
# should return nothing - linked_list_3 and linked_list_4 do not have common part


linked_list_5 = LinkedList()
linked_list_6 = LinkedList()

print(union(linked_list_5, linked_list_6))
# should return nothing - both lists are empty

print(intersection(linked_list_5, linked_list_6))
# should return nothing - both lists are empty


linked_list_7 = LinkedList()
linked_list_8 = LinkedList()

element_7 = [1, 7, 8, 9, 11, 21, 1]

for i in element_7:
    linked_list_7.append(i)


print(union(linked_list_7, linked_list_8))
# 1 -> 7 -> 8 -> 9 -> 11 -> 21 ->  - all elements from linked_list_7

print(intersection(linked_list_7, linked_list_8))
# should return nothing - second list is empty