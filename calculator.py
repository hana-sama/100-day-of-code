from art import logo

def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide 
}


def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    for key in operations.keys():
        print(key)

    should_continue = True
    while should_continue:
        num2 = float(input("What's the next number?: "))
        operation_symbol = input("Pick an operation from the list above: ")
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        more_calculation = input(f"Type 'y' to continue calculation with {answer}, type 'n' to start a new calculation, type 'e' to exit: ").lower()

        if  more_calculation == 'y':
            num1 = answer
        elif more_calculation == 'n':
            should_continue = False
            calculator()
        elif more_calculation == 'e':
            should_continue = False


calculator()