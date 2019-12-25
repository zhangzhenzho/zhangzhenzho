import sys

import pygame

from bullet import Bullet

def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """设置按键的收发命令"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
        
def check_keyup_events(event, ship):
    """响应命令"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False

def check_events(ai_settings, screen, ship, bullets):
    """响应按键和鼠标"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
            
def fire_bullet(ai_settings, screen, ship, bullets):
    """没到达子弹上限就开枪"""
    # 创建新项目符号，添加到项目符号组
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def update_screen(ai_settings, screen, ship, bullets):
    """更新屏幕上的图像，然后翻到新屏幕。"""
    # 重新绘制屏幕，每个都通过循环。
    screen.fill(ai_settings.bg_color)
    
    # 重绘所有子弹，在飞船和外星人后面。
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()

    # 使最近绘制的屏幕可见。
    pygame.display.flip()
    
def update_bullets(bullets):
    """更新子弹位置，去掉旧子弹。"""
    # 更新子弹位置
    bullets.update()

    # 把消失的子弹扔掉。
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
