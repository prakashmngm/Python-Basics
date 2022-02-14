'''
Splitting of Linked List : 


def splitLL( self, k) : 

11 -> 12 -> 13 -> 14 -> 15 -> 16,  k = 4

[   L1,  L2,  L3,  L4   ]

[  11->12 , 13, 14, 15-> 16 ]

arrayLLHeads = []
arrayLLHeads.append(head1)
arrayLLHeads.append(head2)
arrayLLHeads.append(head3)


------ USER Code -------
array = myLL.splitLL(k)

for head in arrayLLHeads : 
        arrayLLHeads.printLL()


SubProblem#1 : 

def( N, k) : 
N = 10, k = 4
Expected Output : [  3, 2, 2, 3   ]


'''

def summation(lst):
    summ = 0
    for ele in lst:
        summ = summ+ele
    return summ

def split(num,parts):
    quotient = num//parts
    lst = []
    if(num%parts == 0):
        for index in range(parts):
            lst.append(quotient)
        return lst
    else:
        for index in range(parts):
            lst.append(quotient)
        for index in range(parts):
            lst[index] = lst[index]+1
            if(summation(lst) == num):
                break
        return lst

split(10,3)

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
		print()
	
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

	def length(self):
	    tempPtr = self.head
	    count = 0
	    while(tempPtr != None):
	        count = count+1
	        tempPtr = tempPtr.nextPtr
	    return count

	def splitLL(self,k,SLL_HeadPtrs):
	    length_of_splitLLs = split(self.length(),k)
	    print(length_of_splitLLs)
	    tempPtr = self.head
	    iter_no = 0
	    for index in length_of_splitLLs:
	        SLL_HeadPtrs[iter_no].head = tempPtr
	        start = 0
	        while(start < index):
	            endPtr = tempPtr
	            tempPtr = tempPtr.nextPtr
	            start = start+1
	        endPtr.nextPtr = None
	        iter_no = iter_no+1
#--------------------------------------------------------------------
mySLL = SLL()
mySLL.create_SLL_From_List([11,12,13,14,15,16])
SLL_HeadPtrs = []
parts = 4

for index in range(parts):
    newSLL = SLL()
    SLL_HeadPtrs.append(newSLL)
    
mySLL.splitLL(parts,SLL_HeadPtrs)

for index in range(parts):
    SLL_HeadPtrs[index].printSLL()

