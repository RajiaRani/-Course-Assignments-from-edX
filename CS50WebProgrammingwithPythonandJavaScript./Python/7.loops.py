#Apply simple for loop
for i in  [0,1,2,3,4,5,6,7]:
    print(i)

# But if we wanted to print like 100 numbers or 1,000 numbers,this is going to start to get tedious.
#So Python has a built-in function called range where I can say for i in range six to achieve exactly the same thing.

for j in range(10):
    print(j)

names = ["reet", "riya", "bujji", "chenchu", "jija", "harry", "geeta"]
for name in names:
    print(name)


#you can also looping the character
name = "Harry"
for character in name:
    print(character)