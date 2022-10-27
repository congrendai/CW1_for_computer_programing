class Node:
    def __init__(self, cargo = None, next = None):
        self.__cargo = cargo
        self.__next = next

    def __str__(self):
        return str(self.__cargo)

    def get_cargo(self):
        return self.__cargo

    def set_cargo(self, cargo):
        self.__cargo = cargo

    def get_next(self):
        return self.__next

    def set_next(self, node):
        self.__next = node

class LinkedList:
    def __init__(self) -> None:
        self.__head = Node()
        self.__length = 0
        self.__size = 0

    def get_head(self):
        return self.__head

    def set_head(self, node):
        self.__head = node

    def get_length(self):
        return self.__length

    def set_length(self, value):
        self.__length = value

    def get_size(self):
        return self.__size

    def set_size(self, value):
        self.__size = value

    # This method returns the values of the nodes in the linked order
    def traverse(self):
        linked_order_list = []
        temp = self.get_head()
        while temp:
            linked_order_list.append(str(temp.get_cargo()))
            temp = temp.get_next()
        return ", ".join(linked_order_list)
    
    # This method append a value to the end of the linked list
    def insert(self, cargo):
        if self.get_length() < self.get_size():
            new_node = Node(cargo)
            temp = self.get_head()
            if temp.get_cargo() == None:
                temp.set_cargo(cargo)
                self.set_length(self.get_length() + 1)
            else:
                while temp.get_next() != None: temp = temp.get_next()
                temp.set_next(new_node)
                self.set_length(self.get_length() + 1)
        else: print("The linked list has reached its size ({}).".format(self.__size))
    
    # This piece of code is referenced from https://www.geeksforgeeks.org/linked-list-set-3-deleting-node/
    # This method deletes the first occurrence of the value from the list
    def delete(self, cargo):
        if self.get_length() == 0: print("The linked list is empty")
        else:
            temp = self.get_head()
            if temp != None:
                if temp.get_cargo() == cargo:
                    temp.set_cargo(None)
                    self.set_length(self.get_length() - 1)
                    if temp.get_next() != None: self.set_head(temp.get_next())
                    else: print("The linked list is empty now.")
    
            while temp != None:
                if temp.get_cargo() == cargo:
                    break
                prev = temp
                temp = temp.get_next()
    
            if temp == None: return

            prev.set_next(temp.get_next())
            self.set_length(self.get_length() - 1)

    # This piece of code is referenced from https://www.geeksforgeeks.org/search-an-element-in-a-linked-list-iterative-and-recursive/
    # It can search for a given value
    def search(self, cargo):
        if self.get_length() == 0: print("The linked list is empty")
        else:
            temp = self.get_head()
            while temp != None:
                if temp.get_cargo() == cargo: return True
                temp = temp.get_next()
            return False

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.set_size(5)
    linked_list.insert(1)
    linked_list.insert(6)
    linked_list.insert(3)
    linked_list.insert(4)
    linked_list.insert(5)

    linked_list.delete(1)
    linked_list.delete(4)

    print(linked_list.search(4))
    print(linked_list.traverse())
