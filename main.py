from pygame import *
import sys

#Создание атрибутов
window = display.set_mode((700, 500))
display.set_caption("Лабиринт")
#background = transform.scale(image.load("background.jpg"), (700, 500))

#Создание музыки
mixer.init()
mixer.music.load("popa.mp3")
mixer.music.play()
damage = mixer.Sound("inecraft_death.ogg")
finish = mixer.Sound("pobeda.ogg")

#Создание шрифтов
font.init()
font = font.Font(None, 70)
win = font.render("YOU WIN", True, (0,255,0))
lose = font.render("YOU LOSE", True, (255,0,0))

#Класс
class GameSprite(sprite.Sprite):
    def __init__(self, p_i, p_x, p_y, p_s, p_s_x, p_s_y):
        super().__init__()
        self.image = transform.scale(image.load(p_i), (p_s_x, p_s_y))
        self.speed = p_s
        self.rect = self.image.get_rect()
        self.rect.x = p_x
        self.rect.y = p_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.y < 450:
            self.rect.y += self.speed
        if key_pressed[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
        if key_pressed[K_d] and self.rect.x < 650:
            self.rect.x += self.speed

class Enemy(GameSprite):
    direct = 'left'
    def update(self):
        if self.rect.x <= 400:
            self.direct = 'right'
        if self.rect.x >= 600:
            self.direct = 'left'
        
        if self.direct == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3,  wall_x, wall_y, wall_width, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

background = GameSprite("background.jpg", 0, 0, 0, 700, 500) #prosto blit
hero = Player("hero.png", 0, 450, 5, 10, 50)
enemy1 = Enemy("tolstjak.png", 400, 300, 5, 50, 90)
pasta = GameSprite("win.png", 600, 450, 0, 50, 50)
w1 = Wall(255, 5, 218, 100, 20, 450, 10)
w2 = Wall(255, 5, 218, 100, 20 , 10, 380)
w3 = Wall(255, 5, 218, 100, 480, 450, 10)
w4 = Wall(255, 5, 218, 150, 100, 10, 400)
w5 = Wall(255, 5, 218, 550, 200, 10, 400)



#Запускаем игровой цикл
clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    background.reset()
    pasta.reset()
    hero.reset()
    enemy1.reset()
    #ОТРИСОВКА СТЕН
    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()

    hero.update()
    enemy1.update()

    #Проверка победы
    if sprite.collide_rect(hero, pasta):
        window.blit(win, (200, 200))
        finish.play()
        sys.exit()
    
    #Проверка проигрыша
    if (sprite.collide_rect(hero, enemy1) or sprite.collide_rect(hero, w1) or 
        sprite.collide_rect(hero, w2) or sprite.collide_rect(hero, w3) or sprite.collide_rect(hero, w4) or sprite.collide_rect(hero, w5)):
        window.blit(lose, (200, 200))
        damage.play()
        hero.rect.x = 0
        hero.rect.y = 450

    display.update()
    clock.tick(FPS)



    

# w1(154, 205, 50, 100, 20 , 450, 10)
# w2(154, 205, 50, 100, 480, 350, 10)
# w3(154, 205, 50, 100, 20 , 10, 380)