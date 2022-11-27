# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseNumber(num: int) -> int:
        reversed_num = 0
        while num != 0:
            digit = num % 10
            reversed_num = reversed_num * 10 + digit
            num //= 10
        return reversed_num
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        arr1 = []
        while l1.next != None:
            arr1.append(l1.val)
            l1 = l1.next
        arr1.append(l1.val)
        
        arr1 = arr1[::-1]
        num1 = 0
        for i in arr1:
            num1 = num1*10 + i
        
        arr2 = []
        while l2.next != None:
            arr2.append(l2.val)
            l2 = l2.next
        arr2.append(l2.val)
        
        arr2 = arr2[::-1]
        num2 = 0
        for i in arr2:
            num2 = num2*10 + i
        
        #print(arr1, arr2, num1, num2)
        finalNumber = num1 + num2
        #print(reverseNum1, reverseNum2)
        
        #print(finalNumber)
        
        headNode = ListNode()
        l3 = headNode
        
        while finalNumber > 0:
            digit = finalNumber%10
            finalNumber //= 10
            l4 = ListNode()
            l4.val = digit
            l3.next = l4
            l3 = l3.next
            #headNode = headNode.next
            
            #print(l3.val)
        if headNode.next == None:
            return headNode
        else:
            return headNode.next
