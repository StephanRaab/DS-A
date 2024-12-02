def iterativeReverseList(self, head: ListNode) -> ListNode:
    prev, curr = None, head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev #aka the new head.

def recursiveReverseList(self, head: ListNode) -> ListNode:
    if not head:
        return None

    newHead = head
    if head.next:
        self.recursiveReverseList(head.next)
        head.next.next = head
    head.next = None
    
    return newHead