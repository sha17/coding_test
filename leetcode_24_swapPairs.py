# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.swapPairsAux(None, head, head, 0)
        
    def swapPairsAux(self, prev, curr, head, idx):
        if curr==None:
            return head
        
        if idx%2==1 or curr.next==None:
            new_prev, new_next = curr, curr.next
        
        elif curr.next!=None:
            if prev!=None:
                prev.next = curr.next
            else:
                head = curr.next
            curr.next.next, curr.next = curr, curr.next.next
            new_prev, new_next = curr.next, curr
            
        return self.swapPairsAux(new_prev, new_next, head, idx+1)
            
