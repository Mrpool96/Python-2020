#Program for Calculator

def Add(a,b):
    return (a+b)   #Addition

def Sub(a,b):
    return (a-b)   #Substraction

def Mul(a,b):
    return (a*b)   #Multiplication

def Div(a,b):
    return (a/b)   #Division

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

while True:
    choice = input("Enter a Choice:- (1,2,3,4):-")  #Taking Input From User
    if choice in('1','2','3','4'):
        num1 = float(input("Enter The Number:-"))
        num2 = float(input("Enter The Second Number:-"))
    if choice == '1':
        print(num1, "+", num2, "=", Add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", Sub(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", Mul(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", Div(num1, num2))
    break
else:
    print("Invalid Input")