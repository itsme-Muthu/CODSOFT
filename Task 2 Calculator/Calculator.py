# returns addition of 2 numbers
def add(n1,n2):
    print(n1,"+",n2,"=",n1+n2)

# returns subtraction of 2 numbers
def sub(n1,n2):
    print(n1,"-",n2,"=",n1-n2)

# returns multiplication of 2 numbers
def mul(n1,n2):
    print(n1,"*",n2,"=",n1*n2)

# returns division of 2 numbers
def div(n1,n2):
    print(n1,"/",n2,"=",n1/n2)

# returns the remainder between 2 numbers
def rem(n1,n2):
    print(n1,"%",n2,"=",n1%n2)

# returns the power of 2 numbers
def power(n1,n2):
    print(n1,"^",n2,"=",n1**n2)

# prints the available operations
def choicesAvailable():
    print("----------------------------------------")
    print("Basic Calculator")
    print("Operation Available :")
    print("----------------------------------------")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Find remainder")
    print("6. Power")
    print("----------------------------------------")

# gets 2 numbers as input to perform the arithmetic operations
def Calculator():
    
    print("----------------------------------------")
    while True:
        choicesAvailable()
        choice = int(input("Enter the choice: "))
        print("----------------------------------------")
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print("----------------------------------------")

        if choice==1:
            add(num1,num2)
        elif choice==2:
            sub(num1,num2)
        elif choice==3:
            mul(num1,num2)
        elif choice==4:
            div(num1,num2)
        elif choice==5:
            rem(num1,num2)
        elif choice==6:
            power(num1,num2)
        
        resume = input("Do you want to perform Further calculation (Y/N) ")
        if resume in "nN":
            print("Thank you !")
            print("X-X-X- Exited from the calculator! -X-X-X")
            break
        elif resume not in "yYnN":
            print("Enter a valid choice: (Y/N) ")

Calculator()     


        
    

    