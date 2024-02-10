from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QLineEdit, QLabel
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

        header_label = QLabel('Scheduler', self)
        header_label.setStyleSheet('font-size: 20px; font-weight: bold;')

        minute_freq_label = QLabel('Minute Frequency:', self)
        minute_freq_input = QLineEdit(self)

        starting_hour_label = QLabel('Starting Hour:', self)
        starting_hour_input = QLineEdit(self)

        ending_hour_label = QLabel('Ending Hour:', self)
        ending_hour_input = QLineEdit(self)

        
        layout.addWidget(header_label, 0, 2, 1, 1)
        layout.addWidget(minute_freq_label, 1, 0, 1, 1)
        layout.addWidget(minute_freq_input, 1, 1, 1, 1)
        layout.addWidget(starting_hour_label, 2, 0, 1, 1)
        layout.addWidget(starting_hour_input, 2, 1, 1, 1)
        layout.addWidget(ending_hour_label, 3, 0, 1, 1)
        layout.addWidget(ending_hour_input, 3, 1, 1, 1)

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
