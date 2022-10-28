import time
import math
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

    
    # Calculate c and b for a linear relationship
    # average_time_spent_by_list[0] = 5 * c + b
    # average_time_spent_by_list[1] = 10 * c + b
    c = (average_time_spent_by_list[9] - average_time_spent_by_list[0]) / 45
    b = average_time_spent_by_list[0] - 45 * c
    estimate_time_for_linear_relationship = []
    for number in equally_spaced_numbers:
        estimate_time_for_linear_relationship.append((number * c + b))

    
    # Calculate c and b for a logarithmic relationship
    # t = clog(n)+b
    # average_time_spent_by_tree[0] = c * math.log2(5) + b
    # average_time_spent_by_tree[1] = c * math.log2(10) + b
    c = (average_time_spent_by_tree[9] - average_time_spent_by_tree[0]) / (math.log2(50) - math.log2(5))
    b = average_time_spent_by_tree[0] - c * math.log2(5)
    estimate_time_for_logarithmic_relationship = []
    for number in equally_spaced_numbers:
        estimate_time_for_logarithmic_relationship.append((math.log2(number) * c + b))
        

    # Plot equally spaced size of BSTs and Linked Lists vs average time spent by them
    fig, axs = plt.subplots(1, 2, sharey = True)
    fig.suptitle('Equally Spaced Size Numbers VS Average Time Spent')
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

    For a better comparison, I change the size n to 5 - 1000 spaced by 5, and put 
    these two graph into one that is shared with y-axis. The graph shows that the 
    time of searching values by a BST approaches a logarithmic time, while that of 
    the Linked List approaches a positive linear time (as the size increases, the 
    search time increases as well). Although the graph of the Linked List is 
    volatile, it still shows that there is a linear relationship between x and y
    -axis of the Linked List. Additionally, the time spent on searching values of
    a BST is way less than that of a Linked List.
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
    Complexity analysis X vs Y, Y2 and Y3

    Since I change the size n to 5 - 1000 spaced by 5, I also change the values 
    to calculate c and b for BST and Linked List. This is because if the two 
    selected times for calculating c and b are too close, the estimated graph 
    cannot fit the average time spent for searching well, which might be the reason 
    that, in most scenarios (I ran several times to see how the graphs change), 
    estimated graph cannot fit the real case perfectly, but the estimated graph 
    for BST fit well since BST uses way less to search, compared to Linked list.
    The estimated Graph for Linked List varies dramatically, which fits real time 
    spent sometimes. Also, I think did not bad for implementing BST and Linked List 
    due to what shows on the graph. If I have more time, I think I would make the BSTs 
    and Linked List classes more efficient by improving the search() function.
    '''
