'''


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
	def clubEvenOdd(self):
	    if(self.head != None):
	        ptr1 = self.head
	        secondNode = ptr1.nextPtr
	        while(ptr1 != None and ptr1.nextPtr != None):
	            ptr2 = ptr1.nextPtr
	            ptr3 = ptr1.nextPtr.nextPtr
	            ptr1.nextPtr = ptr3
	            if(ptr3 != None):
	                ptr2.nextPtr = ptr3.nextPtr
	                ptr1 = ptr3
	        if(ptr1 != None):
	            ptr1.nextPtr = secondNode
	        else:
	            ptr2.nextPtr = secondNode
#--------------------------------------------------------------------
mySLL = SLL()
mySLL.create_SLL_From_List([11,12,13,14,15,16])
mySLL.printSLL()
mySLL.clubEvenOdd()
print()
mySLL.printSLL()
