print("""Choose what operation do you want to do:
    - Add
    - Subtract
    - Multiply
    - Divide
    - Stop
""")

while True:
    answer_option = input("Answer: ")

        if answer_option.lower() == "add"  or answer_option.lower() == "+":
        x = int(input("First number: "))
        y = int(input("Second number: "))
        print(f"{x} + {y} = ", x + y)
        break
    elif answer_option.lower() == "subtract" or answer_option.lower() == "-":
        b = int(input("First number: "))
        c = int(input("Second number: "))
        print(f"{b} - {c} = ", b - c)
        break
    elif answer_option.lower() == "multiply" or answer_option.lower() == "*":
        e = int(input("First number: "))
        o = int(input("Second number: "))
        print(f"{e} * {o} = ", e * o)
        break
    elif answer_option.lower() == "divide" or answer_option.lower() == "/":
        p = int(input("First number: "))
        t = int(input("Second number: "))
        print(f"{p} / {t} = ", p // t)
        break
    elif answer_option.lower() == "stop":
        break
    else:
        print("Incorrect answer")
