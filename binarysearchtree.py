# Some ideas of implementing Binary Search Trss are from https://gist.github.com/jakemmarsh/8273963

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

    def is_empty(self):
        if self.__count == 0: return True
        else: return False

    def is_full(self):
        if self.__count == self.__size: return True
        else: False

    def search(self, cargo):
        return self.search_node(self.__root, cargo)

    def search_node(self, current_node, cargo):
        if(current_node is None):
            return False
        elif(cargo == current_node.get_cargo()):
            return True
        elif(cargo < current_node.get_cargo()):
            return self.search_node(current_node.get_left_child(), cargo)
        else:
            return self.search_node(current_node.get_right_child(), cargo)

    def insert(self, cargo):
        if(self.get_root() is None):
            self.set_root(cargo)
            self.set_count(self.get_count() + 1)
        else:
            if self.__count < self.__size:
                self.insert_node(self.__root, cargo)
                self.set_count(self.get_count() + 1)
            else: print("The BST has reached its size ({}).".format(self.__size))

    def insert_node(self, current_node, cargo):
        # Duplicate values will be added to the left
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

    def delete(self, cargo):
        pass

    def traverse(self):
        pass

    def print_tree(self):
        pass

if __name__ == '__main__':
    binary_search_tree = BinarySearchTree()
    binary_search_tree.set_size(6)
    binary_search_tree.insert(10)
    binary_search_tree.insert(15)
    binary_search_tree.insert(20)
    binary_search_tree.insert(30)
    binary_search_tree.insert(12)
    binary_search_tree.insert(22)