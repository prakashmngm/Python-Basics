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
mySLL = SLL()
mySLL.create_SLL_From_List([11,12,13,13,15])
mySLL.printSLL()
print()
mySLL.removeDuplicates()
print()
mySLL.printSLL()
print()
mySLL.reverse1()
print()
mySLL.printSLL()
mySLL.removeAll(11)
print()
mySLL.printSLL()
