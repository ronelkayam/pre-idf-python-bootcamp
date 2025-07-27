"""
this script is example using in round function
round gets 2 arguments
round(first,second)
first-the number we work on him
second- num of numbers after point
*if i use in round only 1 argument the result will be in integer kind

if number after point >=5 the round will be upwards
if number after point <5 the round will be downwards
also if we used in 0 in second argument
"""
#version 1
print(round(1.222223,2))

#version 2
newNum=round(1.2333443443,3)
print(newNum)

#version 3
result=10/3
print(round(result,2))

#version 4
print(round(10/3,2))

#version 5
roundNum=3
print(round(1.2222,roundNum))

#version 6
#return integer value
print(round(4/3))