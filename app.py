from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLineEdit, QLabel, QCheckBox
from PyQt6.QtCore import QSettings

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Python Cron Job Scheduler')
        self.setGeometry(100, 100, 400, 300)

        self.schedule_widget = ScheduleWidget(self)
        self.settings_widget = SettingsWidget(self)

        self.setCentralWidget(self.schedule_widget)


class ScheduleWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout(self)

        # header_label = QLabel('Scheduler', self)
        # header_label.setStyleSheet('font-size: 20px; font-weight: bold;')

        minute_freq_label = QLabel('Minute Frequency:', self)
        minute_freq_input = QLineEdit(self)

        starting_hour_label = QLabel('Starting Hour:', self)
        starting_hour_input = QLineEdit(self)

        ending_hour_label = QLabel('Ending Hour:', self)
        ending_hour_input = QLineEdit(self)

        weekdays_label = QLabel('Weekdays:', self)
        weekdays_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'All']
        weekdays_checkboxes = [QCheckBox(name, self) for name in weekdays_names]

        generate_button = QPushButton('Generate', self)
        
        # layout.addWidget(header_label, 0, 2, 1, 1)
        layout.addWidget(minute_freq_label, 1, 0, 1, 1)
        layout.addWidget(minute_freq_input, 1, 1, 1, 1)
        layout.addWidget(starting_hour_label, 2, 0, 1, 1)
        layout.addWidget(starting_hour_input, 2, 1, 1, 1)
        layout.addWidget(ending_hour_label, 3, 0, 1, 1)
        layout.addWidget(ending_hour_input, 3, 1, 1, 1)
        layout.addWidget(weekdays_label, 4, 0, 1, 1)
        for i, checkbox in enumerate(weekdays_checkboxes):
            layout.addWidget(checkbox, 4, i+1, 1, 1)
        layout.addWidget(generate_button, 5, 2, 1, 4)

class SettingsWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setup_ui()

    def setup_ui(self):
        layout = QGridLayout(self)
        

app = QApplication([])
window = MainWindow()
window.show()
app.exec()
