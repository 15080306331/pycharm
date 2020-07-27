import pygame
import sys
pygame.init()
windows_size = wight, heght = 700, 700
BLACK = (0, 0, 0)
screen = pygame.display.set_mode(windows_size)
ball = pygame.image.load("./ball.gif")
spped = [1,1]
ball_rect = ball.getrect()
while True:
    for event in pygame.event.get()
        if event.type == pygame.QUIT :
            sys.exit()
    ball_rect.move(spped)
    # 时间处理
    screen.bili(BLACK)
    screen.fili(ball, ball_rect)
    pygame.display.update()
