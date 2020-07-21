
class Node(object):

  def __init__(self, key, value, previous=None, next_node=None):
      self.value = value 
      self.previous = previous 
      self.next_node = next_node
      self.key = key


  def __repr__(self):
      return f"current: { str(self.value)}"
    
    
# Solution 1: Using a doubly linked list.
class LRUCache3:

  def __init__(self, capacity):
    self.capacity = capacity
    self.cache = {}
    self.tail = None
    self.head = None

  def put(self, key, value):
    """
      if there is an empty space (capacity is not full),
      add element to the cache and also add it to the doubly linked list.
      every time a new item is added the head changes to point to it. 

      if the cache was full -> 
      evict element that is at the tail. and add the new element to the head of the doubly linked list and also the cache. 
    """
    node = Node(key, value)

    if len(self.cache) < self.capacity:
      # The addition section to handle adding to the doubly linked list. 
      if not self.head:
        self.head = node
        self.tail = node
      else: 
        previous_head = self.head 
        
        node.previous = previous_head
        previous_head.next_node = node
        
        self.head = node
          
      self.cache[key] = node
    else:
      # evict the tail and delete value from cache
      previous_tail = self.tail 
      self.tail = previous_tail.next_node
      
      del self.cache[previous_tail.key]
      
      # add new element to teh cache and update the head.
      previous_head = self.head 
        
      node.previous = previous_head
      previous_head.next_node = node
      self.head = node

      self.cache[key] = node

  def get(self, key):
    """
      if element does not exist return -1. 
      if element is inside the cache, update the doubly linked list to have the element be at the head. 
    """
    
    if not self.cache.get(key):
      return -1 
    
    node = self.cache[key]

    previous_head = self.head 
    
    if node == self.tail:
      self.tail = self.tail.next_node

    node.previous = previous_head
    node.next_node = None
    previous_head.next_node = node
    
    self.head = node

    return node.value

  def print_values(self):
    pointer_node = self.tail  
    
    count = 0 
    while (pointer_node):  
      print(pointer_node)      

      count += 1 
      if count == 4:
        break
      pointer_node = pointer_node.next_node
    
    print('end of printing')

# Solution 2 Using an ordered Dictionary, all methods used from the ordered dictionary are o(1),
from collections import OrderedDict

class LRUCache2:

  def __init__(self, capacity):
      self.capacity = capacity
      self.cache = OrderedDict()
  
  def put(self, key, value):
      # ordered dictionary can have the same key twice, therefore we delete.
      if key in self.cache:
          del self.cache[key]

      if len(self.cache.keys()) < self.capacity:
          self.cache[key] = value
      else: ## handle eviction
          self.cache.popitem(last=False) # o(1)
          self.cache[key] = value

  def get(self, key):
      value = self.cache.get(key, None)

      if not value:
          return -1

      self.cache.move_to_end(key)

      return value

lru = LRUCache3(3)
lru.put(1, 101)
lru.put(2, 102)
lru.put(3, 103)
lru.print_values()

lru.put(4, 104)
lru.print_values()

assert lru.get(1) == -1

lru.print_values()

assert lru.get(2) == 102
lru.print_values()


assert lru.get(3) == 103


assert lru.get(1) == -1
lru.print_values()

assert lru.tail.value == 104
assert lru.head.value == 103
# 
lru.put(4, 104)
lru.print_values()

assert len(lru.cache) == 3
assert lru.get(4) == 104

# # This tests that the oldest used value is being dropped
assert lru.get(1) == -1


# # This tests that when you write a new value you are putting it back to the top of the cache
lru.put(2, 112)
lru.put(5, 105)
assert lru.get(2) == 112
assert lru.get(4) == 104
assert lru.get(5) == 105

print("Success 123")
