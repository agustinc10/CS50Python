class Jar:
    def __init__(self, capacity=12):
        if int(capacity) < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = int(capacity)
        self._size = 0

    def __str__(self):
        return f"{'🍪' * self.size}"

    def deposit(self, n):
        if self.size + n > self.capacity:
            raise ValueError("Exceed Capacity")
        self.size += n

    def withdraw(self, n):
        if self.size - n < 0:
            raise ValueError("Exceed Capacity")
        self.size -= n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        if int(capacity) < 0:
            raise ValueError("Invalid Capacity")
        self._capacity = int(capacity)

    @size.setter
    def size(self, size):
        self._size = size
