# Linked List Quick Sort Algorithm

This repository contains a Python script that demonstrates the implementation of the Quick Sort algorithm on a singly linked list. The script is designed to create and sort a linked list using the principles of the Quick Sort algorithm. It utilizes classes and functions to create a linked list, insert elements, and perform the Quick Sort operation.

## Linked List Quick Sort Algorithm Python Script

The Python script provided in this repository showcases the following functionalities:

1. **Node Class:** Defines a `Node` class, where each node holds an integer value (`data`) and a reference to the next node (`next`).

2. **LinkedList Class:** Defines a `LinkedList` class responsible for managing the linked list. It includes methods to insert new data elements at the beginning of the list and display the linked list as a string.

3. **Partition Function:** Implements the partitioning step of the Quick Sort algorithm. The `partition` function takes a start node and an end node as parameters and rearranges the elements in such a way that elements less than the pivot are on the left and elements greater than the pivot are on the right.

4. **Quicksort Function:** Implements the Quick Sort algorithm for the linked list. The `quicksort_LL` function recursively applies the partitioning process to sort the linked list in ascending order.

5. **Main Function:** In the `if __name__ == "__main__":` block, the script creates an instance of the `LinkedList` class, prompts the user to input space-separated values to insert into the linked list, and then displays the original linked list. It then calls the `quicksort_LL` function to sort the linked list using the Quick Sort algorithm. Finally, it prints the sorted linked list.

This script provides a clear demonstration of how the Quick Sort algorithm can be applied to a singly linked list to efficiently sort its elements.

Feel free to clone and explore this repository to understand the implementation details and run the script on your local machine to see the Quick Sort algorithm in action on a linked list.
