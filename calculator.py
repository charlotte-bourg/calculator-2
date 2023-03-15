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
        if token[0] == "+":
            print(add(float(token[1]), float(token[2])))
    

