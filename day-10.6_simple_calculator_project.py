# claculator project one time calculation

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
num1 = float(input("enter the first number : "))
for symbol in operations:
    print(symbol)
operation_symbol = input("select the operation from above line : ")
num2 = float(input("enter the second number : "))

calculation_function = operations[operation_symbol]
answer = calculation_function(num1,num2)
print(f" \033[34m the operation between these two number {num1} {operation_symbol} {num2} = \033[31m{answer}")
# \033[34m    added to change the color