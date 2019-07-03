"""
MIT License

Copyright (c) 2019 Michael Schmidt

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class Queue:
    """ A simple queue """
    def __init__(self):
        """ Create an empty queue using a list() """
        self.__queue = []

    def __len__(self):
        """ support for Python's built-in function len() """
        return len(self.__queue)

    @property
    def empty(self):
        """ Check if the queue is empty """
        return bool(len(self.__queue))

    @property
    def size(self):
        """ SIZE of queue"""
        return len(self.__queue)

    @property
    def front(self):
        """ FRONT of queue"""
        if not self.__queue:
            return None
        return self.__queue[0]

    def push(self, data):
        """ PUSH operation
        :data:      object()        Data to place in queue
        """
        self.__queue.append(data)

    def pop(self):
        """ POP operation """
        if self.__queue:
            top = self.__queue[0]
            self.__queue = self.__queue[1:]
            return top
        return None

    def items(self):
        """ Generator POP """
        for _ in self.__queue:
            top = self.__queue[0]
            self.__queue = self.__queue[1:]
            yield top

    def clear(self):
        """ CLEAR the queue """
        self.__queue = []
