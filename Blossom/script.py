from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 


class HashMap:
  def __init__(self, size):
    self.array_size = size
    self.array = [LinkedList() for item in range(size)]

  def hash(self, key):
    hash_calc = key.encode()
    hash_code = sum(hash_calc)
    return hash_code

  def compress(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compress(self.hash(key))
    payload = Node([key, value])
    list_an_array = self.array[array_index]
    
    for item in list_an_array:
      if item[0] == key:
        item[1] = value 
    list_an_array.insert(payload)  

  def retrieve(self, key):
    array_index = self.compress(self.hash(key))
    list_at_index = self.array[array_index]

    for item in list_at_index:
      if item[0] == key:
        return item[1]
      
    return None


blossom = HashMap(len(flower_definitions))
for item in flower_definitions:
  blossom.assign(item[0], item[1])

print(blossom.retrieve('daisy'))
