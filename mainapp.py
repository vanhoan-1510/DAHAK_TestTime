from kivymd.app import MDApp
# from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.pickers import MDDatePicker
from kivy.core.window import Window

Window.size = (375, 750)
            
class MainScreen(Screen):
    pass


class PatientInfomationScreen(Screen):
    pass


class NavigationBar(Screen):
    pass

class StaffInfoScreen(Screen):
    pass

    

sm = ScreenManager()
sm.add_widget(MainScreen(name='mainscreen'))
sm.add_widget(PatientInfomationScreen(name='information'))
sm.add_widget(NavigationBar(name='navigationbar'))
sm.add_widget(StaffInfoScreen(name='staff_information'))

class Testapp(MDApp):

    def build(self):
        screen = Builder.load_file('mainapp.kv')
        # self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "DeepOrange"
        
        return screen
    
    # def on_save(self, instance, value, date_range):
	# # print(instance, value, date_range)
	#     self.root.ids.date_label.text = str(value)
        
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        # date_dialog.bind(on_save=self.on_save)
        date_dialog.open()
        
        
    def show_patient_data(self):
        data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(0.9, 0.6),
                                 background_color=(0, 0, 0),
                                 rows_num=10,
                                 column_data=[
                                     ("Tên xét nghiệm", dp(30)),
                                     ("Thời gian lấy mẫu", dp(17)),
                                     ("Thời gian nhận kết quả", dp(20)),
                                     ("Địa điểm nhận", dp(25))
        ],
            row_data=[
            ("Định lượng glucoso trong máu", "10h", "11h45", "Phòng 501, tòa B"),
            ("Điện tim trường", "10h50", "11h30", "Phòng 407, tòa C"),
            ("Chụp X-quang", "10h20", "12h", "Phòng 302, tòa B")
        ]
        )
        data_table.bind(on_row_press=self.on_row_press)
        data_table.bind(on_check_press=self.on_check_press)
        # self.root..ids.navigationbar.ids.bottim_nv.ids.medicalrecord.add_widget(data_table)


Testapp().run()
