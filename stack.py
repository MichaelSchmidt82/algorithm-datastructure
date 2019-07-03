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

class Stack:
    """ A basic stack """
    def __init__(self):
        """ Construct an empty stack using a list() """
        self.__stack = []

    def __len__(self):
        """ Support for Python's built-in function len() """
        return len(self.__stack)

    @property
    def top(self):
        """ TOP of Stack, same as PEEK """
        if not self.__stack:
            return None
        return self.__stack[-1]

    @property
    def size(self):
        """ SIZE of Stack, see also len() """
        return len(self.__stack)

    def push(self, value=None):
        """ PUSH operation """
        self.__stack.append(value)

    def pop(self):
        """ POP operation """
        if self.__stack:
            top = self.__stack[-1]
            self.__stack = self.__stack[:-1]
            return top
        return None

    def items(self):
        """ Generator POP """
        for _ in self.__stack:
            top = self.__stack[-1]
            self.__stack = self.__stack[:-1]
            yield top

    def empty(self) -> bool:
        """ EMPTY query """
        return bool(len(self.__stack))

    def clear(self):
        """ CLEAR the Stack """
        self.__stack = []
