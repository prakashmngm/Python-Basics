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
            print(tempPtr.data)
            tempPtr = tempPtr.nextPtr
            
# --------------------------------------------

N1 = Node('suresh')
N2 = Node('lokesh')
N3 = Node('prakash')

N1.printData()
N2.printData()
N3.printData()

mySLL = SLL()
mySLL.printSLL()
mySLL.append(N1)
mySLL.printSLL()
mySLL.append(N2)
mySLL.printSLL()
mySLL.append(N3)
mySLL.printSLL()
