'''

create a dictionary with 5 student names and marks

'''

Students_Marks = {'ram':35,'lokesh':95,'satish':58,'surya':72,'arya':13}

Students_Marks['prakash'] = 95

print(Students_Marks)

#for k in Students_Marks.keys():
#    print(k)
    
#for v in Students_Marks.values():
#    print(v)

Max_marks = max(list(Students_Marks.values()))

for k,v in Students_Marks.items():
    if(v == Max_marks):
        print("Student "+k+" got the maximum marks")
        
Min_marks = min(list(Students_Marks.values()))

for k,v in Students_Marks.items():
    if(v == Min_marks):
        print("Student "+k+" got the minimum marks")
        
print(Students_Marks.items())
    
print(type(Students_Marks.items()))

