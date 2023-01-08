from kivymd.app import MDApp
from kivy.core.window import Window
from kivymd.theming import ThemeManager

Window.size = (375, 812)


class MainApp(MDApp):
    def build(self):
        self.title='KivyMD Dashboard'
        self.theme_cls.theme_style = "Light"
        self.theme_cls = ThemeManager
        # self.theme_cls.primary_palette = "Custom"


MainApp().run()