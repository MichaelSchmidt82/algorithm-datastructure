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

class BinarySearchTree:
    """ A basic binary search tree """
    class _node:
        """ A basic node object for trees """
        def __init__(self, data):
            """ Create a node with no children and just a data element
            :data:      object()      Which implements relational <, >, ==
            """
            self.left = None
            self.right = None
            self.data = data

            self.height = 1

        def pre_order(self):
            """ pre-order traversal generator function """
            if self.data is not None:
                yield self.data
            if self.left:
                for data in self.left.pre_order():
                    yield data
            if self.right:
                for data in self.right.pre_order():
                    yield data

        def in_order(self):
            """ in-order traversal generator function """
            if self.left:
                for data in self.left.in_order():
                    yield data
            if self.data:
                yield self.data
            if self.right:
                for data in self.right.in_order():
                    yield data

        def post_order(self):
            """ post-order traversal generator function """
            if self.left:
                for data in self.left.post_order():
                    yield data
            if self.right:
                for data in self.right.post_order():
                    yield data
            if self.data:
                yield self.data

    def __init__(self, data):
        """ construct the root of the tree """
        self.root = self._node(data)

    def insert(self, data):
        """ Insert an element into the tree
        :data:      object()        Which implements <, >, ==
        """
        if not self.root.left and data < self.root.data:
            self.root.left = self._node(data)
        elif not self.root.right and data > self.root.data:
            self.root.right = self._node(data)
        else:
            self._insert(self.root, data)

    def find(self, data) -> bool:
        """ Search tree to check if `data` is in tree
        :data:      object()        Which implements <, >, ==
        :returns:   bool            True if found, otherwise False
        """
        return self._find(self.root, data)

    def _insert(self, node, data):
        """ Hidden method for recursive insert
        :node:      _node()         root node of subtree
        :data:      object()        which implements <, >, ==
        """
        if node.data:
            if data < node.data:
                if node.left is None:
                    node.left = self._node(data)
                else:
                    self._insert(node.left, data)
            elif data > node.data:
                if node.right is None:
                    node.right = self._node(data)
                else:
                    self._insert(node.right, data)
        else:
            node.data = data

    def _find(self, node, data) -> bool:
        """ Hidden method for recursive search
        :node:      _node()         root node of subtree
        :data:      object()        which implements <, >, ==
        """
        if node:
            if data == node.data:
                return True
            if data < node.data:
                return self._find(node.left, data)

            return self._find(node.right, data)
        return False

    def pre_order(self):
        """ Public method which returns a generator for pre-order traversal """
        return self.root.pre_order()

    def in_order(self):
        """ Public method which returns a generator for in-order traversal """
        for data in self.root.in_order():
            yield data

    def post_order(self):
        """ Public method which returns a generator for post-order traversal """
        for data in self.root.post_order():
            yield data


class AVLTree(BinarySearchTree):
    """ A self-balancing AVL tree """
    def __init__(self, data):
        """ Construct the root node
        :data:      object()          Which implements relational <, >, ==
        """
        super(AVLTree, self).__init__(data)

    def insert(self, data):
        """ Public method for inserting data
        :data:      object()           Which implements relational <, >, ==
        """
        self._insert(self.root, data)

    def delete(self, data):
        """ Public method for recursive delete
        Removes element and balances the tree
        :data:      object           Which implements relational <, >, ==
        """
        self.root = self._delete(self.root, data)

    def _insert(self, node, data) -> BinarySearchTree._node:
        """ Hidden method for recursive insert
        :node:      _node()         A tree node
        :data:      object           Which implements relational <, >, ==
        """
        if not node:
            return self._node(data)

        if data < node.data:
            node.left = self._insert(node.left, data)
        else:
            node.right = self._insert(node.right, data)

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))

        balance = self._get_balance(node)
        if balance > 1 and data < node.left.data:
            return self._rotate_right(node)

        if balance < -1 and data > node.right.data:
            return self._rotate_left(node)

        if balance > 1 and data > node.left.data:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and data < node.right.data:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _delete(self, node, data):
        """ Hidden method for recursive delete
        :node:      _node()         A tree node
        :data:      object          Which implements relational <, >, ==
        """
        if not node:
            return node

        if data < node.data:
            node.left = self._delete(node.left, data)
        elif data > node.data:
            node.right = self._delete(node.right, data)

        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp

            if node.right is None:
                temp = node.left
                node = None
                return temp

            temp = self._get_minvalue_node(node.right)
            node.data = temp.data
            node.right = self._delete(node.right, temp.data)

        if node is None:
            return node

        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        balance = self._get_balance(node)

        if balance > 1 and self._get_balance(node.left) >= 0:
            return self._rotate_right(node)

        if balance < -1 and self._get_balance(node.right) <= 0:
            return self._rotate_left(node)

        if balance > 1 and self._get_balance(node.left) < 0:
            node.left = self._rotate_left(node.left)
            return self._rotate_right(node)

        if balance < -1 and self._get_balance(node.right) > 0:
            node.right = self._rotate_right(node.right)
            return self._rotate_left(node)

        return node

    def _rotate_left(self, subtree):
        """ Hidden method for left rotations
        :subtree:   _node()     Root node of a subtree
        """
        new_root = subtree.right
        left = new_root.left

        new_root.left = subtree
        subtree.right = left

        subtree.height = 1 + max(self._get_height(subtree.left), self._get_height(subtree.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))
        return new_root

    def _rotate_right(self, subtree):
        """ Hidden method for right rotations
        :subtree:   _node()     Root node of a subtree
        """
        new_root = subtree.left
        right = new_root.right

        new_root.right = subtree
        subtree.left = right

        subtree.height = 1 + max(self._get_height(subtree.left), self._get_height(subtree.right))
        new_root.height = 1 + max(self._get_height(new_root.left), self._get_height(new_root.right))
        return new_root

    def _get_height(self, subtree):
        """ Hidden method which returns the nodes height in the tree
        :subtree:   _node()     Root node of a subtree
        """
        if not subtree:
            return 0
        return subtree.height

    def _get_balance(self, subtree):
        """ Hidden method which determines the tree balance
        :subtree:   _node()     Root node of a subtree
        """
        if not subtree:
            return 0
        return self._get_height(subtree.left) - self._get_height(subtree.right)

    def _get_minvalue_node(self, node):
        if node is None or node.left is None:
            return node

        return self._get_minvalue_node(node.left)
