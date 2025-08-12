import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel, QVBoxLayout, QWidget, QHBoxLayout)
from PyQt5.QtCore import QTimer, Qt, QTime

class Stopwatch(QWidget):
    def __init__(self):
        super().__init__()
        self.time = QTime(0, 0, 0, 0)
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)
        self.timer = QTimer(self)
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Stopwatch")

        vbox= QVBoxLayout()
        vbox.addWidget(self.time_label, alignment=Qt.AlignCenter)
       
        self.setLayout(vbox)

        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button, alignment=Qt.AlignCenter)
        hbox.addWidget(self.stop_button, alignment=Qt.AlignCenter)
        hbox.addWidget(self.reset_button, alignment=Qt.AlignCenter)

        vbox.addLayout(hbox)


        self.setStyleSheet("QPushButton { font-size:50px; } QLabel { font-size:120px; background-color: hsl(200, 100%, 85%); border-radius: 10px; }")
        self.setStyleSheet("QPushButton,QLabel { padding: 20px;font-weight: bold; }")

        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)
        self.timer.timeout.connect(self.update_dispaly)

    def start(self):
        self.timer.start(10)

    def stop(self):
        self.timer.stop()

    def reset(self):
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def update_dispaly(self):
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))
        
    def format_time(self, time):
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = time.msec() // 10
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch= Stopwatch()
    stopwatch.show()
    sys.exit(app.exec_())
            