'''
Students & Ice-Creams

Queue :  VVBB    
         ↑ 
Stack :  VBVV
         ↑            

1. Take the input queue and stack
2. In the loop :  len(queue) > 0
			ele = queue[0]
			if( ele[0] == stack_top)
				delete 1st element from the stack
				Delete 1st element from the queue
            else:
                if(len(ele) == 1):
                    remove 1st ele of the queue
                    append ele to the queue as ele+'#'
                else
                    return len(queue)
3. return len(queue)

'''

def student_Ice_Creams_Match(queue,stack):
    while(len(queue) > 0):
        ele = queue[0]
        if(ele[0] == stack[0]):
            stack.pop(0)
            queue.pop(0)
        else:
            if(len(ele) == 1):
                queue.pop(0)
                queue.append(ele+'#')
            else:
                return len(queue)
    return len(queue)
print(student_Ice_Creams_Match(['v','v','b','b'],['v','b','v','v']))
        
