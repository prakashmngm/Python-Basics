'''
Mountain Peak
Consider these list of numbers : 
3, 5, 7, 20, 30, 55, 100, 97, 90, 35, 1

Given such a list of nos, find the index of the peak of the mountain.
No inbuilt functions.
3  5  7  9   11   15   25   55   33  22   11
0  1  2   3    4    5     6     7    8    9     10
                                 ↑
Pseudo Code :
Take the input list of numbers(lst)
Start = 0
End = len(lst)-1
Mid = (start+end)/2
In the loop : True
    if( start == end or mid == start or end == start)
        Break
    if( mid+1 > mid)
        Start = mid+1
    if( mid-1 > mid)
        End = mid-1
if(start > end)
    Return start
Else:
	Return end
'''

def mountainPeakofList(lst):
    start = 0
    end = len(lst)-1
    mid = (start+end)//2
    while(True):
        if(start == end or mid == start or mid == end):
            break
        if(lst[mid+1] > lst[mid]):
            start = mid
        if(lst[mid-1] > lst[mid]):
            end = mid-1
        if(lst[mid+1] < lst[mid] and lst[mid-1] < lst[mid]):
            return mid
        mid = (start+end)//2
    if(lst[start] > lst[end]):
        return start
    else:
        return end
        
print(mountainPeakofList([3,5]))
