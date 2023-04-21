import models
import settings
import exceptions


def get_player_name():
    return input("Hello, please enter your name : ")


def play() -> None:

    enemy = models.Enemy(level=settings.INITIAL_ENEMY_LEVEL, health=settings.INITIAL_ENEMY_HEALTH)
    player = models.Player(name=get_player_name(), health=settings.INITIAL_PLAYER_HEALTH,
                           score=settings.INITIAL_PLAYER_SCORE, result_fight=0)

    round = 0
    while True:
        try:
            player.attack(enemy)
            round += 1
            print('round = ', round)
            player.defence(enemy)
            round += 1
            print('round = ', round)
        except exceptions.EnemyDown:
            enemy = models.Enemy(enemy.level + 1, enemy.health)
        except exceptions.GameOver:
            break


if __name__ == '__main__':
    try:
        play()
    except KeyboardInterrupt:
        print('you are off')
