from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.lang import Builder


class MedicalRecord(MDApp):

    def build(self):
        screen = Screen()
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Yellow"
        
        title_Label = Builder.load_file('medicalrecord.kv')
        
        screen.add_widget(title_Label)
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
                                    ("Điện tim trường", "10h50", "11h30", "Phòng 407, tòa C" ),
                                    ("Chụp X-quang", "10h20", "12h", "Phòng 302, tòa B")
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
