from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang import Builder


class PatientInformation(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        
        title_Label = Builder.load_file('patientinfoscreen.kv')
        
        screen.add_widget(title_Label)
        return screen


    def medicalrecord(self, root):
        self.root.ids.sc_m.current = 'patientinfoscreen'

PatientInformation().run()
