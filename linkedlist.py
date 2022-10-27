class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


class LinkedList:
    def __init__(self) -> None:
        self.head = Node()
        self.length = 0

    def show(self, depth):
        if self.length == 0:
            print("The list is empty.")

        else:
            temp = self.head
            if 0 <= depth <= self.length-1:

                if depth == 0:
                    print("The linked list in {} depth:".format(depth))
                    print(temp)
                    print("\n")

                else:
                    print("The linked list in {} depth:".format(depth))
                    print(temp)
                    while True:
                        temp = temp.next
                        print(temp)

                        depth = depth -1
                        if depth == 0:
                            break
                    print("\n")

            else:
                print("The depth is out of boundry.")

    def show_all(self):
        temp = self.head
        print("The linked list contains:")
        while temp:
            print(temp)
            temp = temp.next
                

    def find_length(self):
        print("The length of the linked list is:", self.length) 

    def reverse(self):
        pass

    def add(self, cargo, index):

        if 0 <= index <= self.length:
            temp = self.head
            new_node = Node(cargo)

            if index == 0:
                
                if temp.next != None:
                    next_node = temp
                    self.head = new_node
                    new_node.next = next_node
                    self.length = self.length + 1

                else:
                    self.head = new_node
                    self.length = self.length + 1

            else:
                for _ in range(index-1):
                    temp = temp.next

                if temp.next != None:
                    next_node = temp.next
                    temp.next = new_node
                    new_node.next = next_node
                    self.length = self.length + 1

                else:
                    temp.next = new_node
                    self.length = self.length + 1

        else:
            print("Cannot add a node: the index is out of bountry")
            
    def remove(self, index):
        temp = self.head
        if 0 <= index < self.length:
            if index == 0:
                
                if temp.next != None:
                    self.head = self.head.next
                    self.length = self.length - 1

                else:
                    self.head = Node()
                    self.length = 0

            else:
                for _ in range(index-1):
                    temp = temp.next

                if temp.next.next != None:
                    next_node = temp.next.next
                    temp.next = next_node
                    self.length = self.length - 1

                else:
                    temp.next = None
                    self.length = self.length - 1

        else:
            print("Cannot remove a node: the index is out of boundry.")


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.add("data1", 0)
    linked_list.add("data2", 1)
    linked_list.add("data3", 2)
    linked_list.add("data4", 3)

    linked_list.remove(3)

    linked_list.show(2)
    linked_list.show_all()