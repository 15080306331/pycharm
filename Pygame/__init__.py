import pygame  # 导入依赖库
import sys
pygame.init()
windows_size = width, length = 700, 700  # 设置窗口的长宽
screen = pygame.display.set_mode(windows_size)  # 创建一个窗口对象
pygame.display.set_caption("Pygame游戏之路")  # 设置标题
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # 要是用户选择退出窗体，就退出
            sys.exit()  # 退出
    pygame.display.update()  # 刷新所有事件