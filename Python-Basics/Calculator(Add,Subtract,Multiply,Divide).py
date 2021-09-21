'''

 (2.a) Take two numbers from user and print its addition.
 
 (2.b)Expand above program to create a simple calculator.
Take two integers from the user and an operator.( +, -, *, / )

'''

num1 = float(input("please enter number1 :"))
num2 = float(input("please enter number2 :"))
operation = input("enter your operation :")
if(operation == '+'):
    print("Addition is :",num1+num2)
elif(operation == '-'):
    print("Subtraction is :",num1-num2)
elif(operation == '*'):
    print("Multiplication is :",num1*num2)
elif(operation == '/'):
    print("Division is :", num1/num2)
else:
    print("Please enter correct operation.")

