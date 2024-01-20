while(True):
    print("Please Select your option:")
    print("1. for Addition:")
    print("2. for Subtraction:")
    print("3. for Multiplication:")
    print("4. for Division:")
    print("5. for Modulus:")
    print("6. to Exit:")
    operation = int(input("> "))
    if(operation == 1):
        var_1 = int(input("Enter variable 1: "))
        var_2 = int(input("Enter variable 2: "))
        print(f"Addition: {var_1 + var_2}\n")
    elif(operation == 2):
        var_1 = int(input("Enter variable 1: "))
        var_2 = int(input("Enter variable 2: "))
        print(f"Subtraction: {var_1 - var_2}\n")
    elif(operation == 3):
        var_1 = int(input("Enter variable 1: "))
        var_2 = int(input("Enter variable 2: "))
        print(f"Multiplication: {var_1 * var_2}\n")
    elif(operation == 4):
        var_1 = int(input("Enter variable 1: "))
        var_2 = int(input("Enter variable 2: "))
        print(f"Division: {var_1 / var_2}\n")
    elif(operation == 5):
        var_1 = int(input("Enter variable 1: "))
        var_2 = int(input("Enter variable 2: "))
        print(f"Modulus: {var_1 % var_2}\n")
    elif(operation == 6):
        break
    else:
        print("Invalid Input\n")
        continue