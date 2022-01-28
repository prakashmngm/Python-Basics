'''
convertListToSLL(self, list)


mySLL = convertListToSLL( [1, 2,3,4] )

mySLL.reverse()

'''

class Node:
	def __init__(self,data):
		self.data = data
		self.nextPtr = None

class SLL:
	def __init__(self):
		self.head = None
	
	def printSLL(self):
		tempPtr = self.head
		while(tempPtr != None):
			print(str(tempPtr.data)+'->',end = '')
			tempPtr = tempPtr.nextPtr
	
	def append(self,nodeobj):
		if(self.head == None):
			self.head = nodeobj
		else:
			tempPtr = self.head
			while(tempPtr.nextPtr != None):
				tempPtr = tempPtr.nextPtr
			tempPtr.nextPtr = nodeobj

	# write a function to create a SLL from a given list

	def create_SLL_From_List(self,lst):
		for ele in lst:
			N1 = Node(ele)
			self.append(N1)
			
	def removeDuplicates(self):
	    if(self.head == None):
	        print('Empty Linked List')
	    elif(self.head.nextPtr == None):
	        print('Single Length Linked List')
	    else:
	        tempPtr1 = self.head
	        tempPtr2 = self.head.nextPtr
	        while(tempPtr2 != None):
	            if(tempPtr1.data == tempPtr2.data):
	                tempPtr2 = tempPtr2.nextPtr
	                tempPtr1.nextPtr = tempPtr2
	            else:
	                tempPtr1 = tempPtr1.nextPtr
	                tempPtr2 = tempPtr2.nextPtr
	                	# write a function to remove all the instances of a given element
	def removeAll(self,data):
	    while(self.head != None):
	        if(self.head.data == data):
	            while(self.head != None and self.head.data == data):
	                self.head = self.head.nextPtr
	        else:
	            ptr1 = self.head
	            ptr2 = self.head.nextPtr
	            while(ptr2 != None):
	                if(data == ptr2.data):
	                    ptr1.nextPtr = ptr2.nextPtr
	                    ptr2 = ptr2.nextPtr
	                else:
	                    ptr1 = ptr2
	                    ptr2 = ptr2.nextPtr
	            if(ptr2 == None):
	                break
	def merge(self,sll2):
	    P1 = self.head
	    P2 = sll2.head
	    while(P1 != None and P2 != None):
	        if(P1 != None and P2 != None and P1.data < P2.data):
	            while(P1 != None and P2 != None and P1.data < P2.data):
	                tmpP1 = P1
	                P1 = P1.nextPtr
	            if(P2 != None):
	                tmpP1.nextPtr = P2
	            while(P1 != None and P2 != None and P2.data <= P1.data):
	                tmpP2 = P2
	                P2 = P2.nextPtr
	            if(P1 != None):
	                tmpP2.nextPtr = P1
	        elif(P1 != None and P2 != None and P1.data == P2.data):
	            while(P1 != None and P2 != None and P1.data == P2.data):
	                tmpP1 = P1
	                P1 = P1.nextPtr
	            if(P2 != None):
	                tmpP1.nextPtr = P2
	        else:
	            while(P1 != None and P2 != None and P1.data > P2.data):
	                tmpP2 = P2
	                P2 = P2.nextPtr
	            if(P1 != None):
	                tmpP2.nextPtr = P1
	            while(P1 != None and P2 != None and P1.data <= P2.data):
	                tmpP1 = P1
	                P1 = P1.nextPtr
	            if(P2 != None):
	                tmpP1.nextPtr = P2
	def reverse1(self):
	    if(self.head == None):
	    	print('Empty Linked List')
	    else:
    		ptr1 = self.head
    		ptr2 = self.head.nextPtr
    		ptr1.nextPtr = None
    		while(ptr2 != None):
    		    self.head = ptr2
    		    ptr2 = ptr2.nextPtr
    		    self.head.nextPtr = ptr1
    		    ptr1 = self.head

#-----------------------------------------------------------------------------------
mySLL1 = SLL()
mySLL1.create_SLL_From_List([1,2,3,8,10])
mySLL2 = SLL()
mySLL2.create_SLL_From_List([9,10,11,12])

mySLL1.merge(mySLL2)
print()
mySLL1.printSLL()

