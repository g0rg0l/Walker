import random

def choose_the_drop_10():
    list = ['bow', 'heal_bottle']
    return random.choice(list)

def random_place_to_teleportation_of_boss_ghost(display_width, display_height, user_x, user_y):
    while True:
        x = random.choice(range(100, display_width - 100))
        y = random.choice(range(160, display_height - 160))

        if user_x-100 <= x <= user_x+100 and user_y-158 <= y <= user_y+158:
            pass
        else:
            break
    return (x, y)


def chanse_to_spawn_the_enemy(lvl):   # Генерация рандомного числа противников
    if lvl < 10:
        if lvl == 1:
            return 1
        elif 2 <= lvl <= 5:
            return 2
        elif 6 <= lvl <= 7:
            return 3
        elif lvl == 8:
            return 4
        elif lvl == 9:
            return 5
        elif lvl == 10:
            return 0

def chanse_to_spawn_the_chest():   # Генерация рандомного числа сундуков
    choice = random.choice(range(100))

    if choice <= 10:
        return 3
    elif choice <= 20:
        return 2
    elif choice <= 85:
        return 1
    else:
        return 0

def random_position_of_spawn(display_width, display_height):   # Генерация рандомного места генерации на карте
    x = random.choice(range(65, display_width - 65))
    y = random.choice(range(65, display_height - 65))

    return (x, y)

def random_position_of_spawn_chest(display_width, display_height):   # Генерация рандомного места для сундука генерации на карте
    x = random.choice(range(165, display_width - 165))
    y = random.choice(range(165, display_height - 165))

    return (x, y)

def check_for_item(list):
    return random.choice(list)

def chanse_to_broke_the_bow():
    return random.choice(range(100))