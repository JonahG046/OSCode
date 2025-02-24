ArrayMemory = [None] * 10000

def store_equation_result(equation, index):
    parts = equation.split()
    
    # Check if the equation starts with "y ="
    if len(parts) < 4 or parts[0] != 'y' or parts[1] != '=':
        return "Invalid equation"

    operator = parts[2]  # The third element should be the operator
    try:
        number1 = int(parts[3])  # The fourth element should be the first number
        number2 = int(parts[4])  # The fifth element should be the second number
    except (ValueError, IndexError):
        return "Invalid numbers in equation"

    # Check for valid operators and perform the operation
    if operator == '+':
        operation = f"add {number1} {number2}"
    elif operator == '-':
        operation = f"sub {number1} {number2}"
    elif operator == '*':
        operation = f"mult {number1} {number2}"
    elif operator == '/':
        operation = f"div {number1} {number2}"
    else:
        return "Invalid operator"

    # Store result in the array
    ArrayMemory[index] = operation
    return operation


def perform_stored_operation(index):
    if ArrayMemory[index] is None:
        return "No result found at index"
    
    operation = ArrayMemory[index].split()
    operator = operation[0]
    number1 = int(operation[1])
    number2 = int(operation[2])
    
    if operator == 'add':
        return number1 + number2
    elif operator == 'sub':
        return number1 - number2
    elif operator == 'mult':
        return number1 * number2
    elif operator == 'div':
        return number1 / number2
    else:
        return "Invalid operation"

# Example usage
result1 = store_equation_result("y = - 7 5", 0)
print(ArrayMemory[0])  # Expected output: "sub 7 5"
print(result1)  # Expected output: "sub 7 5"

result2 = store_equation_result("y = * 18 16", 1)
print(ArrayMemory[1])  # Expected output: "mult 18 16"
print(result2)  # Expected output: "mult 18 16"

# Perform stored operations
print(perform_stored_operation(0))  # Expected output: 2 (7 - 5)
print(perform_stored_operation(1))  # Expected output: 288 (18 * 16)
