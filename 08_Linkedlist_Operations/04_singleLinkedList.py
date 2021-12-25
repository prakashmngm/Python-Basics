class Node:
    def __init__(self,data):
        self.data = data
        self.nextPtr = None
    def printNode(self):
        print(self.data)

N1 = Node(5)
#N1.printNode()
N2 = Node(6)
#N2.printNode()
N3 = Node(7)
#N3.printNode()
N4 = Node(8)

class SLL:
    def __init__(self):
        self.head = None
    def printLL(self):
        print('printing linedlist')
        tempNode = self.head
        while(tempNode != None):
            print(tempNode.data)
            tempNode = tempNode.nextPtr
    def append(self,nodeobj):
        if(self.head == None):
            # Linkedlist is empty
            self.head = nodeobj
        else:
            tempNode = self.head
            while(True):
                if(tempNode.nextPtr == None):
                    # we have reached the last node of the linked list
                    tempNode.nextPtr = nodeobj
                    break
                else:
                    tempNode = tempNode.nextPtr

mySLL = SLL()
mySLL.append(N1)
mySLL.printLL()
mySLL.append(N2)
mySLL.printLL()
mySLL.append(N3)
mySLL.printLL()
mySLL.append(N4)
mySLL.printLL()
