# claculator project

# addition
def add(n1 , n2):
    return n1 + n2

# substract
def sub(n1 , n2):
    return n1 - n2

# multiplication
def mul(n1, n2):
    return n1 * n2

# divide
def divide(n1 , n2):
    return n1 / n2

# power
def power(n1 , n2):
    return n1 ** n2

operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : divide,
    "**" : power
}
def my_function(): # recursion function used to start with when you type 'n' with calculation
    num1 = float(input("enter the first number : "))
    for symbol in operations:
        print(symbol)
    should_continue = True
    while should_continue:
        operation_symbol = input("select the operation : ")
        num2 = float(input("enter the next number : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1,num2)
        print(f" \033[34m the operation between these two number {num1} {operation_symbol} {num2} = \033[35m{answer}")
        # \033[34m    added to change the color
        if input(f"type 'y' to continue calculating with {answer} or type 'n' to start new calculation: ") == "y":
            num1 = answer
        else:
            should_continue = False
            my_function()
my_function()