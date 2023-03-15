"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )

exit_condition_not_reached = True
while exit_condition_not_reached:
    expression = input("> ")
    if expression == 'q':
        print("Exiting calculator")
        exit_condition_not_reached = False
        break
    else:
        token = expression.split(' ')
        function_name = token[0]
        try:
            num1 = float(token[1])
        except ValueError:
            print("Please enter numerical value.")
            continue
        if function_name == "square":
            print(square(num1))
        elif function_name == "cube":
            print(cube(num1))
        else: 
            if len(token) < 3: 
                print("Invalid input: please enter the name of the operator followed by the correct number of values")
            else:
                try:
                    num2 = float(token[2])
                except ValueError:
                    print("Please enter numerical value.")
                    continue
                if function_name == "+":
                    print(add(num1, num2))
                elif function_name == "-":
                    print(subtract(num1, num2))
                elif function_name == "*":
                    print(multiply(num1, num2))
                elif function_name == "/":
                    print(divide(num1, num2))
                elif function_name == "pow":
                    print(power(num1, num2))
                elif function_name == "mod":
                    print(mod(num1, num2))
                else:
                    print("Enter one of the following operations: +, -, *, /, square, cube, pow, mod")

