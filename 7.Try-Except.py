try: 
    num1 = int(input("ENTER NUMBER: "))
    num2 = int(input("ENTER NUMBER: "))
    division = num1/num2
    print("QUOTIENT: ", division)

except ZeroDivisionError:
    print("\nYou can't divide a number by zero!!!!!!")

except: 
    print("PROBLEM!!!!!")