from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang import Builder


class MedicalRecord(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Green"
        
        title_Label = Builder.load_file('trackingstatus.kv')
        
        screen.add_widget(title_Label)
        data_table = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(0.9, 0.6),
                                 background_color=(0, 0, 0),
                                 check = True,
                                 rows_num=10,
                                 column_data=[
                                     ("MSBN", dp(25)),
                                     ("Tên bệnh nhân", dp(30)),
                                     ("Tên xét nghiệm", dp(25))
        ],
                            row_data=[
                                    ("123456", "Nguyễn Văn A", "Điện tim trường"),
                                    ("234567", "Trần Văn B", "Chụp X-quang"),
                                    ("345678", "Nguyễn Thị C", "Xét nghiệm máu")
        ]
        )
        data_table.bind(on_row_press=self.on_row_press)
        data_table.bind(on_check_press=self.on_check_press)
        screen.add_widget(data_table)
        return screen

    def on_row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        print(instance_table, current_row)


MedicalRecord().run()
