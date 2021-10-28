'''
Given one input sentence, find the length of the longest and the shortest word in it.

Eg : ‘ ’
          ↑
Index = 0
longest = 0
shortest = 0
count = 0

Pseudo Code :


1)Take the input sentence
index = 0
count = 0
2)In the loop : (index < len(sentence) AND sentence[index] != ‘ ‘)
		 count = count+1
		 index = index+1
longest = count
shortest = count
'''


def longest_shortest(string):
    index = 0
    count = 0
    while(index < len(string) and string[index] != ' '):
        count = count+1
        index = index+1
    longest = count
    shortest = count
    
    '''
    3)In the loop :  (index < len(sentence) AND sentence[index] == ‘ ‘)
    		  index = index+1
    '''
    while(index < len(string) and string[index] == ' '):
        index = index+1
    
    '''
    4)In the loop : index < len(sentence)(1)
    		count = 0
        In the loop : (index < len(sentence) AND sentence[index] != ‘ ‘ )
        	if(sentence[index].isAlpha()):
        		count = count+1
        	index = index+1
        if(count > longest)
        	   longest = count
        if(count < shortest)
        	   shortest = count
         In the loop :  (index < len(sentence) AND sentence[index] == ‘ ‘)
        		 	    index = index+1
    Return longest,shortest
    '''
    while(index < len(string)):
        count = 0
        while(index < len(string) and string[index] != ' '):
            if(string[index].isalpha()):
                count = count+1
            index = index+1
        if(count > longest):
            longest = count
        if(count < shortest):
            shortest = count
        while(index < len(string) and string[index] == ' '):
            index = index+1
    return list((longest,shortest))
    
print(longest_shortest('My name is surya@!123'))
        
