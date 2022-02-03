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
            
    def insert(self,index,nodeobj):
        if(index > self.length() or index < 0):
            print('Index is invalid')
        elif(index == 0):
            tempPtr = self.head
            tempPtr.prevPtr = nodeobj
            nodeobj.nextPtr = tempPtr
            self.head = nodeobj
        else:
            tempPtr = self.head
            start = 0
            while(start < index-1):
                tempPtr = tempPtr.nextPtr
                start = start+1
            nodeobj.nextPtr = tempPtr.nextPtr
            nodeobj.prevPtr = tempPtr
            tempPtr.nextPtr = nodeobj
            tempPtr = tempPtr.nextPtr.nextPtr
            if(tempPtr != None):
                tempPtr.prevPtr = nodeobj
    def length(self):
        tempPtr = self.head
        length = 0
        while(tempPtr != None):
            length = length+1
            tempPtr = tempPtr.nextPtr
        return length
        
    def createCopy(self,dll):
        tempPtr = dll.head
        while(tempPtr != None):
            node = Node(tempPtr.data)
            self.append(node)
            tempPtr = tempPtr.nextPtr
    
    def deleteFirstNode(self):
        if(self.length() == 0):
            print('Empty Linked List')
        elif(self.length() == 1):
            self.head = None
        else:
            tempPtr = self.head.nextPtr
            self.head = tempPtr
            tempPtr.prevPtr = None
            
    def deleteLastNode(self):
        if(self.length() == 0):
            print('Empty Linked List')
        elif(self.length() == 1):
            self.head = None
        else:
            tempPtr = self.head
            while(tempPtr.nextPtr.nextPtr != None):
                tempPtr = tempPtr.nextPtr
            tempPtr1 = tempPtr.nextPtr
            tempPtr.nextPtr = None
            tempPtr1.prevPtr = None
    
    def delete(self,index):
        if(self.length() == 0):
            print('Empty Linked List')
        elif(self.length() == 1):
            self.head = None
        elif(index == 0):
            tempPtr = self.head.nextPtr
            self.head.nextPtr = None
            self.head = tempPtr
            tempPtr.prevPtr = None
        elif(index == self.length()-1):
            tempPtr = self.head
            while(tempPtr.nextPtr.nextPtr != None):
                tempPtr = tempPtr.nextPtr
            tempPtr1 = tempPtr.nextPtr
            tempPtr.nextPtr = None
            tempPtr1.prevPtr = None
        else:
            start = 0
            tempPtr = self.head
            while(start < index-1):
                tempPtr = tempPtr.nextPtr
                start = start+1
            tempPtr1 = tempPtr.nextPtr.nextPtr
            tempPtr.nextPtr.nextPtr = None
            tempPtr1.prevPtr.prevPtr = None
            tempPtr.nextPtr = tempPtr1
            tempPtr1.prevPtr = tempPtr
#--------------------------------------------------------------------

N1 = Node(5)
myDLL = DLL()
myDLL.append(N1)
myDLL.printDLLReverse()
myDLL.printDLL()

N2 = Node(6)
myDLL.append(N2)
myDLL.printDLL()
myDLL.printDLLReverse()

N3 = Node(7)
myDLL.append(N3)
myDLL.printDLL()
myDLL.printDLLReverse()

myDLL1 = DLL()
myDLL1.createDLLfromList([11,12,13,18,19,20])
myDLL1.printDLL()
myDLL1.printDLLReverse()

N4 = Node(25)
myDLL1.insert(-1,N4)
myDLL1.printDLL()
myDLL1.printDLLReverse()
print(myDLL1.length())

newDLL = DLL()
print(newDLL.length())
newDLL.createDLLfromList([30,40,50])
print(newDLL.length())

MyDLL2 = DLL()
MyDLL2.createCopy(myDLL1)
MyDLL2.printDLL()
MyDLL2.printDLLReverse()

MyDLL3 = DLL()
MyDLL3.deleteFirstNode()
MyDLL3.createDLLfromList([1,2,3,4,5])
MyDLL3.deleteFirstNode()
MyDLL3.printDLL()
MyDLL3.printDLLReverse()
MyDLL3.deleteLastNode()
MyDLL3.printDLL()
MyDLL3.printDLLReverse()

MyDLL4 = DLL()
MyDLL4.createDLLfromList([11,12,13,18,19,20])
MyDLL4.delete(0)
MyDLL4.printDLL()
MyDLL4.printDLLReverse()
