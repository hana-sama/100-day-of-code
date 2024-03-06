
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox
from datetime import datetime
import sys
class SpeedCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Speed Calculator")
        grid = QGridLayout()

        # Create widgets
        distance_label = QLabel("distance:")
        self.distance_line_edit = QLineEdit()
        
        self.combobox = QComboBox()
        self.combobox.addItems(["Metric (km)","Imperial (miles)"])
         
        time_label = QLabel("Time(hours):")
        self.time_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Speed?")
        calculate_button.clicked.connect(self.calaculate_speed)
        self.output_label = QLabel("")
        # Add widgets
        grid.addWidget(distance_label, 0, 0)
        grid.addWidget(self.distance_line_edit, 0, 1)
        grid.addWidget(self.combobox, 0, 2)
        
        grid.addWidget(time_label, 1, 0)
        grid.addWidget(self.time_line_edit, 1, 1)

        grid.addWidget(calculate_button, 2, 1)
        grid.addWidget(self.output_label, 3, 1)

        self.setLayout(grid)

    def calaculate_speed(self):
        distance = float(self.distance_line_edit.text())
        time = float(self.time_line_edit.text())
        speed = distance/time
        if self.combobox.currentText() == "Metric (km)":
            speed = round(speed, 2)
            unit = 'km/h'
        if self.combobox.currentText() == "Imperial (miles)":
            speed = round(speed * 0.62137119223733, 2)
            unit = 'mph'
        self.output_label.setText(f"Average speed: {speed} {unit}")
        

app = QApplication(sys.argv)
speed_calculator = SpeedCalculator()
speed_calculator.show()
sys.exit(app.exec())
