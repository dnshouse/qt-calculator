import sys
import math
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Button:
    def __init__(self, text, results):
        self.b = QPushButton(text)
        self.text = text
        self.results = results
        self.b.clicked.connect(lambda: self.handle_input(self.text))

    def handle_input(self, v):
        if v == "=":
            res = eval(self.results.text())
            self.results.setText(str(res))
        elif v == "AC":
            self.results.setText("")
        elif v == "√":
            current_value = self.results.text()
            res = math.sqrt(float(current_value))
            self.results.setText(str(res))
        elif v == "DEL":
            current_value = self.results.text()
            res = current_value[:-1]
            self.results.setText(str(res))
        else:
            current_value = self.results.text()
            res = current_value + str(v)
            self.results.setText(str(res))


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.create_app()

    def create_app(self):
        grid = QGridLayout()
        results = QLineEdit()

        buttons = [
            "AC", "√", "DEL", "/",
            7, 8, 9, "*",
            4, 5, 6, "-",
            1, 2, 3, "+",
            0, ".", "="
        ]

        grid.addWidget(results, 0, 0, 1, 4)

        row = 1
        col = 0

        for button in buttons:
            if col > 3:
                col = 0
                row += 1

            button_object = Button(str(button), results)

            if button == 0:
                grid.addWidget(button_object.b, row, col, 1, 2)
                col += 1
            else:
                grid.addWidget(button_object.b, row, col, 1, 1)

            col += 1

        self.setLayout(grid)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec())





