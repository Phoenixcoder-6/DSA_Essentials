class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

class MyLinkedList:
    @staticmethod
    def is_palindrome(head):

        if not head or not head.next: #Single node or empty list is always a palindrome
            return True
        
        #step-1 : Find the middle
        slow=fast=head
        while fast and fast.next:
            slow= slow.next
            fast= fast.next.next
        #step-2: severse the second half

        second_half= MyLinkedList.reverse_list(slow)
        first_half= head
        second_half_copy= second_half

        while second_half:
            if first_half.data != second_half.data:
                return False  # Mismatch found
            first_half = first_half.next
            second_half = second_half.next

        return True  # Palindrome confirmed


    @staticmethod
    def reverse_list(head):
        if not head or not head.next:
            return head    
        new_head= MyLinkedList.reverse_list(head.next)

        head.next.next= head
        head.next= None
        return new_head

def create_linked_list(arr):
    if not arr:
        return None
    head= Node(arr[0])
    current= head
    for val in arr[1:]:
        current.next= Node(val)
        current= current.next

    return head

# Creating a palindromic linked list: 1 -> 2 -> 3 -> 2 -> 1
head = create_linked_list([1, 2, 3, 2, 1])
print(MyLinkedList.is_palindrome(head)) 

# Creating a non-palindromic linked list: 1 -> 2 -> 3 -> 4 -> 5
head2 = create_linked_list([1, 2, 3, 4, 5])
print(MyLinkedList.is_palindrome(head2))  # Output: False

        