import random
import prompt
from brain_games.cli import welcome_user

name = welcome_user()
count = 0


def is_even(num):
    if num % 2 == 0:
        return True
    return False


answers = {
        'yes': True,
        'no': False,
    }

while count <= 3:
    number = random.randint(0, 50)
    print(f'Question: {number}')
    answer = prompt.string('Your answer: ')
    answer.lower()

    if (is_even(number) == answers[answer]) or (not is_even(number) == answers[answer]):
        print('Correct!')
        count += 1
        continue
    else:
        print(f"{answer} is wrong answer ;(. Correct answer was {not answers[answer]}. Let's try again, {name}!")
        break
