import pygame
import math
import time

pygame.init()  # Инициализация pygame

############################# Параметры экрана #############################
display_width = 1400
display_height = 700
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("My Walker")
first_room = True

clock = pygame.time.Clock()  # Переменная для подсчёта тиков

############################# Класс объекта-игрока ##############################
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('knight\\front.png')
        self.rect = self.image.get_rect()
        self.rect.center = (display_width / 2, display_height / 2)

################################ Класс сундука ##################################
class Chest(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('chest.png')
        self.rect = self.image.get_rect()

############################# Класс объекта-стены ##############################
class Wall_Horizontal(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('wall_horizontal.jpg')
        self.rect = self.image.get_rect()

class Wall_Vertical(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('wall_horizontal.jpg')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.rotate(self.image, 90)


def run_game():   # Основная функция игры
    game = True
    first = True

    all_sprites = pygame.sprite.Group()  # Группа спрайтов
    walls = pygame.sprite.Group()   # Группа стен
    chests = pygame.sprite.Group()   # Группа сундуков

    chest = Chest()  # Создаём сундук
    all_sprites.add(chest)
    chests.add(chest)
    chest.rect.center = (500, 100)

    user = Player()   # Создаём игрока
    all_sprites.add(user)


    ############################# Создаём стены ##############################
    wall_top_1 = Wall_Horizontal()
    all_sprites.add(wall_top_1)
    walls.add(wall_top_1)
    wall_top_1.rect.left = 0

    wall_top_2 = Wall_Horizontal()
    all_sprites.add(wall_top_2)
    walls.add(wall_top_2)
    wall_top_2.rect.left = 350

    wall_top_3 = Wall_Horizontal()
    all_sprites.add(wall_top_3)
    walls.add(wall_top_3)
    wall_top_3.rect.left = 1050

    wall_top_4 = Wall_Horizontal()
    all_sprites.add(wall_top_4)
    walls.add(wall_top_4)
    wall_top_4.rect.left = 0
    wall_top_4.rect.bottom = display_height

    wall_top_5 = Wall_Horizontal()
    all_sprites.add(wall_top_5)
    walls.add(wall_top_5)
    wall_top_5.rect.left = 750
    wall_top_5.rect.bottom = display_height

    wall_top_6 = Wall_Horizontal()
    all_sprites.add(wall_top_6)
    walls.add(wall_top_6)
    wall_top_6.rect.left = 1050
    wall_top_6.rect.bottom = display_height

    wall_top_7 = Wall_Vertical()
    all_sprites.add(wall_top_7)
    walls.add(wall_top_7)
    wall_top_7.rect.top = -150

    wall_top_8 = Wall_Vertical()
    all_sprites.add(wall_top_8)
    walls.add(wall_top_8)
    wall_top_8.rect.top = 500

    wall_top_9 = Wall_Vertical()
    all_sprites.add(wall_top_9)
    walls.add(wall_top_9)
    wall_top_9.rect.top = -150
    wall_top_9.rect.right = 1700

    wall_top_10 = Wall_Vertical()
    all_sprites.add(wall_top_10)
    walls.add(wall_top_10)
    wall_top_10.rect.right = 1700
    wall_top_10.rect.top = 500

    index_of_room = 0

    while game:   # Пока сеанс игры запущен:
        for event in pygame.event.get():   # Считываем все события
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()   # Инициализируем клавиатуру

        ############################# Движение игрока ##############################

        if first:
            back = False   # Направления, куда смотрит игрок
            front = True
            right = False
            left = False
            first = False

        if keys[pygame.K_w] and keys[pygame.K_a]:
            if user.rect.x <= 50 and 200 <= user.rect.y <= 205:
                pass
            elif user.rect.right >= display_width - 50 and 300 <= user.rect.bottom <= 500:
                pass
            elif 339 <= user.rect.left <= 350 and user.rect.bottom > 650:
                pass
            elif 700 <= user.rect.x <= 705 and user.rect.top < 50:
                pass
            else:
                user.rect.y -= 2
                user.rect.x -= 2
        elif keys[pygame.K_w]:
            if user.rect.x <= 50 and 200 <= user.rect.y <= 205:
                pass
            elif user.rect.right >= display_width - 50 and 200 <= user.rect.y <= 205:
                pass
            else:
                user.rect.y -= 4
                back = True
                front = False
                right = False
                left = False
        elif keys[pygame.K_a]:
            if 339 <= user.rect.left <= 350 and user.rect.bottom > 650:
                pass
            elif 700 <= user.rect.x <= 705 and user.rect.top < 50:
                pass
            else:
                user.rect.x -= 4
                back = False
                front = False
                right = False
                left = True

        if keys[pygame.K_w] and keys[pygame.K_d]:
            if user.rect.x <= 50 and 200 <= user.rect.y <= 205:
                pass
            elif user.rect.right >= display_width - 50 and 200 <= user.rect.y <= 205:
                pass
            elif 669 <= user.rect.x <= 675 and user.rect.bottom > 650:
                pass
            elif 970 <= user.rect.x <= 975 and user.rect.top < 50:
                pass
            else:
                user.rect.y -= 2
                user.rect.x += 2
        elif keys[pygame.K_w]:
            if user.rect.x <= 50 and 200 <= user.rect.y <= 205:
                pass
            elif user.rect.right >= display_width - 50 and 200 <= user.rect.y <= 205:
                pass
            else:
                user.rect.y -= 4
                back = True
                front = False
                right = False
                left = False
        elif keys[pygame.K_d]:
            if 669 <= user.rect.x <= 675 and user.rect.bottom > 650:
                pass
            elif 970 <= user.rect.x <= 975 and user.rect.top < 50:
                pass
            else:
                user.rect.x += 4
                back = False
                front = False
                right = True
                left = False

        if keys[pygame.K_d] and keys[pygame.K_s]:
            if user.rect.x <= 50 and 495 <= user.rect.bottom <= 500:
                pass
            elif user.rect.right >= display_width - 50 and 500 <= user.rect.bottom <= 505:
                pass
            elif 669 <= user.rect.x <= 675 and user.rect.bottom > 650:
                pass
            elif 970 <= user.rect.x <= 975 and user.rect.top < 50:
                pass
            else:
                user.rect.x += 2
                user.rect.y += 2
        elif keys[pygame.K_d]:
            if 669 <= user.rect.x <= 675 and user.rect.bottom > 650:
                pass
            elif 970 <= user.rect.x <= 975 and user.rect.top < 50:
                pass
            else:
                user.rect.x += 4
                back = False
                front = False
                right = True
                left = False
        elif keys[pygame.K_s]:
            if user.rect.x <= 50 and 495 <= user.rect.bottom <= 500:
                pass
            elif user.rect.right >= display_width - 50 and 500 <= user.rect.bottom <= 505:
                pass
            else:
                user.rect.y += 4
                back = False
                front = True
                right = False
                left = False
        if keys[pygame.K_s] and keys[pygame.K_a]:
            if user.rect.x <= 50 and 495 <= user.rect.bottom <= 500:
                pass
            elif user.rect.right >= display_width - 50 and 495 <= user.rect.bottom <= 501:
                pass
            elif 339 <= user.rect.left <= 350 and user.rect.bottom > 650:
                pass
            elif 700 <= user.rect.x <= 705 and user.rect.top < 50:
                pass
            else:
                user.rect.y += 2
                user.rect.x -= 2
        elif keys[pygame.K_s]:
            if user.rect.x <= 50 and 490 <= user.rect.bottom <= 500:
                pass
            elif user.rect.right >= display_width - 50 and 500 <= user.rect.bottom <= 505:
                pass
            else:
                user.rect.y += 4
                back = False
                front = True
                right = False
                left = False
        elif keys[pygame.K_a]:
            if 339 <= user.rect.left <= 350 and user.rect.bottom > 650:
                pass
            elif 700 <= user.rect.x <= 705 and user.rect.top < 50:
                pass
            else:
                user.rect.x -= 4
                back = False
                front = False
                right = False
                left = True


        if user.rect.right > display_width - 50:
            if 200 <= user.rect.y <= 400:
                pass
            else:
                user.rect.right = display_width - 50
        if user.rect.left < 50:
            if 200 <= user.rect.y <= 400:
                pass
            else:
                user.rect.left = 50
        if user.rect.top < 50:
            if 700 <= user.rect.x <= 975:
                pass
            else:
                user.rect.top = 50
        if user.rect.bottom > display_height - 50:
            if 345 <= user.rect.x <= 675:
                pass
            else:
                user.rect.bottom = display_height - 50



        if user.rect.right >= display_width + 150:
            user.rect.left = -150
            index_of_room += 1
        elif user.rect.left <= -150:
            user.rect.right = display_width + 150
            index_of_room += 1
        elif user.rect.top <= -150:
            user.rect.bottom = display_height + 150
            user.rect.x = 500
            index_of_room += 1
        elif user.rect.bottom >= display_height + 150:
            user.rect.top = -150
            user.rect.x = 835
            index_of_room += 1

        index_of_room %= 4

        pygame.sprite.spritecollide(user, chests, True)

        if front:
            user.image = pygame.image.load('knight\\front.png')  # Переменная-картинка игрока
        elif back:
            user.image = pygame.image.load('knight\\back.png')  # Переменная-картинка игрока
        elif right:
            user.image = pygame.image.load('knight\\right.png')  # Переменная-картинка игрока
        elif left:
            user.image = pygame.image.load('knight\\left.png')  # Переменная-картинка игрока

        if index_of_room % 4 == 0:
            display.fill((179, 179, 179))
        elif index_of_room % 4 == 1:
            display.fill((127, 118, 121))
        elif index_of_room % 4 == 2:
            display.fill((79, 79, 70))
        elif index_of_room % 4 == 3:
            display.fill((101, 161, 151))


        all_sprites.update()   # Обновление спрайтов
        all_sprites.draw(display)  # Прорисовка всех спрайтов
        pygame.display.flip()   # Переворчиваем экран
        clock.tick(60)   # FPS



run_game()