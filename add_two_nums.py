"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class LinkedList:
    def linkedListFromList(self, l)->Node:
        head = None
        temp = head
        for i in l:
            newnode = Node(i)
            if head == None:
                head = newnode
                temp = head
            else:
                temp.link = newnode
                temp = newnode
        return head

    def displayLinkedList(self, head):
        while head != None:
            print(f"{head.data} --> ",end='')
            head = head.link
        print("NULL")

    def addTwoList(self, num1, num2)->Node:
        sum = None
        temp = None
        carry = 0
        while num1 != None and num2 != None:
            sumDigits = num1.data + num2.data + carry
            r = sumDigits % 10
            carry = sumDigits // 10
            newnode = Node(r)
            if sum == None:
                sum = newnode
                temp = sum
            else:
                temp.link = newnode
                temp = newnode
            num1 = num1.link
            num2 = num2.link

        num = num1 if num1 else num2
        while num != None:
            sumDigits = num.data + carry
            r = sumDigits % 10
            carry = sumDigits // 10
            newnode = Node(r)
            if sum == None:
                sum = newnode
                temp = sum
            else:
                temp.link = newnode
                temp = newnode
            num = num.link

        if carry != 0:
            newnode = Node(carry)
            temp.link = newnode
        return sum


listObj = LinkedList()

data1 = [0, 0, 0, 1]
data2 = [9, 9, 9]

num1 = listObj.linkedListFromList(data1)

listObj.displayLinkedList(num1)

num2 = listObj.linkedListFromList(data2)

listObj.displayLinkedList(num2)

sum = listObj.addTwoList(num1, num2)

listObj.displayLinkedList(sum)