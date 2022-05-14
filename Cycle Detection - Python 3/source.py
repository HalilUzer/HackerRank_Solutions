# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def has_cycle(head):
    history = []
    head_t = head

    while head_t is not None:
        if head_t in history:
            return True
        history.append(head_t)
        head_t = head_t.next
    
    return False