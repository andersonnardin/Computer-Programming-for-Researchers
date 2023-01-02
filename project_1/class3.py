#functions
def myfirstfunction (x, y):
    mysum = x+y
    print("hello")
    return mysum
value1 = 4
value2 = 5
output = myfirstfunction(value1,value2)
print(f'this is what my function returns {output}')

#exercise
def myfunction (list1):
    """
    help goes here
    """
    sum = 0
    for element in list1:
        sum += element
    return sum
list1 = [1,2,3,4]
output = myfunction(list1)
print(f'this is the return: {output}')

#to show the help of the function
help(myfunction)


#exercise
def myfunction2 (name, surname, year, city):
    result = f'1-{name} {surname} was born in {year} in {city}'
    return result
output = myfunction2('Marcello','Goccia',1996,'Wellington')
print(output)

"""
remark: a variable created out of any function is global 
and accessible by any function
"""

#exercise
def myfunction3 (*args):
    name, surname, year, city = args
    result = f'1-{name} {surname} was born in {year} in {city}'
    return result
output = myfunction3('Marcello',"Goccia",1996,"Genova")
print(output)

def myfunction4 (**kwargs):
    name = kwargs['name']
    surname = kwargs['surname']
    year = kwargs['year_birth']
    city = kwargs['city_birth']
    result = f"3-{name} {surname} was born in {year} in {city}"
    return result
dictionary = {'name':'Marcello', 'surname':'Goccia', 'year_birth':1996, 'city_birth':'Pisa'}
output = myfunction4(**dictionary)
print(output)

#lambda functions
multiplier = lambda a,b: a*b
output=multiplier(4,5)
print(output)

comparison = lambda a,b,c:a if b>c else c
output=comparison(4,8,7)
print(output)

print((lambda a,b:a*b)(4,5))

#functions are objects
def first(msg):
    print(msg)
first('hello')
second = first
second('hello')

def inc(x):
    return x + 1
def dec(x):
    return x - 1
def operate(func, x):
    result = func(x)
    return result
print(operate(inc,3))
print(operate(dec,3))

def is_called():
    def is_returned():
        print("Hello")
    return is_returned
new = is_called()
#when I call "new" actually I am calling "is_returned"
new()

#decorators
def smart_divide(func):
    def inner(a, b):
        print("I am going to divide", a, "and", b)
        if b == 0:
            print("Whoops! cannot divide")
            return
        return func(a, b)
    return inner

@smart_divide
def divide(a, b):
    print(a/b)
 
#when I call "divide" actually I am calling "inner"
#eventually "inner" uses the function "divide" calling by "func"
print(divide(2,5))
print(divide(2,0))

def function_1 (myinputfunction):
    def function_2():
        print("decoration")
        myinputfunction()
    return function_2

@function_1
def function_3():
    print("main aim of this funtion")

#when I call "function_3" actually I am calling "function_2"
print(function_3())

#exercise
with open('reading_from_file.txt','r') as file:
    out = file.readlines()
    n_python = 0
    n_matlab = 0
    for line in out:
        if 'python' in line:
            n_python += 1
        elif 'matlab' in line :
            n_matlab += 1
print(f"there are {n_python} lines written python")
print(f"there are {n_matlab} lines written matlab")
