import random

DESCRIPTION = "What number is missing in the progression?"


def generate_progression(start, step, length):
    return [start + i * step for i in range(length)]


def generate_expression():
    start = random.randint(1, 20)
    step = random.randint(1, 10)
    length = random.randint(5, 10)

    progression = generate_progression(start, step, length)

    skipped_index = random.randint(0, length - 1)
    correct_answer = progression[skipped_index]

    progression[skipped_index] = '..'

    question = ' '.join(map(str, progression))

    return question, correct_answer