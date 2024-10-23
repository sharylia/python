import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt

class SimpleWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.label = QLabel("Нажмите кнопку", self)
        self.button = QPushButton("Нажми на меня", self)

        self.label.setStyleSheet("font-size: 20px; color: blue;")
        self.button.setStyleSheet("background-color: lightgreen; font-size: 16px;")

        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        self.setLayout(layout)

        self.button.clicked.connect(self.change_text_and_style)

    def change_text_and_style(self):
        self.label.setText("Кнопка нажата!")
        self.button.setText("Нажата!")
        
        self.label.setStyleSheet("font-size: 20px; color: red;")
        self.button.setStyleSheet("background-color: yellow; font-size: 18px; color: black;")

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = SimpleWindow()
    window.setWindowTitle('Окно')
    window.setGeometry(100, 100, 300, 150)
    window.show()

    sys.exit(app.exec_())
