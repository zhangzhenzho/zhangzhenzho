class Settings():
    """一个类，用于存储外星入侵的所有设置。"""

    def __init__(self):
        """初始化游戏的设置。"""
        # Screen settings.
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 屏幕设置.
        self.ship_speed_factor = 1.5

        # 项目符号设置.
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3
