import ctypes  # Import ctypes to create low-level arrays

class mara_list:
    """A custom list implementation that works like Python's built-in list"""
    
    def __init__(self):
        """Initialize an empty list with default size 1"""
        self.size = 1  # Current maximum capacity of the list
        self.n = 0  # Current number of items in the list
        self.a = self.__make_array(self.size)  # Internal array storage

    def __len__(self):
        """Return the number of items in the list"""
        return self.n

    def __str__(self):
        """Return a string representation of the list like [item1, item2]"""
        if self.n == 0:
            return "[]"  # Empty list case

        # Convert all items to strings and join with commas
        result = []
        for i in range(self.n):
            result.append(str(self.a[i]))
        return "[" + ", ".join(result) + "]"

    def __resize(self, new_capacity):
        """Internal method to resize the list when it gets full"""
        # Create new bigger array
        b = self.__make_array(new_capacity)
        self.size = new_capacity

        # Copy all existing items to the new array
        for i in range(self.n):
            b[i] = self.a[i]

        # Replace old array with new bigger array
        self.a = b

    def append(self, item):
        """Add an item to the end of the list"""
        if self.n == self.size:
            # If list is full, double its size
            self.__resize(2 * self.size)

        # Add the new item at the end
        self.a[self.n] = item
        self.n += 1  # Increase item count

    def __make_array(self, capacity):
        """Create a low-level array of given capacity"""
        return (capacity * ctypes.py_object)()  # Create empty array

    def __getitem__(self, index):
        """Get an item by index (e.g., list[0])"""
        if 0 <= index < self.n:
            return self.a[index]  # Return item if index is valid
        else:
            raise IndexError("Index out of range")  # Error if index invalid

    def pop(self):
        """Remove and return the last item from the list.
        Raises an error if the list is empty."""
        if self.n == 0:
            raise IndexError("pop from empty list")  # Standard Python behavior

        # Save the last item before removing it
        popped_item = self.a[self.n-1]

        # Decrease item count (this effectively "removes" the item)
        self.n -= 1

        # Optional: Shrink the array if it's too empty
        if self.n < self.size // 4:  # If less than 25% full
            self.__resize(self.size // 2)  # Halve the size

        return popped_item  # Return the removed item

    def clear(self):
        """Remove all items from the list and reset to initial state"""
        self.n = 0
        self.size = 1
        self.a = self.__make_array(self.size)  # Reset array to initial size

    def find(self, item):
        """Return the index of the first occurrence of item, or -1 if not found"""
        for i in range(self.n):
            if self.a[i] == item:
                return i
        return -1


# DEMO: How to use the mara_list
if __name__ == "__main__":
    print("=== Testing mara_list implementation ===")
    l = mara_list()
    print(f"Initial empty list: {l}")
    print(f"Length: {len(l)}")

    print("\nAppending items...")
    items_to_add = [1, True, "hello", 3.14, 1, False]
    for item in items_to_add:
        l.append(item)
        print(f"Appended {item!r}, list: {l}")

    print("\nTesting find():")
    test_items = [1, "hello", False, "not_in_list"]
    for item in test_items:
        index = l.find(item)
        if index != -1:
            print(f"Found {item!r} at index {index}")
        else:
            print(f"{item!r} not found in list")

    print("\nTesting pop():")
    while len(l) > 0:
        print(f"Before pop: {l}, length: {len(l)}")
        popped = l.pop()
        print(f"Popped {popped!r}, after pop: {l}, length: {len(l)}")

    print("\nTesting pop() on empty list:")
    try:
        l.pop()
    except IndexError as e:
        print(f"Got expected error: {e}")

    print("\nTesting clear():")
    l.append(10)
    l.append(20)
    print(f"Before clear: {l}, length: {len(l)}")
    l.clear()
    print(f"After clear: {l}, length: {len(l)}")