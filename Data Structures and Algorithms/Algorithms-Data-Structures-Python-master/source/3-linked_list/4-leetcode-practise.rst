Leetcode Practise
=========================

Reverse Linked List
------------------------

https://leetcode.com/problems/reverse-linked-list/

Solution

.. code-block:: python

  # Definition for singly-linked list.
  # class ListNode:
  #     def __init__(self, val=0, next=None):
  #         self.val = val
  #         self.next = next
  class Solution:
      def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
          if not head:
              return
          if head.next == None:
              return head

          prev = None
          curr = head
          after = curr.next

          while after:
              curr.next = prev
              prev = curr
              curr = after
              after = after.next

          curr.next = prev
          return curr

Middle of the Linked List
---------------------------

https://leetcode.com/problems/middle-of-the-linked-list/

Palindrome Linked List
------------------------

https://leetcode.com/problems/palindrome-linked-list/

Reverse Linked List II
----------------------------

https://leetcode.com/problems/reverse-linked-list-ii/

