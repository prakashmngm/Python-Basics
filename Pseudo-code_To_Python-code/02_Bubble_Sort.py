'''
>Given pseudo code, convert it into Python code
1.)Consider list of integers
2.)Let N = total no. of integers in list.

3)Loop : from i = 0 till (N-1) , i<N, i = i+1
3.a) Loop : from j = 0 till (N-2), j<N-1, j = j + 1
3.b) if list[j] > list[j+1] then swap( list[j], list[j+1] )

4)Print the list.

'''


def Bubble_Sort(lst):
    length = len(lst)
    for index1 in range(length):
            for index2 in range(length-1):
                if(lst[index2] > lst[index2+1]):
                    temp = lst[index2]
                    lst[index2] = lst[index2+1]
                    lst[index2+1] = temp
    return lst
    
print(Bubble_Sort([-1,0,3,2]))
        
        
