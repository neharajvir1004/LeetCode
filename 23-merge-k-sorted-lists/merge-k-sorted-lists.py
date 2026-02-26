class Solution(object):
    def mergeKLists(self, lists):
        import heapq
        if not lists:
            return None
        
        heap = []
        
        # Push first node of each list into heap
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        dummy = ListNode(0)
        current = dummy
        
        while heap:
            val, i, node = heapq.heappop(heap)
            current.next = node
            current = current.next
            
            if node.next:
                heapq.heappush(heap, (node.next.val, i, node.next))
        
        return dummy.next