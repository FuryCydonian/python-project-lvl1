# from brain_games.cli import welcome_user
from brain_games.scripts import brain_games
from brain_games.game import game


def main():
    brain_games.main()
    game()


if __name__ == '__main__':
    main()
