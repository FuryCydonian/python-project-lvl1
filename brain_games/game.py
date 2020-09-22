import random
import prompt
from brain_games.cli import welcome_user


def game():
    name = welcome_user()
    count = 0

    def is_even(num):
        if num % 2 == 0:
            return True
        else:
            return False

    answers = {
            'yes': True,
            'no': False,
        }

    while count < 3:
        number = random.randint(0, 50)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        answer.lower()

        if answer != 'yes' and answer != 'no':
            print(f"Wrong answer. Let's try again, {name}.")
            break
        else:
            if is_even(number) == answers[answer]:
                print('Correct!')
                print('')
                count += 1
                continue
            else:
                if answer == 'yes':
                    not_answer = 'no'
                else:
                    not_answer = 'yes'

                print(f"{answer} is wrong answer ;(. Correct answer was {not_answer}. Let's try again, {name}!")
                break

    if count == 3:
        print(f'Congratulations, {name}!')
