class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache_data = {}
        self.head = None
        self.tail = None

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent.
        if key in self.cache_data:
            item = self.cache_data[key]
            self.increase_usage(item)
            return item.value
        return -1

    def set(self, key, value):
        # Set the value if the key is not present in the cache.
        # If the cache is at capacity remove the oldest item.
        if self.capacity == 0:
            return
        if key in self.cache_data:
            item = self.cache_data["key"]
            item.value = value
            self.increase_usage(item)
        else:
            if len(self.cache_data) == self.capacity:
                self.remove_node()
            item = Node(key, value)
            self.cache_data[key] = item
            self.add_to_head(item)

    def increase_usage(self, node):
        if node.prev is None:
            self.head = node.next
        else:
            node.prev.next = node.next

        if node.next is None:
            self.tail = node.prev
        else:
            node.next.prev = node.prev

        self.add_to_head(node)

    def remove_node(self):
        key = self.tail.key
        del self.cache_data[key]
        if self.tail.prev:
            self.tail.prev.next = None

    def add_to_head(self, node):
        node.next = self.head
        node.prev = None
        if self.head:
            self.head.prev = node
        self.head = node
        if not self.tail:
            self.tail = node


# Test case 1
our_cache = LRU_Cache(5)

our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)


print(our_cache.get(1))
# should returns 1

print(our_cache.get(2))
# should returns 2

print(our_cache.get(9))
# should returns -1 because 9 is not present in the cache

our_cache.set(5, 5)
our_cache.set(6, 6)

print(our_cache.get(3))
# should returns -1 because the cache reached it's capacity and 3 was the least recently used entry


# Test case 3
our_cache = LRU_Cache(0)

our_cache.set(1, 1)

print(our_cache.get(1))
# should returns -1, nothing can't be set to cache with capacity equal 0

our_cache.set(2, 2)

print(our_cache.get(3))
# should returns -1


# Test case 3
our_cache = LRU_Cache(1)

our_cache.set(1, 1)

print(our_cache.get(1))
# should returns 1

our_cache.set(2, 2)

print(our_cache.get(1))
# should returns -1 - only one element can be kept in cache so 1 was removed

print(our_cache.get(2))
# should returns 2
