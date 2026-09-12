# Problem: Reverse Linked List
# LeetCode: 206
# Difficulty: Easy
# Approach: Iterative / Three Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev
