'''
Given a SLL : 11-> 12 -> 13 -> 14 -> 15
                        0      1        2      3        4

Club even positioned nodes first, and then club odd positioned nodes.
Modify the input list itself.
def clubEvenOdd( self )
     …..
     …..
     Return head

Output : 11 -> 13  -> 15 ->  12 -> 14


                P1                    P3
          ↓             ↓      
Head -> 11 -> 12  -> 13 -> 14 -> 15
                         ↑
                       P2             



Ptr1 = self.head
SecondNode = Ptr1.next
 while(ptr1 != None and ptr1.nextPtr != None):
Ptr2 = ptr1.nextPtr
Ptr3 = ptr1.nextPtr.nextPtr
ptr1.nextPtr = ptr3
Ptr4 = ptr2.nextPtr.nextPtr

if(P3 != None)
Ptr2.nextPtr = ptr4 (P3.next)
Ptr1 = Ptr3
Ptr2 = Ptr4 (P3.next)


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
