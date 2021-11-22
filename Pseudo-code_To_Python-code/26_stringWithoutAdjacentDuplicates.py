'''
Problem Statement : Remove the adjacent duplicates in the string
String : abbcdee
Output : acd

String : aaaaaaa
Output : a

String : abbacd
Output : cd

Pseudo Code:

Take the input string
lst = []
index = 1
Append lst with string[0]
In the loop : index < len(string)(7)
    Append lst with (string[index])
    if(  len(lst) > 1 AND lst[-1] == lst[-2]  )
        lst.pop(-1)
        lst.pop(-2)
    Index = index+1
Output = ‘’
For ele in lst:
    Add ele to output
Return output

'''
def stringWithoutAdjacentDuplicates(string):
    lst = []
    index = 1
    lst.append(string[0])
    while(index < len(string)):
        lst.append(string[index])
        if((len(lst) > 1) and (lst[-1] == lst[-2])):
            lst.pop(-1)
            lst.pop(-1)
        index = index+1
    output = ''
    for ele in lst:
        output = output+str(ele)
    return output
print(stringWithoutAdjacentDuplicates('abbacd'))

