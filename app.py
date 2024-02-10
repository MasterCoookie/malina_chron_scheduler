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
        self.minute_freq_input = QLineEdit(self)

        starting_hour_label = QLabel('Starting Hour:', self)
        self.starting_hour_input = QLineEdit(self)

        ending_hour_label = QLabel('Ending Hour:', self)
        self.ending_hour_input = QLineEdit(self)

        weekdays_label = QLabel('Weekdays:', self)
        weekdays_names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'All']
        self.weekdays_checkboxes = [QCheckBox(name, self) for name in weekdays_names]

        generate_button = QPushButton('Generate', self)
        generate_button.clicked.connect(self.generate_cron)
        
        # layout.addWidget(header_label, 0, 2, 1, 1)
        layout.addWidget(minute_freq_label, 1, 0, 1, 1)
        layout.addWidget(self.minute_freq_input, 1, 1, 1, 1)
        layout.addWidget(starting_hour_label, 2, 0, 1, 1)
        layout.addWidget(self.starting_hour_input, 2, 1, 1, 1)
        layout.addWidget(ending_hour_label, 3, 0, 1, 1)
        layout.addWidget(self.ending_hour_input, 3, 1, 1, 1)
        layout.addWidget(weekdays_label, 4, 0, 1, 1)
        for i, checkbox in enumerate(self.weekdays_checkboxes):
            layout.addWidget(checkbox, 4, i+1, 1, 1)
        layout.addWidget(generate_button, 5, 2, 1, 4)

    def generate_cron(self):
        print('Generating cron...')
        minute_freq = int(self.minute_freq_input.text())
        starting_hour = int(self.starting_hour_input.text())
        ending_hour = int(self.ending_hour_input.text())
        
        if self.weekdays_checkboxes[-1].isChecked():
            weekdays = [True] * 7
        else:
            weekdays = [checkbox.isChecked() for checkbox in self.weekdays_checkboxes][:-1]
        print(minute_freq, starting_hour, ending_hour, weekdays)


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
