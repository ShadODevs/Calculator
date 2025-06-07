def calculator():
    print("Calculadora: Suma y Resta")
    print("Escribe una operación como: 5 + 3 o 10 - 2")

    while True:
        operation = input(">>> ").strip()

        if operation.lower() in ["exit", "quit", "q"]:
            print("Goodbye!")
            break

        try:
            # Remove spaces and detect operator
            if "+" in operation:
                parts = operation.split("+")
                result = float(parts[0]) + float(parts[1])
            elif "-" in operation:
                parts = operation.split("-")
                result = float(parts[0]) - float(parts[1])
            else:
                print("Only addition (+) and subtraction (-) are allowed.")
                continue

            print("Result:", result)
        except:
            print("Invalid operation. Please use valid numbers and operators.")


# Run the calculator
calculator()
