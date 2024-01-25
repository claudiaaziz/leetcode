class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        # delete
        left.next = left.next.next
        return dummy.next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l = dummy
        r = dummy.next

        #shift r until it is at the correct position
        while n > 0 and r:
            r = r.next
            n-=1
        
        #shift l and r until l is in the right position
        while r:
            l = l.next
            r = r.next
        
        #removes the node we want
        l.next = l.next.next

        #return head and onward
        return dummy.next
