from pathlib import Path
import os
from kivy.uix.widget import Widget
import pickle
import threading
import struct
import time
from kivy.graphics import *
from kivy.core.camera import Camera
from kivy.graphics.texture import Texture
from kivy.properties import StringProperty, ObjectProperty, NumericProperty, ReferenceListProperty
from kivy.lang import Builder
from kivy.config import Config
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
import kivy
import socket

# import cv2

Builder.load_file('test.kv')


class fscreen(Widget):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	def push_me(self):

		self.ids.output.text = self.ids.output.text + '\n' + self.ids.input.text


class secscreen(Widget):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		pass


class thscreen(Widget):

	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		pass


class theapp(App):
	def build(self):

		self.screenm = ScreenManager()  # (transition=FadeTransition())

		self.fscreen = fscreen()
		screen = Screen(name="first screen")
		screen.add_widget(self.fscreen)
		self.screenm.add_widget(screen)

		self.secscreen = secscreen()
		screen = Screen(name="secondscreen")
		screen.add_widget(self.secscreen)
		self.screenm.add_widget(screen)

		self.thscreen = thscreen()
		screen = Screen(name="thirdscreen")
		screen.add_widget(self.thscreen)
		self.screenm.add_widget(screen)
		return self.screenm


if __name__ == "__main__":
	theapp = theapp()  # LISTING THREAD
	theapp.run()
