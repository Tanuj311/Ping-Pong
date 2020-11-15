import pygame
import random
pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

win = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption('PING PONG')
y = SCREEN_HEIGHT/2 -50
y1 = SCREEN_HEIGHT/2 -50
y2 = SCREEN_HEIGHT/2 -50
x1 = 40
x2 = SCREEN_WIDTH-50
clock = pygame.time.Clock()
score1 = 0
score2 = 0

def draw():
    font = pygame.font.Font(None,35)
    text1 = font.render(f'SCORE: {score1}', True, (255,255,255))
    win.blit(text1, (20,20))

    text2 = font.render(f'SCORE: {score2}', True, (255,255,255))
    win.blit(text2, (SCREEN_WIDTH-130, 20))

    pygame.draw.rect(win,(255,255,255),(x1, y1, 20,100))
    pygame.draw.rect(win,(255,255,255),(x2, y2, 20,100))
    obj.draw()

    pygame.draw.line(win,(255,255,255),(SCREEN_WIDTH/2,0),(SCREEN_WIDTH/2,SCREEN_HEIGHT))

class ball:
    def __init__(self):
        self.x = SCREEN_WIDTH/2
        self.y = SCREEN_HEIGHT/2
        self.vel = 10
        self.LEFT_UP = False
        self.LEFT_DOWN = False
        self.RIGHT_UP = False
        self.RIGHT_DOWN = False
        self.dir = random.randint(1,4)
        if self.dir == 1:
            self.LEFT_UP = True
        elif self.dir == 2:
            self.LEFT_DOWN = True
        elif self.dir == 3:
            self.RIGHT_UP = True
        elif self.dir == 4:
            self.RIGHT_DOWN = True

    def move(self):
        if self.LEFT_UP:
            self.x -= self.vel
            self.y -= self.vel
        if self.LEFT_DOWN:
            self.x -= self.vel
            self.y += self.vel
        if self.RIGHT_UP:
            self.x += self.vel
            self.y -= self.vel
        if self.RIGHT_DOWN:
            self.x += self.vel
            self.y += self.vel

    def collide(self):

        if self.x == x1 and self.y < y1+100 and self.y+20 > y1:
            if self.y <= y1+50:
                self.RIGHT_UP = True
                self.RIGHT_DOWN = False
                self.LEFT_UP = False
                self.LEFT_DOWN = False
            else:
                self.RIGHT_DOWN = True
                self.RIGHT_UP = False
                self.LEFT_UP = False
                self.LEFT_DOWN =False

        if self.x+20 == x2 and self.y < y2+100 and self.y+20 > y2:
            if self.y < y2+50:
                self.LEFT_UP = True
                self.LEFT_DOWN = False
                self.RIGHT_DOWN = False
                self.RIGHT_UP = False
            else:
                self.LEFT_DOWN = True
                self.LEFT_UP = False
                self.RIGHT_DOWN = False
                self.RIGHT_UP = False

        if self.y < 0:
            if self.LEFT_UP:
                self.LEFT_UP = False
                self.LEFT_DOWN = True
                self.RIGHT_DOWN = False
                self.RIGHT_UP = False
            else:
                self.RIGHT_UP = False
                self.RIGHT_DOWN = True
                self.LEFT_UP = False
                self.LEFT_DOWN = False

        if self.y + 20 >= SCREEN_HEIGHT:
            if self.LEFT_DOWN:
                self.LEFT_DOWN = False
                self.LEFT_UP = True
                self.RIGHT_DOWN = False
                self.RIGHT_UP = False
            else:
                self.RIGHT_DOWN = False
                self.RIGHT_UP = True
                self.LEFT_DOWN = False
                self.LEFT_UP = False

    def draw(self):
        pygame.draw.rect(win,(255,255,255), (self.x,self.y,20,20))

def start_over():
    global score1,score2
    if obj.x < 0: 
        obj.x = SCREEN_WIDTH/2
        obj.y = SCREEN_HEIGHT/2+50
        score2 += 1
        obj.dir = random.randint(1,4)
        if obj.dir == 1:
            obj.LEFT_UP = True
            obj.LEFT_DOWN = False
            obj.RIGHT_DOWN = False
            obj.RIGHT_UP = False
        elif obj.dir == 2:
            obj.LEFT_DOWN = True
            obj.LEFT_UP = False
            obj.RIGHT_DOWN = False
            obj.RIGHT_UP = False
        elif obj.dir == 3:
            obj.RIGHT_UP = True
            obj.LEFT_UP = False
            obj.LEFT_DOWN = False
            obj.RIGHT_DOWN = False
        elif obj.dir == 4:
            obj.RIGHT_DOWN = True
            obj.LEFT_UP = False
            obj.LEFT_DOWN = False
            obj.RIGHT_UP = False

    elif obj.x > SCREEN_WIDTH:
        obj.x = SCREEN_WIDTH/2
        obj.y = SCREEN_HEIGHT/2+50
        score1 += 1
        obj.dir = random.randint(1,4)
        if obj.dir == 1:
            obj.LEFT_UP = True
            obj.LEFT_DOWN = False
            obj.RIGHT_DOWN = False
            obj.RIGHT_UP = False
        elif obj.dir == 2:
            obj.LEFT_DOWN = True
            obj.LEFT_UP = False
            obj.RIGHT_DOWN = False
            obj.RIGHT_UP = False
        elif obj.dir == 3:
            obj.RIGHT_UP = True
            obj.LEFT_UP = False
            obj.LEFT_DOWN = False
            obj.RIGHT_DOWN = False
        elif obj.dir == 4:
            obj.RIGHT_DOWN = True
            obj.LEFT_UP = False
            obj.LEFT_DOWN = False
            obj.RIGHT_UP = False

obj = ball()
vel = 20

while True:
    clock.tick(30)
    win.fill((0,0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    key = pygame.key.get_pressed()
    if key[pygame.K_UP] and y1 > 0:
        y1 -= vel
    if key[pygame.K_DOWN] and y1+100 < SCREEN_HEIGHT:
        y1 += vel
    # if key[pygame.K_w] and y2 > 0:
    #     y2 -= vel
    # if key[pygame.K_s] and y2 +100 < SCREEN_HEIGHT:
    #     y2 += vel
    if obj.y < y2+50:
        y2 -= vel
    if obj.y > y2+50:
        y2 += vel

    start_over()
    obj.move()
    obj.collide()
    draw()
    pygame.display.update()