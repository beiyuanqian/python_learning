# -*- coding:utf-8 -*-
# auto：刘小涵  时间：{2022/2/16}

import sys
import pygame


def check_events(ship):
    """响应按键和鼠标事件"""
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        # 玩家单击游戏窗口的关闭按钮时，退出游戏
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def check_keydown_events(event, ship):
    """响应按键"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕，用背景色填充背景，该方法只接受一个参数，一种颜色
    screen.fill(ai_settings.bg_color)
    # 将飞船绘制到屏幕上，确保它出现在背景前面
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
