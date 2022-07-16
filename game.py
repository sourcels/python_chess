from pygame import *
import os

window = display.set_mode((800, 600))
display.set_caption('Chess')
background = transform.scale(image.load(r"assets\\design\\background.jpg"), (800, 600))
clock = time.Clock()
FPS = 60
game = True
#mixer.init()
#mixer.music.load('music.ogg')
#mixer.music.play()
font.init()
txt = font.SysFont('Arial', 50).render('Pygame chess', True, (0, 0, 0))
class gamespr(sprite.Sprite):
    def __init__(self, sprite_image, x, y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(sprite_image), (size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Figure(gamespr):
    def func(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 300:
            self.rect.y += self.speed

figure = Figure(r"assets\\figures\\black_pawn.png", 100, 100, 45, 45)
while game:
    window.blit(background,(0,0))
    figure.update()
    figure.func()
    window.blit(txt, (0,0))

    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)