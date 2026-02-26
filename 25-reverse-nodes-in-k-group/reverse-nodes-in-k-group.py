class Solution(object):
    def reverseKGroup(self, head, k):

        if not head or k == 1:
            return head
        
        # Dummy node
        dummy = ListNode(0)
        dummy.next = head
        groupPrev = dummy
        
        while True:
            # Find kth node
            kth = groupPrev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            
            groupNext = kth.next
            
            # Reverse group
            prev = groupNext
            curr = groupPrev.next
            
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            
            # Connect with previous part
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp