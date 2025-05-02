class BufferFullException(BufferError):
    """Exception raised when writing to a full buffer."""
    pass

class BufferEmptyException(BufferError):
    """Exception raised when reading from an empty buffer."""
    pass

class CircularBuffer:
    def __init__(self, capacity):
        if capacity <= 0:
            raise ValueError("Capacity must be positive")
        self._capacity = capacity
        self._buffer = [None] * capacity
        self._head = 0
        self._size = 0

    @property
    def capacity(self):
        """Return the capacity of the buffer."""
        return self._capacity

    def __len__(self):
        """Return the current size of the buffer."""
        return self._size

    def is_empty(self):
        """Check if the buffer is empty."""
        return self._size == 0

    def is_full(self):
        """Check if the buffer is full."""
        return self._size == self._capacity

    def _tail_index(self):
        """Calculate the tail index."""
        return (self._head + self._size) % self._capacity

    def read(self):
        """Read and remove the oldest item from the buffer."""
        if self.is_empty():
            raise BufferEmptyException("Circular buffer is empty")
        
        data = self._buffer[self._head]
        self._buffer[self._head] = None  # Clear the slot
        self._head = (self._head + 1) % self._capacity
        self._size -= 1
        return data

    def write(self, data):
        """Write an item to the buffer.

        Raises:
            BufferFullException: If the buffer is full.
        """
        if self.is_full():
            raise BufferFullException("Circular buffer is full")
        
        self._buffer[self._tail_index()] = data
        self._size += 1

    def overwrite(self, data):
        """Write an item to the buffer, overwriting the oldest item if full."""
        if self.is_full():
            self._buffer[self._head] = data
            self._head = (self._head + 1) % self._capacity
        else:
            self._buffer[self._tail_index()] = data
            self._size += 1

    def clear(self):
        """Clear the buffer."""
        for i in range(self._capacity):
            self._buffer[i] = None
        self._head = 0
        self._size = 0

    def __str__(self):
        """Return a string representation of the buffer."""
        return f"CircularBuffer([{', '.join(str(self._buffer[(self._head + i) % self._capacity]) for i in range(self._size))}])"
