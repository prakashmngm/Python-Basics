'''

str = "My name is Lokesh. My city name is Pune."

Count the total no. of alphabets in string.
Replace the word “is” by “was”.
Find the no. of words in a given sentence.
Find no. of sentences in a given paragraph.

'''

'''
Count the total no. of alphabets in string.
'''

str = "My name is Lokesh. My city name is Pune."
count = 0
for char in str:
    if(char.isalpha()):
        count = count+1
print(count)

'''
Replace the word “is” by “was”.
'''
print(str.replace('is','was'))

'''
Find the no. of words in a given sentence.
'''
str_list = str.split()
print(len(str_list))

'''
Find no. of sentences in a given paragraph.
'''
str_para = str.split('.')
print(str_para)
print(len(str_para)-1)

