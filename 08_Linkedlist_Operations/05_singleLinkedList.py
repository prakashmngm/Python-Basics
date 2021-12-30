'''
Create a Single Linked List with names as data.
Create two user functions : print() & append()

'''

class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr = None
    
    def printData(self):
        print("Node data is:",self.data)
        
class SLL:
    def __init__(self):
        self.head = None
        
    def append(self,nodeobj):
        # First insertion , need to make head pointer points to where N1 is pointing to
        if(self.head == None):
            self.head = nodeobj
        else:
            tempPtr = self.head
            while(tempPtr.nextPtr != None):
                tempPtr = tempPtr.nextPtr
            tempPtr.nextPtr = nodeobj
            
    def printSLL(self):
        tempPtr = self.head
        while(tempPtr != None):
            print(tempPtr.data+'->',end='')
            tempPtr = tempPtr.nextPtr
        print()
        
    def length(self):
        tempPtr = self.head
        count = 0
        while(tempPtr != None):
            count = count+1
            tempPtr = tempPtr.nextPtr
        return count
        
    def printData(self,index):
        if(index < 0):
            return "invalid index"
        if(index >= self.length()):
            return 'invalid index'
        tempPtr = self.head
        start = 0
        while(start < index):
            tempPtr = tempPtr.nextPtr
            start = start+1
        return tempPtr.data
        
    # Write a function to return the list of indices of the given data element
    
    def printIndices(self,data):
        tempPtr = self.head
        list_of_indices = []
        index = 0
        while(tempPtr != None):
            if(tempPtr.data == data):
                list_of_indices.append(index)
            index = index+1
            tempPtr = tempPtr.nextPtr
        return list_of_indices
        
    # write a function to copy one linked list to other linked list
    
    def copy(self,existingSLL):
        tempPtr = existingSLL.head
        while(tempPtr != None):
            nodeobj = Node(tempPtr.data)
            self.append(nodeobj)
            tempPtr = tempPtr.nextPtr
    # write a function to update a new data element in a given index position
    
    def update(self,index,newValue):
        tempPtr = self.head
        start = 0
        while(start < index):
            tempPtr = tempPtr.nextPtr
            start = start+1
        tempPtr.data = newValue
    
    # write a function to insert a new node at the start of the SLL
    
    def insertAtStart(self,nodeobj):
        if(self.head == None):
            self.head = nodeobj
        else:
            nodeobj.nextPtr = self.head
            self.head = nodeobj
    
    # write a function to insert a new node at the end of the SLL
    
    def insertAtEnd(self,nodeobj):
        if(self.head == None):
            self.head = nodeobj
        else:
            tempPtr = self.head
            while(tempPtr.nextPtr != None):
                tempPtr = tempPtr.nextPtr
            tempPtr.nextPtr = nodeobj
    
    # write a function to insert a new node at the given index position
    
    def insert(self,index,nodeobj):
        if(self.head == None):
            self.head = nodeobj
        else:
            tempPtr = self.head
            start = 0
            while(start < index-1):
                tempPtr = tempPtr.nextPtr
                start = start+1
            nodeobj.nextPtr = tempPtr.nextPtr
            tempPtr.nextPtr = nodeobj
            
    # write a function to delete first node of the SLL
    
    def deleteFirstNode(self):
        if(self.head == None):
            return 'empty Linked List'
        else:
            tempPtr = self.head
            self.head = tempPtr.nextPtr
    
    # write a function to delete last node of the SLL
    
    def deleteLastNode(self):
        if(self.head == None):
            return 'empty Linked List'
        else:
            tempPtr = self.head
            start = 0
            while(start < self.length()-2):
                tempPtr = tempPtr.nextPtr
                start = start+1
            tempPtr.nextPtr = None
            
    # write a function to delete a node at the given index position
    
    def delete(self,index):
        if(self.head == None):
            return 'empty linked List'
        elif(index >= self.length()):
            return 'invalid index'
        else:
            tempPtr1 = self.head
            tempPtr2 = self.head
            start = 0
            while(start < index-1):
                tempPtr1 = tempPtr1.nextPtr
                start = start+1
            start = 0
            while(start < index):
                tempPtr2 = tempPtr2.nextPtr
                start = start+1
            tempPtr1.nextPtr = tempPtr2.nextPtr
            
# --------------------------------------------

N1 = Node('11')
N2 = Node('12')
N3 = Node('13')
N4 = Node('11')
N5 = Node('12')
N6 = Node('13')

mySLL = SLL()
mySLL.append(N1)
mySLL.append(N2)
mySLL.append(N3)
mySLL.append(N6)
mySLL.append(N5)
mySLL.append(N4)
mySLL.printSLL()
print(mySLL.length())
print(mySLL.printData(10))
print(mySLL.printIndices('15'))
newSLL = SLL()
newSLL.copy(mySLL)
newSLL.printSLL()
mySLL.update(2,'200')
mySLL.printSLL()
N7 = Node('100')
mySLL.insertAtStart(N7)
mySLL.printSLL()
N8 = Node('500')
mySLL.insertAtEnd(N8)
mySLL.printSLL()
N9 = Node('1000')
mySLL.insert(5,N9)
mySLL.printSLL()
mySLL.deleteFirstNode()
mySLL.printSLL()
mySLL.deleteLastNode()
mySLL.printSLL()
mySLL.delete(6))
mySLL.printSLL()



