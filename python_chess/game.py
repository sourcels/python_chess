from pygame import *
import os

window = display.set_mode((800, 600))
display.set_caption('Chess')
background = transform.scale(image.load(os.path.join("assets", "ui", "background.jpg")), (800, 600))
clock = time.Clock()
FPS = 60
#mixer.init()
#mixer.music.load('music.ogg')
#mixer.music.play()
font.init()
txt = font.SysFont('Arial', 80).render('Player 2 wins!', True, (0, 255, 0))
class gamespr(sprite.Sprite):
    def __init__(self, sprite_image, x, y, size_x, size_y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load(sprite_image), (size_x,size_y))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Figure(gamespr):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 300:
            self.rect.y += self.speed

figure = Figure('assets/figures/black_pawn.png', 20, 197, 26, 100)
while game:
    window.blit(background,(0,0))
    for event in event.get():
        if event.type == QUIT:
            game = False
    display.update()
    clock.tick(FPS)