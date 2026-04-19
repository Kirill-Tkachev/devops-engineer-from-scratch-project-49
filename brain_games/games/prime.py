import random

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    if n < 2:  
        return False 
    for i in range(2, n):  
        if n % i == 0:  
            return False 
    return True


def generate_expression():
    number = random.randint(1, 100)
    question = str(number)

    if is_prime(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"

    return question, correct_answer