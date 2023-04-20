"""Этот код определяет несколько констант, используемых в игре:
PLAYER_LIVES: количество жизней, с которыми игрок начинает игру.
ALLOWED_ATTACKS: список целых чисел, представляющих разрешенные варианты атаки для игрока.
КОМАНДЫ: список строк, представляющих доступные команды в меню игры.
Эти константы используются на протяжении всей игры и не предназначены для изменения во время выполнения."""

PLAYER_LIVES = 2
ALLOWED_ATTACKS = [1, 2, 3]
COMMANDS = ['help', 'start', 'show scores', 'exit']

HARD_MODE_MULTIPLIER = 3