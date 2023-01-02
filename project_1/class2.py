#conditional if
my_variable_condition = 4
my_variable = "Hi" if my_variable_condition == 5 else "goodbye"
print(my_variable)


#loop for
numbers = [1,2,3,4,5]
sum = 0
for value in numbers:
    sum+=value
print(sum)

#my_string = input("please input a string: ")
my_string = 'test'
print ("Received input is : ", my_string)
sum = 0

#exercise
for _ in my_string:
    sum+=1
print(f'The string is {sum} characters long')

#range
for count in range(0,10,2):
    print(count)

#exercise
for count in range(15,27+1):
    if (count%7==0) and (count%5==0):
        print(count)
#or:
# for count in range(1500,2701,5):
#     if (count%7==0):
#         print(count)

#while and break
var = True
while var:
    print('Hi')
    break

#continue skips the rest of the loop
numbers = [6,5,3,8,2,4,6]
for value in numbers:
    if value==8:
        continue
    print(value)

#enumerate
my_list = [6,5,3,8,2,4,6]
for position, value in enumerate(my_list):
    print(f'the position {position} has value {value}')
    
#exercise
print('with for')
for value in range(1,11):
    if value==3 or value==6:
        continue
    print(value)

print('with while')
value = 0;
while value<10:
    value += 1
    if value==3 or value==6:
        continue
    print(value)
    
#lists
my_list = [5,6,7,8,'ciao',[1,2,3]]
another_list = list()
another_list.append('ciao')
another_list.append(23)
print(another_list)
print(my_list)

#exercise
a = [10,20,30,20,10,50,60,40,80,50,40]
b = []
for val in a: #for catches each element in a
    if val in b: #if catches all elements in b
        continue
    else:
        b.append(val)
print(b)

#dictionary
mydictionary = {}
mydictionary["name"]="Marcello"
mydictionary["age"]=21

for key, value in mydictionary.items():
    print(key)
    print(value)
    
print(mydictionary.keys())
#calling like an array of index "key"
print(mydictionary["age"])

#exercise
d1 = {'a':100,'b':200}
d2 = {'x':300,'y':200}
#option 1
# for dic_key, dic_value in d2.items():
#     d1[dic_key] = dic_value
#option 2
d1.update(d2)
#option 3
# d1 = {**d1, **d2}
#option 4 (just to python version above 3.9)
# d1 = d1|d2
print(d1)

#list comprehension
"""list comprehension is a list created based on
another list or iterator"""
mylist = [10,19,30,21,10,50,65,40,83,50,40]
#decrease one on every element
newlist = [i-1 for i in mylist]
print(newlist)
#catches the even numbers
newlist = [i for i in mylist if i%2==0]
print(newlist)

#to see the python version and folder
import sys
print(sys.version)
print(sys.executable)



