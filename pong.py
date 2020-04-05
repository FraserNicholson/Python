import pygame
import random

pygame.init()

width = 600
height = 500

win = pygame.display.set_mode((width, height))
#defines a game window

pygame.display.set_caption("Pong")
#defines the game title

p1x = 10
p1y = 225
p1w = 10
p1h = 50
#controls the position and shape of the left paddle

p2x = 580
p2y = 225
p2w = 10
p2h = 50
#controls the position and shape of the right paddle

bx = 300
by = 247
br = 6

player1Score = 0
player2Score = 0
font = pygame.font.SysFont('Arial', 30, True)


class paddle(object):

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 15
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        #initial parameters of the paddle

    def draw(self, win):
        pygame.draw.rect(win, (255, 255, 255),
                         (self.x, self.y, self.width, self.height))


class Ball(object):

    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.velx = 13*random.choice([-1, 1])
        self.vely = 13*random.choice([-1, 1])
        self.rect = pygame.Rect(self.x, self.y, self.radius, self.radius)
        #initital parameters of the ball

    def update(self):
        global player1Score, player2Score
        self.x += self.velx
        self.y += self.vely
        #trajectory of the ball
        if self.y <= 0 or self.y >= height:
            self.vely *= -1
        if self.x <= 0:
            player2Score += 1
            ball.restart()
        if self.x >= width:
            player1Score += 1
            ball.restart()
        #boundary conditions of the ball
        if paddle1.x <= self.x <= paddle1.x + 10 and paddle1.y <= self.y <= paddle1.y + 50:
            self.velx *= -1
        if paddle2.x <= self.x <= paddle2.x + 10 and paddle2.y <= self.y <= paddle2.y + 50:
            self.velx *= -1
        #when the ball hits either of the paddles

    def restart(self):
        self.x = bx
        self.y = by
        self.velx = 13*random.choice([-1, 1])
        self.vely = 13*random.choice([-1, 1])
        #when the ball passes a paddle

    def draw(self, win):
        pygame.draw.circle(win, (255, 255, 255),
                           (self.x, self.y), self.radius)


def move():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.y > 0:
        paddle1.y -= paddle1.vel
    if keys[pygame.K_s] and paddle1.y < height:
        paddle1.y += paddle1.vel
    if keys[pygame.K_UP] and paddle2.y > 0:
        paddle2.y -= paddle2.vel
    if keys[pygame.K_DOWN] and paddle2.y < height:
        paddle2.y += paddle2.vel
    #the movement of the paddles


def redrawGameWindow():
    win.fill((0, 0, 0))
    text = font.render(str(player1Score) + ":" +
                       str(player2Score), 1, (255, 255, 255))
    win.blit(text, (282, 20))
    paddle1.draw(win)
    paddle2.draw(win)
    ball.draw(win)
    pygame.draw.line(win, (255, 255, 255), (300, 0), (300, 500))
    pygame.display.update()


paddle1 = paddle(p1x, p1y, p1w, p1h)
paddle2 = paddle(p2x, p2y, p2w, p2h)
ball = Ball(bx, by, br)


def main():
    run = True

    while run:
        pygame.time.delay(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        move()
        ball.update()
        redrawGameWindow()

    pygame.quit()


main()
