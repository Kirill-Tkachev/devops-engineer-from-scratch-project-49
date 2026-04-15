import random

DESCRIPTION = "What is the result of the expression?"


def calculate(num1, num2, operation):
    match operation:
        case '+':
            return num1 + num2
        case '-':
            return num1 - num2
        case '*':
            return num1 * num2


def generate_expression():
    num1 = random.randint(1, 25)
    num2 = random.randint(1, 25)
    operations = ['+', '-', '*']
    operation = random.choice(operations)

    expression = f"{num1} {operation} {num2}"
    correct_answer = calculate(num1, num2, operation)

    return expression, correct_answer