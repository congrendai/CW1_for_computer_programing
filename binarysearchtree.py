# Some ideas of implementing Binary Search Trss are from https://gist.github.com/jakemmarsh/8273963, 
# including search(), search_node(), insert(), insert_node()
from requests import delete


class TreeNode():
    def __init__(self, cargo = None):
        self.__cargo = cargo
        self.__left_child = None
        self.__right_child = None

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo
    
    def get_left_child(self):
        return self.__left_child
    
    def set_left_child(self, node):
        self.__left_child = node

    def get_right_child(self):
        return self.__right_child

    def set_right_child(self, node):
        self.__right_child = node

    # Referenced from https://github.com/pagekeytech/education/blob/master/BST/bst.py
    def traverse(self, l):
        if self.get_left_child():
            self.get_left_child().traverse(l)
        l.append(self.get_cargo())
        if self.get_right_child():
            self.get_right_child().traverse(l)
        return l

    # Referenced from https://stackoverflow.com/questions/62406562/how-to-print-a-binary-search-tree-in-python
    def __repr__(self):
        lines = []
        if self.get_right_child():
            found = False
            for line in repr(self.get_right_child()).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " ┌─" + line
                elif found:
                    line = " | " + line
                else:
                    line = "   " + line
                lines.append(line)

        lines.append(str(self.get_cargo()))
        if self.get_left_child():
            found = False
            for line in repr(self.get_left_child()).split("\n"):
                if line[0] != " ":
                    found = True
                    line = " └─" + line
                elif found:
                    line = "   " + line
                else:
                    line = " | " + line
                lines.append(line)
        return "\n".join(lines)


class BinarySearchTree():
    def __init__(self):
        self.__root = None
        self.__size = 0
        self.__count = 0

    def get_root(self):
        return self.__root

    def set_root(self, cargo):
        self.__root = TreeNode(cargo)

    def get_count(self):
        return self.__count

    def set_count(self, value):
        self.__count = value

    def get_size(self):
        return self.__size

    def set_size(self, value):
        self.__size = value

    # This method checks whether BST is empty
    def is_empty(self):
        if self.__count == 0: return True
        else: return False

    # This method checks whether BST is full
    def is_full(self):
        if self.__count == self.__size: return True
        else: False

    # This method is used for searching values
    def search(self, cargo):
        return self.search_node(self.__root, cargo)

    # This method recursively searches nodes that whether have specific values
    def search_node(self, current_node, cargo):
        if(current_node is None):
            return False
        elif(cargo == current_node.get_cargo()):
            return True
        elif(cargo < current_node.get_cargo()):
            return self.search_node(current_node.get_left_child(), cargo)
        else:
            return self.search_node(current_node.get_right_child(), cargo)

    # This method checks whether the BSt has root and 
    # whether reaches the size limit, before inserting nodes
    def insert(self, cargo):
        if(self.get_root() is None):
            self.set_root(cargo)
            self.set_count(self.get_count() + 1)
        else:
            if not self.is_full():
                self.insert_node(self.__root, cargo)
                self.set_count(self.get_count() + 1)
            else: print("The BST has reached its size ({}).".format(self.__size))
    
    # This method recursively insert nodes with specific values
    # And duplicate values will be added to the left
    def insert_node(self, current_node, cargo):
        if cargo <= current_node.get_cargo():
            if current_node.get_left_child():
                self.insert_node(current_node.get_left_child(), cargo)
            else:
                current_node.set_left_child(TreeNode(cargo))
        elif cargo > current_node.get_cargo():
            if current_node.get_right_child():
                self.insert_node(current_node.get_right_child(), cargo)
            else:
                current_node.set_right_child(TreeNode(cargo))

    # Referenced from https://github.com/pagekeytech/education/blob/master/BST/bst.py
    def delete(self, d):
        # Case 1: Empty Tree?
        if self.__root == None:
            return False
            
        # Case 2: Deleting root node
        if self.__root.get_cargo() == d:
            # Case 2.1: Root node has no children
            if self.__root.get_left_child() is None and self.__root.get_right_child() is None:
                self.set_root(None)
                return True
            # Case 2.2: Root node has left child
            elif self.__root.get_left_child() and self.__root.get_right_child() is None:
                self.__root = self.__root.get_left_child()
                return True
            # Case 2.3: Root node has right child
            elif self.__root.get_left_child() is None and self.__root.get_right_child():
                self.__root = self.__root().get_right_child()
                return True
            # Case 2.4: Root node has two children
            else:
                moveNode = self.__root.get_left_child()
                moveNodeParent = None
                while moveNode.get_left_child():
                    moveNodeParent = moveNode
                    moveNode = moveNode.get_left_child()
                self.__root = moveNode.get_cargo()
                if moveNode.get_cargo() < moveNodeParent.get_cargo():
                    moveNodeParent.set_left_child(None)
                else:
                    moveNodeParent.__right_child =None
                return True		
        # Find node to remove
        parent = None
        node = self.__root
        while node and node.get_cargo() != d:
            parent = node
            if d < node.get_cargo():
                node = node.get_left_child()
            elif d > node.get_cargo():
                node = node.get_right_child()
        # Case 3: Node not found
        if node == None or node.get_cargo() != d:
            return False
        # Case 4: Node has no children
        elif node.get_left_child() is None and node.get_right_child() is None:
            if d < parent.get_cargo():
                parent.set_left_child(None)
            else:
                parent.set_right_child(None)
            return True
        # Case 5: Node has left child only
        elif node.get_left_child() and node.get_right_child() is None:
            if d < parent.get_cargo():
                parent.set_left_child(node.get_left_child())
            else:
                parent.set_right_child(node.get_left_child())
            return True
        # Case 6: Node has right child only
        elif node.get_left_child() is None and node.get_right_child():
            if d < parent.get_cargo():
                parent.set_left_child(node.get_right_child())
            else:
                parent.set_right_child(node.get_right_child())
            return True
        # Case 7: Node has left and right child
        else:
            moveNodeParent = node
            moveNode = node.get_right_child()
            while moveNode.get_left_child():
                moveNodeParent = moveNode
                moveNode = moveNode.get_left_child()
            node.set_cargo(moveNode.get_cargo())
            if moveNode.get_right_child():
                if moveNode.get_cargo() < moveNodeParent.get_cargo():
                    moveNodeParent.set_left_child(moveNode.get_right_child())
                else:
                    moveNodeParent.set_right_child(moveNode.get_right_child())
            else:
                if moveNode.get_cargo() < moveNodeParent.get_cargo():
                    moveNodeParent.set_left_child(None)
                else:
                    moveNodeParent.set_right_child(None)
            return True

    # Referenced from https://github.com/pagekeytech/education/blob/master/BST/bst.py
    def traverse(self):
        if self.get_root(): return self.get_root().traverse([])
        else: return []

    # Referenced from https://stackoverflow.com/questions/62406562/how-to-print-a-binary-search-tree-in-python
    def print_tree(self):
        print(self.__root)

if __name__ == '__main__':
    binary_search_tree = BinarySearchTree()
    binary_search_tree.set_size(100)

    # insert nodes
    binary_search_tree.insert(100)
    binary_search_tree.insert(50)
    binary_search_tree.insert(112)
    binary_search_tree.insert(30)
    binary_search_tree.insert(100)
    binary_search_tree.insert(60)
    binary_search_tree.insert(130)
    binary_search_tree.insert(127)
    binary_search_tree.insert(1)

    # Search nodes
    print(binary_search_tree.search(20))

    # Traverse the BST
    traverse = binary_search_tree.traverse()
    print(*traverse)

    # Delete nodes
    binary_search_tree.delete(127)
    traverse = binary_search_tree.traverse()
    print(*traverse)

    # Look the tree graph from the left (that's the root)
    binary_search_tree.print_tree()