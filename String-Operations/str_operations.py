'''
Create a string variable.
str = “My name is Lokesh. My city name is Pune.”
Print it. Print its type.
'''

str = "My name is Lokesh. My city name is Pune."
print(type(str))

'''
Create a new string using 1st, 5th, 10th, 20th, 30th alphabets of above string.
Print it.
'''
new_str = ""
index = 0
while(index < 30):
    new_str = new_str+str[index]
    index = index+5
print(new_str)

'''
Make all alphabets in string lowercase.
Make all alphabets in string uppercase.
'''
upper_str = str.upper()
print(upper_str)
lower_str = str.lower()
print(lower_str)

'''
Print all the position of the alphabet ‘a’ in the given string.
'''

for index in range(len(str)):
    if(str[index] == 'a'):
        print(index)
'''
Guess the output
str = “My name is Lokesh. My city name is Pune.”
str.index(“z”)
str.find(“z”)

output : error:string not found
        -1
'''
#print(str.index("z"))
print(str.find("z"))

'''
Count the number of times sub-string “is” appears in the string.
'''
print(str.count("is"))
print(str.count("me"))
