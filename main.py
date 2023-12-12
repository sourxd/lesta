from typing import Any


class FirstBufferFifo:
    """
    +++:
    Простой буфер, size для контроля объема буфера.

    ---:
    Использование лишней памяти при удалении из буфера.
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.buffer = [None] * capacity
        self.head = 0
        self.tail = 0
        self.size = 0

    def enq(self, item: Any) -> None:
        if self.size == self.capacity:
            return 'Full'
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

    def deq(self) -> Any:
        if self.size == 0:
            return 'Empty'
        item = self.buffer[self.head]
        self.head = (self.head + 1) % self.capacity
        self.size -= 1
        return item

    def clear(self):
        self.__init__(self.capacity)
