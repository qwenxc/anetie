from pygame import *

img_racket='racket.png'
img_ball = 'tenis_ball.png'

class GSprite(sprite.Sprite):
    def __init__(self,pl_image,pl_x,pl_y,size_x,size_y,pl_speed):
        super().__init__()
        self.image = transform.scale(image.load(pl_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.speed = pl_speed
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image,self.rect)

class Player(GSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y >= 20:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y <= 400:
            self.rect.y += self.speed

class Player1(GSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y >= 20:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <= 400:
            self.rect.y += self.speed


class Ball(GSprite):
    def update(self):
        if self.rect.y >= 20 or self.rect.y <= 400:
            self.rect.x -= 5
            self.rect.y -= 5

player = Player(img_racket,650,250,30,90,7)
player1 = Player1(img_racket,50,250,30,90,7)
ball = GSprite(img_ball,350,250,30,30,5)



win_height = 500
win_width = 700
display.set_caption('anetie')
window = display.set_mode((win_width,win_height))
back = transform.scale(image.load('r.jpg'),(win_width,win_height))

yea = True
while yea:
    for e in event.get():
        if e.type == QUIT:
            yea = False


        
    window.blit(back,(0,0))
    
    player.update()
    player.reset()
    player1.update()
    player1.reset()
    ball.update()
    ball.reset()







    display.update()
    time.delay(30)