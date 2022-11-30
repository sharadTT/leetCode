class Solution:
    def mergeTwoLists(self, list1: [ListNode], list2: [ListNode]) -> [ListNode]:
        finalList = []
        listOne = []
        listTwo = []
        
        if list1 == None and list2 == None:
            return None
        
        if not list1 == None:
            while list1.next != None:
                listOne.append(list1.val)
                list1 = list1.next
            listOne.append(list1.val)
        
        if not list2 == None:
            while list2.next != None:
                listTwo.append(list2.val)
                list2 = list2.next
            listTwo.append(list2.val)
            
        finalList = listOne + listTwo
        finalList.sort()
        #finalList = reversed(finalList)
            
        #print(finalList)
        #finalNumber = int(''.join(map(str, reversed(finalList))))
        
        headNode = ListNode()
        l3 = headNode
        
        for digit in finalList:
            l4 = ListNode()
            l4.val = digit
            l3.next = l4
            l3 = l3.next
            
        if headNode.next == None:
            return headNode
        else:
            return headNode.next
