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
    # Set the number of simulations
    number_of_tree = 1000

    # Set the number of nodes in the BST and the Linked List
    search_number = 42

    # Set the start, end, space for the spaced list
    start_of_the_spaced_list = 5
    end_of_the_spaced_list = 105
    space = 5

    # Generate a list of equally spaced numbers from 5 to 100
    equally_spaced_numbers = [i for i in range(start_of_the_spaced_list, end_of_the_spaced_list, space)]
    time_spent_by_tree = []
    time_spent_by_list = []    
    
    # Store the average time spent by list
    for number in equally_spaced_numbers:
        for _ in range(number_of_tree):
            binary_search_tree, linked_list = random_tree_list(number)

            # Search values by the binary search tree
            start_time_for_BST = time.time()
            binary_search_tree.search(search_number)
            elapsed_time_for_BST = time.time() - start_time_for_BST
            time_spent_by_tree.append(elapsed_time_for_BST)

            # Search values by the linked list
            start_time_for_list = time.time()
            linked_list.search(search_number)
            elapsed_time_for_list = time.time() - start_time_for_list
            time_spent_by_list.append(elapsed_time_for_list)

    # Calculate the average time spent by BST
    temp_tree = divide_lists(time_spent_by_tree, number_of_tree)
    average_time_spent_by_tree = []
    for t in temp_tree: average_time_spent_by_tree.append(sum(t) / len(t))

    # Calculate the average time spent by Linked List
    temp_list = divide_lists(time_spent_by_list, number_of_tree)
    average_time_spent_by_list = []
    for t in temp_list: average_time_spent_by_list.append(sum(t) / len(t))
    
    # Calculate c and b for a linear relationship
    # t = c * n + b
    # average_time_spent_by_list[0] = 5 * c + b => 2 * average_time_spent_by_list[0] = 10 * c + 2b
    # average_time_spent_by_list[1] = 10 * c + b
    b = 2 * average_time_spent_by_list[0] - average_time_spent_by_list[1]
    c = (average_time_spent_by_list[1] - b) / equally_spaced_numbers[1]
    
    # Calculate the estimated time spent by Linked List
    estimate_time_for_linear_relationship = []
    for number in equally_spaced_numbers: estimate_time_for_linear_relationship.append((number * c + b))

    # Calculate c and b for a logarithmic relationship
    # t = clog(n)+b
    # average_time_spent_by_tree[0] = c * math.log2(5) + b
    # average_time_spent_by_tree[1] = c * math.log2(10) + b
    c = (average_time_spent_by_tree[1] - average_time_spent_by_tree[0]) / (math.log2(10) - math.log2(5))
    b = average_time_spent_by_tree[0] - c * math.log2(5)

    # Calculate the estimated time spent by BST
    estimate_time_for_logarithmic_relationship = []
    for number in equally_spaced_numbers: estimate_time_for_logarithmic_relationship.append((math.log2(number) * c + b))
        
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

    # Plot equally spaced size of BST with average time spend, estimate time for linear and logarithmic relationship
    plt.plot(equally_spaced_numbers, average_time_spent_by_tree)
    plt.plot(equally_spaced_numbers, estimate_time_for_linear_relationship)
    plt.plot(equally_spaced_numbers, estimate_time_for_logarithmic_relationship)
    plt.legend(["BST", "Linear", "Logarithmic"])
    plt.xlabel('Size')
    plt.ylabel('Search time')
    plt.title("Comparison between Average Time Spend and Estimate Time")
    plt.ticklabel_format(axis='both', style='sci', scilimits=(0,0))
    plt.show()

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
    Complexity analysis X vs Y

    For a better comparison, I put these two graph into one that is shared with y-axis. 
    The graph shows that the time of searching values by a BST approaches a logarithmic time, 
    while that of the Linked List approaches a positive linear time (as the size increases, the 
    search time increases as well). Additionally, the average time spent on searching values of 
    a BST is way less than that of a Linked List if the size of BST and Linked List increases to 
    a quiet large number, say, 100. 

    -----------------------------------------------------------------------------------------------

    Complexity analysis X vs Y, Y2, and Y3

    The graph shows that the time of searching values by a BST and estimated time for a linear time 
    and a logarithmic time, which fits well with the estimated logarithmic time, based on the initial
    graph. However, the real averaged time spent by BST is not exacly the same as the estimated one.
    This happens may because the BSTs are not balanced where the line does not fit the estimated one.
    If all the BSTs with random numbers that are balanced, it might fit the estimated one precisely.
    Although they are not the same, the real time spent on searching by BSTs approaches the estimated 
    one, which means that the implementation of BST is quiet good.

    -----------------------------------------------------------------------------------------------

    Complexity analysis X vs Y, Y2, Y3, and Y4

    The estimated graph fits the average time spent by BST and Linked list for searching values well, 
    in most scenarios (I ran several times to see how the graphs change), which means I did not bad 
    for implementing BST and Linked List due to what shows on the graph. However, the average time 
    spent on searching values by Linked List sometimes fail to fit the estimated one. This is happens 
    might because the two times selected to calculate "c" and "b" are too close to each other, which 
    makes the estimated time line sentisive in terms of the c. If I select two times that are far 
    from each other, the estimated one might be more precise.
    '''