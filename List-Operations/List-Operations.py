'''

1.a)Create a list with any five cities of India.

'''

cities = ['hyderabad','bangalore','chennai','pune','mumbai']
print(cities)

print(cities[0])

print(cities[-1])

print(cities[2])

cities.append('kochi')

print(cities)

cities.insert(2,'amaravati')
print(cities)

print(cities.index('pune'))

states = ['Telanga','Andhra Pradesh','Maharastra']
#for ele in states:
#    cities.append(ele)
#cities.insert(-1,states)
cities.append(states)
cities.append(25)
print(cities)
del cities[4]
print(cities)
print(cities[6][0])
print(len(cities))
count = 0
for ele in cities:
    count += 1
print(count)
for ele in cities:
    print(type(ele))
print(cities.index('pune'))
states = ['Telanga','Andhra Pradesh','Maharastra']
#for ele in states:
#    cities.append(ele)
#cities.insert(-1,states)
cities.append(states)
cities.append(25)
print(cities)
#del cities(4)
for ele in cities:
    print(type(ele))

