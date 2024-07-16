from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton
import sys
from datetime import datetime

class AgeCalculator(QWidget):
# QWidget creates GUI windows
    def __init__(self):
        super().__init__()  # return parent of the class i.e. QWidget in this case
        self.setWindowTitle("Age Calculator")
        grid = QGridLayout()
        name_label = QLabel("Name:")
        self.name_line_edit = QLineEdit()
        dob_label = QLabel("DoB in MM/DD/YYYY:")
        self.dob_line_edit = QLineEdit()

        calc_btn = QPushButton("Calculate age")
        calc_btn.clicked.connect(self.calc_age)
        self.op_label = QLabel("")

        grid.addWidget(name_label, 0, 0)
        grid.addWidget(self.name_line_edit, 0, 1)
        grid.addWidget(dob_label, 1, 0)
        grid.addWidget(self.dob_line_edit, 1, 1)
        grid.addWidget(calc_btn, 2, 0, 1, 2)
        grid.addWidget(self.op_label, 3, 0, 1, 2)

        self.setLayout(grid)

    def calc_age(self):
        curr_year = datetime.now().year
        date_of_birth = self.dob_line_edit.text()
        year = datetime.strptime(date_of_birth, "%m/%d/%Y").date().year
        age = curr_year - year
        name = self.name_line_edit.text()
        self.op_label.setText(f"{name} is {age} years old")
