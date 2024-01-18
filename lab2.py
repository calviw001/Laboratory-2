#lab2.py

# Starter code for lab 2 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.
# Please see the README in this repository for the requirements of this lab exercise

# Calvin Wong
# calviw8@uci.edu
# 36522374


def add(a, b):
    return  a + b


def sub(a, b):
    return  a - b


def div(a, b):
    try:
        quotient = a / b
    except ZeroDivisionError:
        return "Error! Division by 0 is undefined!"
    else:
        return quotient


def mul(a, b):
    return  a * b


def run():
    a = input("Enter left operand: ")
    b = input("Enter right operand: ")
    operator = input("What type of calculation would you like to perform (+, -, x, /)? ")
    
    r = 0

    try:
        a = int(a)
        b = int(b)
    except ValueError:
        print("Error! Only enter integer values!")
    else:
        if operator == "+":
            r = add(int(a),int(b))
        elif operator == "-":
            r = sub(int(a),int(b))
        elif operator == "x":
            r = mul(int(a),int(b))
        elif operator == "/":
            r = div(int(a),int(b))
        else:
            r = "Unable to perform the desired calculation, please try again."
        
        print(r)
    
    finally:
        if input("Run another calculation (y/n)? ") == "y":
            run()


if __name__ == "__main__":
    print("Welcome to PyCalc!")
    run()
