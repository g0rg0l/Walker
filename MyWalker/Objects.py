import pygame
display_width = 1400
display_height = 700

############################# Класс объекта-игрока ##############################
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\knight\\front.png')
        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height / 2)
        self.hp = 5
        self.items = []
        self.scores = 0
        self.lvl = 9
        self.time_to_realise = True
        self.time_spended_to_realise = 0
        self.sword_time = 1
        self.bow_time = 1

############################# Класс инвентаря ##############################
class Inventory:
    def __init__(self):
        self.items = []

############################# Класс объекта-бара прочности ##############################
class Bar_DURABILITY(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        self.rect = self.image.get_rect()
        self.rect.left = 350
        self.rect.top = 5

############################# Класс эффекта следа меча ##############################
class Smash(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/empty_slot.png')
        self.rect = self.image.get_rect()
        self.name = ''
        self.condition = 1

############################# Класс объекта-бара хп ##############################
class Bar_HP(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\health\\5.png')
        self.rect = self.image.get_rect()
        self.rect.center = (1215,675)

############################# Класс объекта-бара хп босса ##############################
class Boss_Bar_HP(pygame.sprite.Sprite):
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\boss_bars\\1.png')
        self.rect = self.image.get_rect()
        self.rect.center = (500,500)
        self.follow = object
        self.condition = 1

############################# Класс объекта-бара хп противника ##############################
class Enemy_Bar_HP(pygame.sprite.Sprite):
    def __init__(self, object):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy health\\3.png')
        self.rect = self.image.get_rect()
        self.follow = object

############################# Класс объекта-портала призраков ##############################
class Ghost_portal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/objects/portal_right_1.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction = ''
        self.spawned_ghosts = 0
        self.spawn_timer = 1

################################ Класс призрака ##################################
class Ghost(pygame.sprite.Sprite):
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy\\ghost_left.png')
        self.rect = self.image.get_rect()
        self.speed = 2
        self.hp = 6
        self.bar = object
        self.direction = ''

################################ Класс призрака-босса ##################################
class Ghost_Boss(pygame.sprite.Sprite):
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy\\ghost_boss_left_1.png')
        self.rect = self.image.get_rect()
        self.bar = object
        self.hp = 1
        self.condition = 1
        self.direction = 'left'
        self.teleportation = 1
        self.blue_ball_timer = 1
        self.pink_ball_timer = 1
        self.count_of_pink_balls = 0
        self.portal_timer = 1
        self.angry = False
        self.created_portals = False
        self.invisible = False

################################ Класс импа ##################################
class Imp(pygame.sprite.Sprite):
    def __init__(self, object=0):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\enemy\\imp_front_1.png')
        self.rect = self.image.get_rect()
        self.speed = 1
        self.hp = 10
        self.bar = object
        self.shoot_timming = 1
        self.condition = 1
        self.direction = ''

############################# Класс объекта-снаряда Импа ##############################
class Imp_Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/empty_slot.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction = ''

############################# Класс объекта-синего файерболла ##############################
class Ghost_boss_blue_ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/attacking/blue_ball_left_1.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction = ''

############################# Класс объекта-розового файерболла ##############################
class Ghost_boss_pink_ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/attacking/pink_ball_left_1.png')
        self.rect = self.image.get_rect()
        self.condition = 1
        self.direction =''

################################ Класс ячейки инвентаря ##################################
class Ceil_of_inventory(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\inventory\\ceil_of_inventory.png')
        self.rect = self.image.get_rect()
        self.is_empty = True

################################ Класс места для предмета в ячейке инвентаря ##################################
class Place_for_item_in_ceil(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\inventory\\items\\empty_slot.png')
        self.rect = self.image.get_rect()

################################ Класс сундука ##################################
class Chest(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\objects\\chest.png')
        self.rect = self.image.get_rect()
        self.opened = False
        self.dropted = False

############################# Класс right_left места для меча ##############################
class Right_left_sword_barrier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/attacking/left_and_right_sword_place.png')
        self.rect = self.image.get_rect()
        self.name = ''

############################# Класс top_bottom места для меча ##############################
class Top_bottom_sword_barrier(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/attacking/top_and_bottom_sword_place.png')
        self.rect = self.image.get_rect()
        self.name = ''

############################# Класс гозизонтальной стены ##############################
class Wall_Horizontal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\level elements\\wall-horizontal.png')
        self.rect = self.image.get_rect()

############################# Класс вертикальной стены ##############################
class Wall_Vertical(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\level elements\\wall-vertical.png')
        self.rect = self.image.get_rect()

############################# Класс временной вертикальной стены ##############################
class Temporary_Wall_Vertical(pygame.sprite.Sprite):
    def __init__(self, place):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\level elements\\temporary_vertical_wall.png')
        self.rect = self.image.get_rect()
        self.place = place

############################# Класс временной горизонтальной стены ##############################
class Temporary_Wall_Horizontal(pygame.sprite.Sprite):
    def __init__(self, place):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\level elements\\temporary_horizontal_wall.png')
        self.rect = self.image.get_rect()
        self.place = place

############################# Класс хилки ##############################
class Heal_bottle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/heal_bottle.png')
        self.rect = self.image.get_rect()
        self.name = 'heal_bottle'

############################# Класс чёрного фона ##############################
class Black(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/level elements/black.png')
        self.rect = self.image.get_rect()
        self.image.set_alpha(1)

############################# Класс арбалета ##############################
class Crossbow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/crossbow.png')
        self.rect = self.image.get_rect()
        self.name = 'crossbow'

############################# Класс меча ##############################
class Sword(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/sword.png')
        self.rect = self.image.get_rect()
        self.name = 'sword'

############################# Класс лука ##############################
class Bow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/bow.png')
        self.rect = self.image.get_rect()
        self.name = 'bow'
        self.durability = 30

############################# Класс сообщения ##############################
class Message(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources/inventory/items/empty_slot.png')
        self.rect = self.image.get_rect()

############################# Класс снаряда ##############################
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\attacking\\arrow.png')
        self.rect = self.image.get_rect()
        self.direction = 0
        self.speed = 11

################################ Класс заднего фона ##################################
class Background(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('resources\\level elements\\background-1.png')
        self.rect = self.image.get_rect()
        self.index_of_room = 1

    def change_the_room(self, count_of_room):
        directory = 'resources\\level elements\\background-' + str(count_of_room + 1) + '.png'
        self.image = pygame.image.load(directory)