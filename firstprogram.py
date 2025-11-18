def calculator():
    print("Simple Calculator")
    print("Operations: +  -  *  /")
    print("Type 'exit' to quit.\n")

    while True:
        num1 = input("Enter first number: ")
        if num1.lower() == "exit":
            break

        num2 = input("Enter second number: ")
        if num2.lower() == "exit":
            break

        op = input("Enter operator (+, -, *, /): ")
        if op.lower() == "exit":
            break

        # Convert input to numbers
        num1 = float(num1)
        num2 = float(num2)

        # Perform calculation
        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                result = "Error! Division by zero."
            else:
                result = num1 / num2
        else:
            result = "Invalid operator!"

        print("Result:", result, "\n")

# Run calculator
calculator()
