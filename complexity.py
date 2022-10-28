import time
import math
from random import randint
import matplotlib.pyplot as plt
from linkedlist import LinkedList
from binarysearchtree import BinarySearchTree

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

# split lists by step
def divide_lists(list, step):
    for i in range(0, len(list), step):
        yield list[i:i + step]

if __name__ == '__main__':
    binary_search_tree = BinarySearchTree()

    equally_spaced_numbers = [i for i in range(5,105,5)]
    time_spent_by_tree = []
    time_spent_by_list = []    
    
    # Store the average time spent by list
    for number in equally_spaced_numbers:
        for i in range(1000):
            binary_search_tree, linked_list = random_tree_list(number)

            # Search 42 by the binary search tree
            start_time_for_BST = time.time()
            binary_search_tree.search(42)
            elapsed_time_for_BST = time.time() - start_time_for_BST
            time_spent_by_tree.append(elapsed_time_for_BST)

            # Search 42 by the linked list
            start_time_for_list = time.time()
            linked_list.search(42)
            elapsed_time_for_list = time.time() - start_time_for_list
            time_spent_by_list.append(elapsed_time_for_list)

    temp_tree = divide_lists(time_spent_by_tree, 1000)
    average_time_spent_by_tree = []
    for t in temp_tree:
        average_time_spent_by_tree.append(sum(t) / len(t))

    temp_list = divide_lists(time_spent_by_list, 1000)
    average_time_spent_by_list = []
    for t in temp_list:
        average_time_spent_by_list.append(sum(t) / len(t))

    print(average_time_spent_by_tree)
    print(average_time_spent_by_list)
    
    # Calculate c and b for a linear relationship
    # t = c * n + b
    # average_time_spent_by_list[0] = 5 * c + b ===> 2 * average_time_spent_by_list[0] = 10 * c + 2b
    # average_time_spent_by_list[1] = 10 * c + b
    b = 2 * average_time_spent_by_list[0] - average_time_spent_by_list[1]
    c = (average_time_spent_by_list[1] - b) / 10
    estimate_time_for_linear_relationship = []
    for number in equally_spaced_numbers:
        estimate_time_for_linear_relationship.append((number * c + b))

    
    # Calculate c and b for a logarithmic relationship
    # t = clog(n)+b
    # average_time_spent_by_tree[0] = c * math.log2(5) + b
    # average_time_spent_by_tree[1] = c * math.log2(10) + b
    c = (average_time_spent_by_tree[1] - average_time_spent_by_tree[0]) / (math.log2(10) - math.log2(5))
    b = average_time_spent_by_tree[0] - c * math.log2(5)
    estimate_time_for_logarithmic_relationship = []
    for number in equally_spaced_numbers:
        estimate_time_for_logarithmic_relationship.append((math.log2(number) * c + b))
        

    # Plot equally spaced size of BSTs and Linked Lists vs average time spent by them
    fig, axs = plt.subplots(1, 2, sharey = True)
    fig.suptitle('Average Time Spent by BST and Linked List')
    axs[0].plot(equally_spaced_numbers, average_time_spent_by_tree)
    axs[0].set_title("BST")
    axs[0].set_xlabel("Size of tree")
    axs[0].set_ylabel("Search time")
    axs[1].plot(equally_spaced_numbers, average_time_spent_by_list)
    axs[1].set_title("Linked List")
    axs[1].set_xlabel("Size of linked list")
    plt.show()

    '''
    Complexity analysis X vs Y

    For a better comparison, I put these two graph into one that is shared with y-axis. 
    The graph shows that the time of searching values by a BST approaches a logarithmic time, 
    while that of the Linked List approaches a positive linear time (as the size increases, the 
    search time increases as well). Additionally, the time spent on searching values of a BST is 
    way less than that of a Linked List if the size of BST and Linked List increases.
    '''

    # Plot equally spaced size of BST and Linked List with average time spend, estimate time for linear and logarithmic relationship
    plt.plot(equally_spaced_numbers, average_time_spent_by_tree)
    plt.plot(equally_spaced_numbers, average_time_spent_by_list)
    plt.plot(equally_spaced_numbers, estimate_time_for_linear_relationship)
    plt.plot(equally_spaced_numbers, estimate_time_for_logarithmic_relationship)
    plt.legend(["BST", "Linked List", "Linear", "Logarithmic"])
    plt.xlabel('Size')
    plt.ylabel('Search time')
    plt.title("Comparison between Average Time Spend and Estimate Time")
    plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    plt.show()


    '''
    Complexity analysis X vs Y, Y2, Y3, and Y4

    The estimated graph fits the average time spent by BST and Linked list for searching values well, 
    in most scenarios (I ran several times to see how the graphs change), which means I did not bad 
    for implementing BST and Linked List due to what shows on the graph. If I have more time, I think 
    I would make the BSTs and Linked List classes more efficient by improving the search() function.
    '''
