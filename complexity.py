import time
from random import randint
import matplotlib.pyplot as plt
from linkedlist import LinkedList
from binarysearchtree import BinarySearchTree

if __name__ == '__main__':
    binary_search_tree = BinarySearchTree()

    # This method generates a BST and a Linked List with n random integer
    def random_tree_list(n):
        binary_search_tree = BinarySearchTree()
        binary_search_tree.set_size(n)
        linked_list = LinkedList()
        linked_list.set_size(n)
        for _ in range(n):
            i = randint(1,1000)
            binary_search_tree.insert(i)
            linked_list.insert(i)
        return binary_search_tree, linked_list

    equally_spaced_numbers = [i for i in range(5,1005,5)]
    average_time_spent_by_tree = []
    average_time_spent_by_list = []

    estimate_time_for_tree = []
    estimate_time_for_list = []
    
    # Store the average time spent by list
    for number in equally_spaced_numbers:
        binary_search_tree, linked_list = random_tree_list(number)

        # Search 42 by the binary search tree
        start_time_for_BST = time.time()
        binary_search_tree.search(42)
        elapsed_time_for_BST = time.time() - start_time_for_BST
        average_time_spent_by_tree.append(elapsed_time_for_BST)

        # Search 42 by the linked list
        start_time_for_list = time.time()
        linked_list.search(42)
        elapsed_time_for_list = time.time() - start_time_for_list
        average_time_spent_by_list.append(elapsed_time_for_list)
        

    # Plot equally spaced size of BSTs and Linked Lists vs average time spent by them
    fig, axs = plt.subplots(1, 2, sharey = True)
    fig.suptitle('Equally Spaced Size Numbers VS Average Time Spents')
    axs[0].plot(equally_spaced_numbers, average_time_spent_by_tree)
    axs[0].set_title("BST")
    axs[0].set_xlabel("Size of tree")
    axs[0].set_ylabel("Search time")
    axs[1].plot(equally_spaced_numbers, average_time_spent_by_list)
    axs[1].set_title("Linked List")
    axs[1].set_xlabel("Size of linked list")
    plt.show()

    '''
    Complexity analysis equally spaced size of BSTs and Linked Lists vs average time spent by them

    For a better comparison, I change the size n to 5 - 1000 spaced by 5, and put 
    these two graph into one that is shared with y-axis. The graph shows that the 
    time of searching values by a BST approaches a logarithmic time, while that of 
    the Linked List approaches a linear time. Although the graph of the Linked List 
    is volatile, it still shows that there is a linear relationship between x and y
    -axis of the Linked List. Additionally, the time spent on searching values of
    a BST is way less than that of a Linked List.
    '''


