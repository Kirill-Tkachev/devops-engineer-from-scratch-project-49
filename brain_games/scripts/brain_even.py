import random

from brain_games.cli import welcome_user


def is_even(number):
    return number % 2 == 0


def game_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    
    correct_answer = 0
    need_correct_answer = 3

    while correct_answer < need_correct_answer:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = input('Your answer: ').strip().lower()

        correct_answer_str = 'yes' if is_even(number) else 'no'

        if user_answer == correct_answer_str:
            print('Correct!')
            correct_answer += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. Correct answer was "{correct_answer_str}".')
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')


def main():
    game_even()


if __name__ == '__main__':
    main()