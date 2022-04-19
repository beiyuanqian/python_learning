# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/2/16}

import sys
import pygame
from settings import Settings
from ship import Ship
import game_functions as gf
from pygame.sprite import Group


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    # # 创建一个名为screen的显示窗口，这个游戏的所有图形元素都将在其中绘制。实参（1200，800）是一个元组，指定了游戏窗口的尺寸
    # screen = pygame.display.set_mode((1200, 800))
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # # 设置背景色
    # bg_color = (230, 230, 230,)

    # 创建一艘飞船
    ship = Ship(ai_settings, screen)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 开始游戏的主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        bullets.update()
        gf.update_screen(ai_settings, screen, ship, bullets)


run_game()
