# if you know that all the elements are going to be unique,then you can use a set, which is another Python data
# structure that works in similar ways.The syntax is slightly different.

#Create an empty set
s = set()

#Add elements to the set
#No element ever appears twice in the set,
#following with the mathematical definition of a set where no element ever appears more than once inside of a set.
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(3)
s.add(4)
print(s)

#Remove the elements from the sets
s.remove(4)
print(s)

#Using len() function to calculate the length of the set
print(f"The set has {len(s)} elements inside it.")
