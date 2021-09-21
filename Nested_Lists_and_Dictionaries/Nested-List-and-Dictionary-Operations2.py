'''

**(1) Nested List & Nested Dict - Exercises

'''

myList = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

myList.insert(1,'p')

print(myList)

myList[3].insert(1,'q')

print(myList)

myList[3][2].insert(1,'r')

print(myList)

myList[3][2][3].insert(1,'s')

print(myList)

#del myList[2]

myList.pop(2)

print(myList)

#del myList[2][2]

myList[2].pop(2)

print(myList)

