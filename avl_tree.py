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

from tree import Tree

class AVLTree(Tree):
    """
    A self-balancing AVL tree
    """

    def __init__(self, data):
        super(AVLTree, self).__init__(data)

        self.bal = 0

    def insert(self, value):
        """
        Insert and balance (if needed).
        """

        if value == self.data:
            return False

        if value < self.data:
            if not self.left:
                self.left = Tree(value)
                if not self.right:
                    self.bal = -1
                else:
                    self.bal = 0
            else:
                if self.left.insert(value):
                    if self.left.bal < -1 or self.left.bal > 1:
                        self.rebalance(self.left)
                    else:
                        self.bal -= 1

        if value > self.data:
            if not self.right:
                self.right = Tree(value)
                if not self.left:
                    self.bal = 1
                else:
                    self.bal = 0
            else:
                if self.right.insert(value):
                    if self.right.bal < -1 or self.right.bal > 1:
                        self.rebalance(self.right)
                    else:
                        self.bal += 1

        if not self.bal:
            return True

        return False

    def rotate_left(self, node):
        """
        Left branch rotation
        """

        r = node.right
        node.right = r.Left

        r.left = node

        if node == self.left:
            self.left = r
        else:
            self.right = r

        node.bal = 0
        r.bal = 0

    def rotate_right(self, node):
        """
        Right branch rotation
        """

        l = node.left
        node.left = l.right

        l.right = node

        if node == self.left:
            self.left = l
        else:
            self.right = l

        node.bal = 0
        l.bal = 0

    def rotate_right_left(self, node):
        """
        right-left rotation
        """

        node.right.left.bal = 1
        node.rotate_right(node.right)
        node.right.bal = 1
        self.rotate_left(node)

    def rotate_left_right(self, node):
        """
        left-right rotation
        """

        node.left.right.bal = -1
        node.rotate_left(node.left)
        node.left.bal = -1
        self.rotate_right(node)


    def rebalance(self, node):
        """
        Full rebalance
        """

        if node.bal == -2 and node.left.bal == -1:
            self.rotate_right(node)

        if node.bal == 2 and node.right.bal == 1:
            self.rotate_left(node)

        if node.bal == -2 and node.left.bal == 1:
            self.rotate_left_right(node)

        if node.bal == 2 and node.right.bal == -1:
            self.rotate_right_left(node)
