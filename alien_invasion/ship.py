import pygame

class Ship():

    def __init__(self, ai_settings, screen):
        """初始化飞船，并设置它的起始位置。"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像，得到它的矩形。
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 在屏幕的底部中央启动每艘新船。
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        
        # 因为移动是像素用float储存
        self.center = float(self.rect.centerx)
        
        # 移动
        self.moving_right = False
        self.moving_left = False
        
    def update(self):
        """根据移动标志调整船的位置。"""
        # 更新飞船的中心（center）的值而不是rect
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
            
        # 从self.center更新rect对象。
        self.rect.centerx = self.center

    def blitme(self):
        """吧船停在当前位置"""
        self.screen.blit(self.image, self.rect)
