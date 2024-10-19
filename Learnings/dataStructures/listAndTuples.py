# basic understanding of lists and tuples first 

# lists are mutable as their values can be changed, and we use [] to declare them, it's like a array in javascript,

list_example = ['dc', 'marvel','x-men']

# tuples are immutable , we can't change their vales, and () is used to declare them , 
tuples_example_cordinates = (99.89, 78.88)

#? SPAM for list operations - sort, pop, append, modify

#sort 
numbers = [1,5,6,2,8,9,3,5,7]
numbers.sort()
print(numbers)

#pop -  removes the last item in the list
heros = ['flash', 'batman', 'supe', 'martian']
heros.pop()
print(heros)

# apped - adds a item at the end 
heros.append('shazam')
print(heros)

# modify - modify the items in the list 
heros[2] = 'superman'
print(heros)


#? Key differences between lists and tuples
# one of the key difference between lists and tuples is that lists are mutable and are used where you need to make lot of changes to the lists elements, and while tuples are used when you have to keep the data constant . i.e when using cordinates etc

# common list and tuple operations 

#finding length 
print(len(numbers))

#indexing 
print(heros[1])

# slicing  - prints the numbers between the mentioned indexes
print(numbers[2:6])

# concatenation 
listOne = [1,2] + [44, 66]
tupleOne = (2,3) + (31, 32)
print(f"this is list concatenation: {listOne}, and this is the tuple concatenation: {tupleOne}")
