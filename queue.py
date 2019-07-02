class Queue:
    """ A simple queue"""

    def __init__(self):
        self.__queue = []

    def __len__(self):
        return len(self.__queue)

    @property
    def front(self):
        """FRONT of queue"""
        if not self.__queue:
            return None
        return self.__queue[0]

    def pop(self):
        """POP operation"""
        if self.__queue:
            top = self.__queue[0]
            self.__queue = self.__queue[1:]
            return top
        return None

    def items(self):
        """Generator POP"""
        for _ in self.__queue:
            top = self.__queue[0]
            self.__queue = self.__queue[1:]
            yield top

    def push(self, value=None):
        """PUSH operation"""
        self.__queue.append(value)

    def empty(self):
        """EMPTY query"""
        return bool(len(self.__queue))

    @property
    def size(self):
        """SIZE of queue"""
        return len(self.__queue)

    def clear(self):
        """CLEAR the queue"""
        self.__queue = []
