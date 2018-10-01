import re

# Calculator program, be careful when using eval because people could insert valid syntax, like in SQL injection, when passing a username , could simply do SELECT * From Studenti
print("Amazing Calculator #1 Project")
print("Type quit to exit\n")
previous = 0
run = True


def performMath():
    global run                                # Run is a variable defined in the top level of our program, but run = false, which is further down the function,wont take effect because it cant access the top level run
    global previous
    equation = " "

    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))

    if equation == 'quit':
        run = False
        print("Calculator terminated")

    else:
        equation = re.sub('[A-Za-z,./:" "]', '', equation)
        if previous == 0:
            previous = eval(equation)           # Eval is a built-in function that will perform complex mathematical operations for us, at the cost of high risk if users input are not numbers, can crash.
        else:
            previous = eval(str(previous) + equation)  # So the reason you're concatenating strings in your project Is because you're doing additional stuff to the previous answer So if the person initially types in 3+4, you get 7. If they then type in +6, your stuff does "7" + "+6", which becomes "7+6", which, when fed into eval("7+6"), evaluates to 13


while run:
    performMath()
