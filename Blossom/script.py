from linked_list import Node, LinkedList
from blossom_lib import flower_definitions 

"""
This script implements a HashMap class using a linked list to handle collisions.
It also uses the HashMap to store and retrieve flower definitions.
Classes:
    HashMap: A class that implements a hash map with separate chaining for collision resolution.
Functions:
    __init__(self, size): Initializes the HashMap with a given size.
    hash(self, key): Generates a hash code for a given key.
    compress(self, hash_code): Compresses the hash code to fit within the array size.
    assign(self, key, value): Assigns a key-value pair to the hash map.
    retrieve(self, key): Retrieves the value associated with a given key from the hash map.
Usage:
    The script creates an instance of HashMap with the size of the flower_definitions list.
    It then assigns each flower definition to the hash map and retrieves the definition for 'daisy'.
"""

class HashMap:
    def __init__(self, size):
        # Initialize the hash map with a given size
        self.array_size = size
        self.array = [LinkedList() for item in range(size)]

    def hash(self, key):
        # Generate a hash code for a given key
        hash_calc = key.encode()
        hash_code = sum(hash_calc)
        return hash_code

    def compress(self, hash_code):
        # Compress the hash code to fit within the array size
        return hash_code % self.array_size

    def assign(self, key, value):
        # Assign a key-value pair to the hash map
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_an_array = self.array[array_index]
        
        # Check if the key already exists in the linked list
        for item in list_an_array:
            if item[0] == key:
                item[1] = value  # Update the value if key is found
        list_an_array.insert(payload)  # Insert the new key-value pair

    def retrieve(self, key):
        # Retrieve the value associated with a given key from the hash map
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]

        # Search for the key in the linked list
        for item in list_at_index:
            if item[0] == key:
                return item[1]  # Return the value if key is found
            
        return None  # Return None if key is not found

# Create an instance of HashMap with the size of the flower_definitions list
blossom = HashMap(len(flower_definitions))

# Assign each flower definition to the hash map
for item in flower_definitions:
    blossom.assign(item[0], item[1])

# Retrieve and print the definition for 'daisy'
print(blossom.retrieve('daisy'))
