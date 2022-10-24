# Palindrome Linked List
# 3 Solutions
# 1. Copy linked list into array then take two pointer, then check whether array is palindrome or not using two-pointers technique. -> O(N) extra space for array
# 2. Using recursion -> O(N) space for recursion-stack
# 3. Reverse half linked-list -> O(1) space


from typing import *


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        n = []

        ptr = head

        while ptr != None:
            n.append(ptr.val)
            ptr = ptr.next

        return n == n[::-1]
