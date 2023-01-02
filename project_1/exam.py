#the class construction
class Calculator:
   def add(self, x, y):
       return x + y
    
   def subtract(self, x, y):
       return x - y

   def multiply(self, x, y):
       return x * y

   def divide(self, x, y):        
       if (y == 0):
           a = "not possible. You cannot divide by zero!"
       else:
           a = x / y  
       return a

#function to ask for values
def asking():
    #Parameters
    print("Select the arithmetic operation:")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 Division")
    print("0 Exit")
    
    a = input("Please enter your option:")
    if a == '0':
        raise SystemExit
        
    #exceptions
    try:
        z = int(a)
        
        if((z!=4) & (z!=3) & (z!=2) & (z!=1)):
            raise Exception ('Invalid!')
            a = 'error'
    except ValueError:
        print("it was not a numeric value")
        a = 'error'
    except Exception as e:
        print(e)
        a = 'error'
    else:
        print("good choice!")

        #exceptions
        try:
            x = float(input("Please enter first number:"))
        except ValueError:
            print("it was not a numeric value")
            a = 'error'
        except Exception as e:
            print(e)
            a = 'error'
        else:
            print("good choice!")
        
            #exceptions
            try:
                y = float(input("Please enter second number:"))
            except ValueError:
                print("it was not a numeric value")
                a = 'error'
            except Exception as e:
                print(e)
                a = 'error'
            else:
                print("good choice!")

    #calculations
    calc = Calculator()
    if a == '1':
        display = calc.add(x, y)
        
    elif a == '2':
        display = calc.subtract(x, y)
        
    elif a == '3':
        display = calc.multiply(x, y)
        
    elif a == '4':
        display = calc.divide(x, y)
    
    else:
        display = "not possible!"
    
    print(f"\nThe result of your operation is {display}\n")

#main pipeline
import time
while True:
    asking()
    time.sleep(2)

