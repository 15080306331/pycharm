#  这个python文件将控制pygame壁球的节奏
import pygame
import sys
pygame.init()  # 初始化pygame
windows_size = width, length = 700, 700  # 设置窗口的长宽
fps = 300  # 每一秒的帧数
speed = [1, 1]  # 设置速度
winodws_background = (0, 0, 0)  # 设置背景
screen = pygame.display.set_mode(windows_size)  # 创建一个窗口对象
clock = pygame.time.Clock()  # 操作时间的对象
ball = pygame.image.load("PYG02-ball.gif")
ball_rect = ball.get_rect()


pygame.display.set_caption("Pygame游戏之路")  # 设置标题
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 要是用户选择退出窗体，就退出
            sys.exit()  # 退出
    ball_rect = ball_rect.move(speed[0], speed[1])
    if ball_rect.left < 0 or ball_rect.right > width :
        speed[0] = -speed[0]
    if ball_rect.top < 0 or ball_rect.bottom > length:
        speed[1] = -speed[1]
    screen.fill(winodws_background)  # 绘制背景色
    screen.blit(ball, ball_rect)  # 将小球绘制在他已经移动的矩形图像
    pygame.display.update()  # 刷新所有事件
    clock.tick(fps)