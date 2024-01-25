class Solution:
    def reorderList(self, head: ListNode) -> None:
        # find middle
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # reverse second half
        second = slow.next
        prev = slow.next = None
        while second:
            tmp = second.next
            second.next = prev
            prev = second
            second = tmp

        # merge two halfs
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        #create a dummy list node
        dummy = ListNode()
        #set the head equal to dummy's next
        dummy.next = head

        #use while loop to add nodes to list
        current = head
        nodes = []
        while current:
            #add node to list
            nodes.append(current)
            #move to next node
            current = current.next

        #two pointers
        l, r = 0, len(nodes) - 1

        #new dummy.next will start at list[0]
        dummy.next = nodes[l]

        #add to nodes[l] and nodes[r] using .next, -=, +=
        while l < r:
            nodes[l].next = nodes[r]
            l += 1
            nodes[r].next = nodes[l]
            r -= 1

        #need this because it adds # from left again during the last cycle.
        nodes[l].next = None
