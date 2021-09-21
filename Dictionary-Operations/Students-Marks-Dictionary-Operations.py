'''

create a dictionary with 5 student names and marks

'''

Students_Marks = {'ram':35,'lokesh':95,'satish':58,'surya':72,'arya':13}

print(Students_Marks)

print(type(Students_Marks))

print(Students_Marks['surya'])

Students_Marks['arya'] = 31

print(Students_Marks['arya'])

Students_Marks['geeta'] = 85

Students_Marks['anusha'] = 72

print(Students_Marks)

#Students = Students_Marks.keys()

#print(type(Students_Marks.keys()))

#print(Students_Marks.keys())

#print(Students[1])

Students = list(Students_Marks.keys())

print(type(Students))

print(sorted(Students))

Marks = list(Students_Marks.values())

print(Students_Marks.values())

print(type(Students_Marks.values()))

print(type(Marks))

Marks.sort()

print(Marks)

print(len(Students_Marks))

print(max(Students_Marks))

print(min(Students_Marks))

