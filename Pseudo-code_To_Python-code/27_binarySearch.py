'''
Problem Statement : Implement the standard binary search algorithm.

Sorted Input :  
A    E    I   O    U   W
0     1   2   3     4   5

Search element :  W

Pseudo Code:
Take the input sorted list , search element (ele)
start = 0
End = len(list)-1
Mid = Floor( (start+end)/2 )
In the loop : 
        if( start==end  OR start == mid OR end == mid)
            break
        if( ele > mid):
            start = mid
            Mid = floor((start+end)/2)
        elif(ele < mid):
            End = mid
            Mid = floor((start+end)/2)
        Else:
            Return mid
	
if( start == ele)
    Return start
elif(end == ele)
    Return end
Else
    Return -1
'''
def binarySearch(lst,ele):
    start = 0
    end = len(lst)-1
    mid = (start+end)//2
    while(True):
        if(start == end or start == mid or end == mid):
            break
        elif(ele > lst[mid]):
            start = mid
            mid = (start+end)//2
        elif(ele < lst[mid]):
            end = mid
            mid = (start+end)//2
        else:
            return mid
    if(lst[start] == ele):
        return start
    elif(lst[end] == ele):
        return end
    else:
        return -1

print(binarySearch(['janu','meena','raghu','rama','shanu'],'jhanu'))
