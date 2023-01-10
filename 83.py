# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head

        while cur:
            if cur == prev:
                temp = cur
                del cur
                prev = temp
                cur = temp.next
                
            else:
                prev = cur
                cur = cur.next
        return head