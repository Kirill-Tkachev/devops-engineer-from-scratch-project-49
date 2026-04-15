import prompt


def run_game(game_module):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print(game_module.DESCRIPTION)

    ROUNDS_COUNT = 3

    for _ in range(ROUNDS_COUNT):
        question, correct_answer = game_module.generate_expression()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")

        if user_answer == str(correct_answer):
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")