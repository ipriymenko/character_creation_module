"""Doc string for entire module."""
from random import randint
from graphic_arts.start_game_banner import run_screensaver


DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10 
DEFAULT_STAMINA = 80

class Character:

    RANGE_VALUE_ATTACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)

    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    SPECIAL_BUFF = 15
    SPECIAL_SKILL = 'Удача'

    def __init__(self,name):
        self.name=name

    def attack(self):
        value_attack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATTACK)
        return f'{self.name} нанёс противнику урон, равный {value_attack}'

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return f'{self.name} блокировал {value_defence} ед. урона.'

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.__class__.__name__} - {self.BRIEF_DESC_CHAR_CLASS}.'

class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'

class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'

class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита' 


def start_training(character):
    """
    Принимает объект персонажа.
    Возвращает сообщения о результатах цикла тренировки персонажа.
    """
    # Замените конструкцию условных операторов на словарь.
    commands = {
        'attack': character.attack,
        'defence': character.defence,
        'special': character.special
    }
    
    print(f'{character.name}, {character}.')
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать противника, '
          'defence — чтобы блокировать атаку противника или '
          'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            print(commands[cmd]())
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """
    Возвращает строку с выбранным
    классом персонажа.
    """
    # Добавили словарь, в котором соотносится ввод пользователя и класс персонажа.
    game_classes = {'warrior': Warrior, 'mage': Mage, 'healer': Healer}
    
    approve_choice: str  = None
    
    while approve_choice != 'y':
        selected_class = input('Введи название персонажа, '
                           'за которого хочешь играть: Воитель — warrior, '
                           'Маг — mage, Лекарь — healer: ')
        char_class: Character = game_classes[selected_class](char_name)
        # Вывели в терминал описание персонажа.
        print(char_class)
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, '
                               'или любую другую кнопку, '
                               'чтобы выбрать другого персонажа ').lower()
    return char_class 





def attack(char_name: str, char_class: str) -> str:
    """Doc string for attack function."""
    if char_class == 'warrior':
        damage = 5 + randint(3, 5)
    elif char_class == 'mage':
        damage = 5 + randint(5, 10)
    elif char_class == 'healer':
        damage = 5 + randint(-3, -1)
    else:
        damage = 0

    if damage:
        return f'{char_name} нанёс урон противнику равный {damage}'
    else:
        return f'{char_name} не нанёс урон противнику'


def defence(char_name: str, char_class: str) -> str:
    """Doc string for defence function."""
    if char_class == 'warrior':
        block = 10 + randint(5, 10)
    elif char_class == 'mage':
        block = 10 + randint(-2, 2)
    elif char_class == 'healer':
        block = 10 + randint(2, 5)
    else:
        block = 0

    if block:
        return f'{char_name} блокировал {block} урона'
    else:
        return f'{char_name} не смог заблокировать урон'


def special(char_name: str, char_class: str) -> str:
    """Doc string for special function."""
    if char_class == 'warrior':
        spec_title = 'Выносливость'
        spec_value = 80 + 25

    elif char_class == 'mage':
        spec_title = 'Атака'
        spec_value = 5 + 40

    elif char_class == 'healer':
        spec_title = 'Защита'
        spec_value = 10 + 30

    else:
        spec_value = 0
        spec_title = ''

    if spec_value and spec_title:
        return (f'{char_name} применил специальное умение '
                f'«{spec_title} {spec_value}»')
    else:
        return f'{char_name} не применил специальное умение'


def start_training(char_name: str, char_class: str) -> str:
    """Doc string for start_training function."""
    if char_class == 'warrior':
        print(f'{char_name}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name}, ты Маг — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name}, ты Лекарь — чародей, способный исцелять раны.')
    print('Потренируйся управлять своими навыками.')
    print(
        'Введи одну из команд: attack — чтобы атаковать противника, '
        'defence — чтобы блокировать атаку противника или '
        'special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(attack(char_name, char_class))
        if cmd == 'defence':
            print(defence(char_name, char_class))
        if cmd == 'special':
            print(special(char_name, char_class))
    return 'Тренировка окончена.'


def choice_char_class() -> str:
    """Doc string for choice_char_class function."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input(
            'Введи название персонажа, за которого хочешь играть: '
            'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. '
                  'Сильный, выносливый и отважный.')
        if char_class == 'mage':
            print('Маг — находчивый воин дальнего боя. '
                  'Обладает высоким интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. '
                  'Черпает силы из природы, веры и духов.')
        approve_choice = input(
            'Нажми (Y), чтобы подтвердить выбор, или любую другую кнопку, '
            'чтобы выбрать другого персонажа ').lower()
    return str(char_class)


def main() -> None:
    """Doc string for main function."""
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name: str = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class: str = choice_char_class()
    print(start_training(char_name, char_class))


if __name__ == '__main__':
    main()
