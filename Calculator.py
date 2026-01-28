print("calculator program")

try:
    eleccion = input("choose 1 of the following options\n1. addition(+)\n2. substraction(-)\n3. multiplication(*)\n4. division(/)")
    num1 = int(input("give me a number: "))
    num2 = int(input("give me another number: "))


    if eleccion == '1':
        print(f"The result is: {num1 + num2}")
    elif eleccion == '2':
        print(f"The result is: {num1 - num2}")
    elif eleccion == '3':
        print(f"The result is :{num1 * num2}")
    elif eleccion == '4':
        if num2 == '0':
            print(f"You can't divide by zero")    
        else:
            print(f"The result is: {num1 / num2}")
    else:
        print("you can only choose the options above")

except ValueError as e:
    print(f"wrong value entered")

finally:
    print("...")