'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr = None
        self.prevPtr = None
class DLL:
    def __init__(self):
        self.head = None
        
    def append(self,nodeobj):
        if(self.head == None):
            self.head = nodeobj
        else:
            tempPtr = self.head
            while(tempPtr.nextPtr != None):
                tempPtr = tempPtr.nextPtr
            tempPtr.nextPtr = nodeobj
            nodeobj.prevPtr = tempPtr
            
    def printDLL(self):
        if(self.head == None):
            print('Empty Linked List')
        else:
            tempPtr = self.head
            while(tempPtr != None):
                print(str(tempPtr.data)+'->',end = '')
                tempPtr = tempPtr.nextPtr
            print()
            
    def printDLLReverse(self):
        if(self.head == None):
            print('Empty Linked List')
        else:
            tempPtr = self.head
            while(tempPtr.nextPtr != None):
                tempPtr = tempPtr.nextPtr
            while(tempPtr != None):
                print(str(tempPtr.data)+'->',end = '')
                tempPtr = tempPtr.prevPtr
            print()
    
    def createDLLfromList(self,lst):
        for ele in lst:
            node = Node(ele)
            self.append(node)
    def merge(self,dll2):
        p1 = self.head
        p2 = dll2.head
        tmp1 = p1.prevPtr
        tmp2 = p2.prevPtr
        while(p1 != None and p2 != None):
            if(p1 != None and p2 != None and p1.data < p2.data):
                while(p1 != None and p2 != None and p1.data < p2.data):
                    p1 = p1.nextPtr
                    if(tmp1 == None):
                        tmp1 = self.head
                    else:
                        tmp1 = tmp1.nextPtr
                if(tmp1.nextPtr == None):
                    tmp1.nextPtr = p2
                    p2.prevPtr = tmp1
                else:
                    tmp1.nextPtr = p2
                    p1.prevPtr = p2
                    tmp2 = p2
                    p2 = p2.nextPtr
                    tmp2.prevPtr = tmp1
                    tmp2.nextPtr = p1
                    tmp1 = p1.prevPtr
            elif(p1 != None and p2 != None and p1.data == p2.data):
                p1.prevPtr = p2
                p2 = p2.nextPtr
                tmp1 = p1.prevPtr
                tmp2 = p2.prevPtr
                tmp1.nextPtr = p1
                while(p1 != None and p2 != None and p1.data == p2.data):
                    p1 = p1.nextPtr
                    if(tmp1 == None):
                        tmp1 = self.head
                    else:
                        tmp1 = tmp1.nextPtr
            else:
                while(p1 != None and p2 != None and p1.data > p2.data):
                    p2 = p2.nextPtr
                    tmp2 = tmp2.nextPtr
                if(tmp2.nextPtr == None):
                    tmp2.nextPtr = p1
                    p1.prevPtr = tmp2
                else:
                    tmp2.nextPtr = p1
                    p2.prevPtr = p1
                    tmp1 = p1
                    p1 = p1.nextPtr
                    tmp1.prevPtr = tmp2
                    tmp1.nextPtr = p2
                    tmp2 = p2.prevPtr
#----------------------------------------------------------------------------------

myDLL1 = DLL()
myDLL1.createDLLfromList([1,5,7,8,10])
myDLL2 = DLL()
myDLL2.createDLLfromList([6,9,10,11,12])
myDLL1.merge(myDLL2)

