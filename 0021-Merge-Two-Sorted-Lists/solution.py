# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        temp1=list1
        temp2=list2
        dummy=ListNode()
        current=dummy 
        while temp1 and temp2:
            if temp1.val<=temp2.val:
                current.next=temp1
                current=current.next
                temp1=temp1.next
            else :
                current.next=temp2
                current=current.next
                temp2=temp2.next

        if temp1 is not None:
            current.next=temp1
        else :
            current.next=temp2
        return dummy.next











    #    result=[]
    #    i=0
    #    j=0
    #    while i<len(list1) and j<len(list2):
    #         if list1[i]<=list2[j]:
    #             result.append(list1[i])
    #             i+=1
    #         else:
    #             result.append(list2[j])
    #             j+=1

    #    return result

        