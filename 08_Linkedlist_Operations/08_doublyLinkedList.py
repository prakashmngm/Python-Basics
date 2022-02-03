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
        tempPtr = self.head
        while(tempPtr != None):
            print(str(tempPtr.data)+'->',end = '')
            tempPtr = tempPtr.nextPtr
        print()
    
    def printDLLReverse(self):
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
        if(index == 0):
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
myDLL1.insert(0,N4)
myDLL1.printDLL()
myDLL1.printDLLReverse()
