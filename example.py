from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
from datetime import datetime
import sys
class AgeCalculator(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()

        # Create widgets
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()
        
        birth_date_label = QLabel("Date of Birth MM/DD/YYYY:")
        self.birth_date_line_edit = QLineEdit()

        calculate_button = QPushButton("Calculate Age?")
        calculate_button.clicked.connect(self.calaculate_age)
        self.output_label = QLabel("")
        # Add widgets
        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        
        grid.addWidget(birth_date_label, 1, 0)
        grid.addWidget(self.birth_date_line_edit, 1, 1)

        grid.addWidget(calculate_button, 2, 0, 1, 2)
        grid.addWidget(self.output_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calaculate_age(self):
        current_year = datetime.now().year
        birth_year = self.birth_date_line_edit.text()
        birth_year = datetime.strptime(birth_year, "%m/%d/%Y").date().year
        age = current_year - birth_year
        name = self.name_line_edit.text()
        self.output_label.setText(f"{name.capitalize()} is {age} years old.")

app = QApplication(sys.argv)
age_calculator = AgeCalculator()
age_calculator.show()
sys.exit(app.exec())
