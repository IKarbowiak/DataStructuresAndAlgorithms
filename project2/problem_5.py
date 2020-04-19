import datetime
import hashlib


class Block:

    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash(data)
        self.next = None
        self.previous = None

    def calc_hash(self, data):
        sha = hashlib.sha256()

        hash_str = str(self.timestamp).encode('utf-8') + data.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()


class BlockChain:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def append(self, data):
        """ Append a value to the end of the list. """
        timestamp = datetime.datetime.now()
        if not self.head:
            self.head = Block(timestamp, data, None)
            self.tail = self.head
            self.num_elements += 1
            return

        last = self.tail
        self.tail = Block(timestamp, data, last.hash)
        self.tail.previous = last
        last.next = self.tail
        self.num_elements += 1

    def search_by_hash(self, hash):
        block = self.head
        while block:
            if block.hash == hash:
                return block
            block = block.next
        return None

    def search_by_data(self, data):
        """ Search the block chain for a node with the requested data and return the block. """
        block = self.head
        while block:
            if block.data == data:
                return block
            block = block.next
        return None

    def size(self):
        """ Return the size or length of the block chain. """
        return self.num_elements

    def pop(self):
        """ Return the last chain block and remove it from the list. """
        if not self.tail:
            return None

        block = self.tail
        if not block.previous_hash:
            self.tail = None
            self.head = None
            self.num_elements -= 1
            return block

        self.tail = block.previous
        self.num_elements -= 1
        return block


# Test case 1

block_chain = BlockChain()

block_chain.append("Some data")
block_chain.append("Another data")
block_chain.append("Extra data")

print(block_chain.size())
# block chain size should be 3

print(
    block_chain.search_by_data("Another data").timestamp
    < block_chain.search_by_data("Extra data").timestamp
)
# should return True, because Another data was created before Extra data

print(block_chain.search_by_data("data"))
# result should be None because block chain does not contain block with this data

print(block_chain.pop().data)
# return data should be "Extra data"

print(block_chain.size())
# block chain size should be 2

print(block_chain.pop().data)
# return data should be "Another data"

print(block_chain.pop().data)
# return data should be "Some data"

print(block_chain.size())
# block chain size should be 0

print(block_chain.pop())
# return data should be None


# Test case 2
block_chain = BlockChain()

print(block_chain.pop())
# result should be None - block is empty

print(block_chain.size())
# block chain size should be 0

block_chain.append("")
block_chain.append("")

print(block_chain.size())
# should return 2


# Test case 3
block_chain = BlockChain()

block_chain.append("data 1")
block_chain.append("data 2")

data_1 = block_chain.search_by_data("data 2")
print(data_1.data)
# should return "data 2"

print(block_chain.search_by_hash(data_1.previous_hash).data)
# should return "data 1"

block_chain.append("data 3")

print(
    block_chain.search_by_data("data 1").timestamp
    < block_chain.search_by_data("data 3").timestamp
)
# should return True, because "data 1" was created before "data 2"

block_chain.pop().previous_hash
block_chain.pop().previous_hash

print(block_chain.pop().previous_hash)
# should return None

print(block_chain.size())
# should return 1

block_chain.append("data 4")
block_chain.append("data 4")

print(block_chain.pop().hash != block_chain.pop().hash)
# True - hashes should be different
