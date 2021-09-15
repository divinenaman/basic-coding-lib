# floyd tortoise and hare cycle algo 
# https://www.geeksforgeeks.org/how-does-floyds-slow-and-fast-pointers-approach-work/

def has_cycle(head):
    tortoise = head
    hare = head.next
    while hare and hare.next:
        if hare == tortoise:
            return 1         
        tortoise = tortoise.next
        hare = hare.next.next
    return 0