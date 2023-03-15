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
        num1 = float(token[1])
        if len(token) == 3: 
            num2 = float(token[2])
        if function_name == "+":
            print(add(num1, num2))
        if function_name == "-":
            print(subtract(num1, num2))
        if function_name == "*":
            print(multiply(num1, num2))
        if function_name == "/":
            print(divide(num1, num2))
        if function_name == "square":
            print(square(num1))
        if function_name == "cube":
            print(cube(num1))
        if function_name == "pow":
            print(power(num1, num2))
        if function_name == "mod":
            print(mod(num1, num2))

