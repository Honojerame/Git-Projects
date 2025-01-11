# Blossom HashMap

This project implements a HashMap class using a linked list to handle collisions. It also uses the HashMap to store and retrieve flower definitions.

## Project Structure

## Files

- `blossom_lib.py`: Contains the flower definitions.
- `linked_list.py`: Implements the `Node` and `LinkedList` classes.
- `script.py`: Implements the `HashMap` class and demonstrates its usage with flower definitions.

## Classes and Functions

### `linked_list.py`

- `Node`
  - `__init__(self, value)`: Initializes a node with a value.
  - `get_value(self)`: Returns the value of the node.
  - `get_next_node(self)`: Returns the next node.
  - `set_next_node(self, next_node)`: Sets the next node.

- `LinkedList`
  - `__init__(self, head_node=None)`: Initializes a linked list with an optional head node.
  - `insert(self, new_node)`: Inserts a new node at the end of the linked list.
  - `__iter__(self)`: Iterates over the linked list.

### `script.py`

- `HashMap`
  - `__init__(self, size)`: Initializes the HashMap with a given size.
  - `hash(self, key)`: Generates a hash code for a given key.
  - `compress(self, hash_code)`: Compresses the hash code to fit within the array size.
  - `assign(self, key, value)`: Assigns a key-value pair to the hash map.
  - `retrieve(self, key)`: Retrieves the value associated with a given key from the hash map.

## Usage

The script creates an instance of `HashMap` with the size of the `flower_definitions` list. It then assigns each flower definition to the hash map and retrieves the definition for 'daisy'.

```python
# Create an instance of HashMap with the size of the flower_definitions list
blossom = HashMap(len(flower_definitions))

# Assign each flower definition to the hash map
for item in flower_definitions:
    blossom.assign(item[0], item[1])

# Retrieve and print the definition for 'daisy'
print(blossom.retrieve('daisy'))

- Running the Script
To run the script, execute the following command: python Blossom/script.py

- License
This project is licensed under the MIT License.
