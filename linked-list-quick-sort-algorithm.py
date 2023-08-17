"""
Given a linked list with head pointer, 
sort the linked list using quicksort technique without using any extra space
Time complexity: O(NlogN), Space complexity: O(1)
"""
from __future__ import annotations


class Node:
    def __init__(self, data: int):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, new_data: int):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def __str__(self):
        if self.head is None:
            return 'Linked List is empty'
        elements = []
        temp = self.head
        while temp:
            elements.append(str(temp.data))
            temp = temp.next
        return ' -> '.join(elements)


def partition(start, end):
    if start is None or start.next is None:
        return start
    pivot = start.data
    prev, curr = start, start.next
    while curr != end:
        if curr.data < pivot:
            prev = prev.next
            prev.data, curr.data = curr.data, prev.data
        curr = curr.next
    start.data, prev.data = prev.data, start.data
    return prev


def quicksort_LL(start, end):
    if start != end:
        pos = partition(start, end)
        quicksort_LL(start, pos)
        quicksort_LL(pos.next, end)


if __name__ == "__main__":
    ll = LinkedList()
    print("Enter space-separated values to insert in the linked list:")
    arr = list(map(int, input().split()))
    for num in arr:
        ll.insert(num)
    print("Linked list before sorting:", ll)
    quicksort_LL(ll.head, None)
    print('Linked list after sorting:', ll)
