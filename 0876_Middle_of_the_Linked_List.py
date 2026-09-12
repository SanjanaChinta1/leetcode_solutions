# Problem: Middle of the Linked List
# LeetCode: 876
# Difficulty: Easy
# Approach: Fast and Slow Pointers
# Time Complexity: O(n)
# Space Complexity: O(1)

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pt1 = head
        pt2 = head

        while pt2 is not None and pt2.next is not None:
            pt1 = pt1.next
            pt2 = pt2.next.next

        return pt1
