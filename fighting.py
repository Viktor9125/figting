import colorama
import random
import time
import os

white_color = colorama.Fore.WHITE
green_color = colorama.Fore.GREEN
red_color = colorama.Fore.RED
blue_color = colorama.Fore.BLUE
yellow_color = colorama.Fore.YELLOW
cyan_color = colorama.Fore.CYAN

delay = 2

role = {
    '1': 'Воин',
    '2': 'Лучник',
    '3': 'Маг'
}

classes = {
    'Воин': {
        'здоровье': 100,
        'атака': 30,
        'защита': 25,
        'навыки': {
            'щит': 10
        }
    },
    'Лучник': {
        'здоровье': 50,
        'атака': 40,
        'защита': 20,
        'навыки': {
            'убежать': 10
        }
    },
    'Маг': {
        'здоровье': 30,
        'атака': 50,
        'защита': 15,
        'навыки': {
            'магический щит': 10,
            'лечение': 5
        }
    }
}


def init_person(name: str, is_enemy: bool = False) -> dict[str, str | dict[str, int | dict]]:
    if is_enemy:
        person = {'класс': role[random.choice(list(role.keys()))]}
    else:
        while True:
            choice = input(f"{blue_color}Введите роль: 1-Воин, 2-Лучник, 3-Маг\n{white_color}")
            if is_valid(choice, True):
                break
        person = {'класс': role[choice]}

    person.update({'характеристики': classes[person['класс']]})
    person.update({'имя': name})

    print(
        f"{blue_color}{person['имя']} - {person['класс']}, имеет характеристики: {person['характеристики']}{white_color}")
    return person


def attack_enemy(enemy1: dict[str, str | dict], enemy2: dict[str, str | dict]) -> None:
    print(f"{green_color}{enemy1['имя']}{white_color} атакует {red_color}{enemy2['имя']}!{white_color}")
    time.sleep(delay)

    apply_skill(enemy2)

    damage = enemy1['характеристики']['атака'] - enemy2['характеристики']['защита']
    if damage < 0:
        damage = 1

    enemy2['характеристики']['здоровье'] -= damage
    print(
        f"{enemy1['имя']} наносит {red_color}{damage} урона{white_color} и у {enemy2['имя']} остается {green_color}{enemy2['характеристики']['здоровье']} здоровья!{white_color}")


def fight_for_the_win(attacker: dict[str, str | dict], defender: dict[str, str | dict]) -> bool:
    while True:
        time.sleep(delay)
        clear()

        if attacker['характеристики']['здоровье'] > 0:
            attack_enemy(attacker, defender)
        else:
            print(f"{red_color}{attacker['имя']} потерпел поражение!{white_color}")
            return False

        if defender['характеристики']['здоровье'] > 0:
            attack_enemy(defender, attacker)
        else:
            print(f"{green_color}{defender['имя']} потерпел поражение!{white_color}")
            return True
        proceed()


def proceed(): input('Нажмите Enter, чтобы продолжить.')


def apply_skill(enemy2):
    apply_skill2 = random.randint(0, 9)
    if apply_skill2 > 6:
        skill = random.choice(list(enemy2['характеристики']['навыки'].keys()))
        enemy2['характеристики']['здоровье'] += enemy2['характеристики']['навыки'][skill]

        print(f"{blue_color}{enemy2['имя']} применяет способность {green_color}{skill}!{white_color}")


def get_random_name() -> str:
    from random import choice
    first_names = ['Доктор', 'Летающий', 'Светящийся', 'Профессор', 'Неимоверный', 'Мега', 'Железный', 'Голодный',
                   'Капитан', 'Быстрый', 'Мистер', 'Горячий', 'Звездный', 'Космический', 'Стойкий', 'Восхитительный',
                   'Непопедимый']
    second_names = ['слесарь', 'мухомор', 'пепел', 'лемур', 'шаман', 'пельмень', 'слизень', 'алхимик', 'крот', 'фикус',
                    'господин', 'кролик', 'танцор', 'пингвин', 'викинг', 'паук', 'плащ']
    return f"{choice(first_names)} {choice(second_names)}"


def is_valid(other: str, is_role: bool = False) -> bool:
    if len(other) <= 0:
        print('Ошибка ввода. Вы ввели пустую строку.')
        return False
    elif other not in '123' and is_role:
        print('Ошибка ввода. Вы ввели не правильное значение. Введите числа от 1 до 3.')
        return False
    else:
        return True


def get_player_name() -> str:
    while True:
        player_name = input(f'{blue_color}Как зовут твоего героя?\n{white_color}')
        if is_valid(player_name):
            break
    return player_name


def clear(): return os.system('cls')


clear()

player = init_person(name=get_player_name())
enemy = init_person(name=get_random_name(), is_enemy=True)

proceed()
clear()

fight_for_the_win(player, enemy)


def attack_enemy2(self, target):
    print(f'{green_color}{self.name}{white_color} атакует {red_color}{target.name}!{white_color}')
    time.sleep(2)

    damage = self.attack - target.defence
    if damage < 0:
        damage = 1
    target.health -= damage

    print(f'{self.name} наносит {red_color}{damage} урона{white_color} и у {target.name} остается {green_color}{target.health} здоровья!{white_color}')
    time.sleep(2)


def fight_for_the_win(self, attacker, defender):
    while attacker.is_alive and defender.is_alive:
        time.sleep(2)

        if attacker.health > 0:
            self.attack_enemy(attacker, defender)
        else:
            print(f"{red_color}{attacker.name} потерпел поражение!{white_color}")
            attacker.is_alive = False
            return False

        if defender.health > 0:
            self.attack_enemy(defender, attacker)
        else:
            print(f"{green_color}{defender.name} потерпел поражение!{white_color}")
            defender.is_alive = False
            return True

import os


class Utils:
    def clear(self):
        return os.system('cls')     # os.system('clear') для Linux и MacOS

    def go_on(self):
        input('Нажмите Enter, чтобы продолжить')
        self.clear()

    def is_valid(self, other, data_range=''):
        if len(other) == 0:
            print('Ошибка ввода. Вы ввели пустую строку.')
            return False
        elif (other not in data_range and (data_range != '')) or (other == data_range):
            print(
                f'Ошибка ввода. Введите числа от {data_range[0]} до {data_range[-1]}.')
            return False
        else:
            return True


