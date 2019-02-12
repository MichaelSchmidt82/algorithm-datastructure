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

class Tree:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Tree(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Tree(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def in_order(self):
        if self.left:
            for data in self.left.in_order():
                yield data

        if self.data:
            yield self.data

        if self.right:
            for data in self.right.in_order():
                yield data

    def pre_order(self):
        if self.data:
            yield self.data

        if self.left:
            for data in self.left.pre_order():
                yield data

        if self.right:
            for data in self.right.pre_order():
                yield data

    def post_order(self):
        if self.left:
            for data in self.left.post_order():
                yield data

        if self.right:
            for data in self.right.post_order():
                yield data

        if self.data:
            yield self.data


root = Tree(50)

root.insert(25)
root.insert(12)
root.insert(37)

root.insert(75)
root.insert(87)
root.insert(62)

for value in root.post_order():
    print(value)
