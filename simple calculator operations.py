
number1 = int(input("enter the number 1: "))
number2 = int(input("enter the number 2:"))


choice = 0

while choice<5:
    print("1. Add")
    print("2. subtract")
    print("3. Multiply")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter the number:"))

    if choice == 1:
      sum = number1+number2
      print("sum:",sum)
    elif choice == 2:
      subtract = number1-number2
      print("subtract;",subtract)
    elif choice == 3:
      multiply = number1*number2
      print("multiply:",multiply)
    elif choice == 4:
      division = number1/number2
      print("Quotient:",division)
    elif choice == 5:
      print("Exiting calculator")
      break
    
    else:
      print ("Invalid Choice")

