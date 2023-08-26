# The different mathmatical operations
operators = {'+', '-', '*', '/'}

#Defining the mathmatical operations
def addition(number_one, number_two):
    return number_one + number_two

def subtraction(number_one, number_two):
    return number_one - number_two

def multiplication(number_one, number_two):
    return number_one * number_two

def division(number_one, number_two):
    if number_two == 0:
        # This send an err message saying that dividing by zero is not allowed
        raise ValueError("Division by zero is not allowed")
    return number_one / number_two
# This function does operations on numbers, handling division by zero errors.
def performTheOperations(operations, numbers):
    result = numbers[0]
    for i in range(len(operations)):
        # The different operations
        if operations[i] == '+':
            result = addition(result, numbers[i + 1])
        elif operations[i] == '-':
            result = subtraction(result, numbers[i + 1])
        elif operations[i] == '*':
            result = multiplication(result, numbers[i + 1])
        elif operations[i] == '/':
            try:
                result = division(result, numbers[i + 1])
           # If their is a err it will send to the console 'ERROR' and return no solution to the problem
            except ValueError as ERROR:
                print(ERROR)
                return None
            # This makes sure that the solution is sent to the console
    return result

while True:
    # This is shown to the user to enter the equation
    expression = input("Enter Equation: ")
    components = expression.split()
# if their is a invalid input it will send a message saying that its a invalid format and alternate the numbers and operators
    if len(components) % 2 == 0:
        print("Invalid input format, provide alternating numbers and operators.")
        continue

    numbers = [float(components[i]) for i in range(0, len(components), 2)]
    operations = [components[i] for i in range(1, len(components), 2)]
# this shows that the solution is solved and it will print the result if solution is zero then it will return nothing
    result = performTheOperations(operations, numbers)
    if result is not None:
        print("Result:", result)
# This last part says in the console if you would like to conitnue tyep YES else type NO to stop 
    to_continue = input("Would you like to do another calculation? (YES or NO): ").upper()
    if to_continue != "YES":
        break