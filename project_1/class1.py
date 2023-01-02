#print and comment
print("hello") #this is a comment

#function definition
def my_function():
    """this is a doc string 
    this is too
    we can use multiple lines
    """
    #to see the doc string type print(my_function.__doc__) in the console
    print("ciao")

#calls the function
my_function()

#converts from decimal to binary
print(bin(42))
print(0b101010)

#adjusts the precision
from decimal import Decimal
a = 20
b = 13
c = a/b
d = Decimal(a/b)
print(c)
print(d)

#bitwise comparison
my_v1 = 4
my_v2 = 3
my_v3 = my_v1 & my_v2
print(f'my_v1 is {my_v1:08b}, my_v2 is {my_v2:08b}, then my_v3 is {my_v3:08b}')

#working with strings
a = "my first string"
print(a[3])
print(a)
#strings are immutable a[3]='h' does not work
a = a.replace ("first", "last")
print(a)

#formating
my_var = 54.6
a =  'my first number is {0: 5.5f}'.format(my_var)
print(a)
#or we can do
b =  f'my first number is {my_var: 5.5f}'
print(b)

#exercise
string_1 = 'abc'
string_2 = 'xyz'
s1 = string_1.replace(string_1[-1],string_2[-1])
s2 = string_2.replace(string_2[-1],string_1[-1])
print(s2+' '+s1)