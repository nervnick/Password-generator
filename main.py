from random import choice
import string
import sys
import os

try:
    from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                            QHBoxLayout, QLineEdit, QPushButton, 
                            QLabel, QButtonGroup)
    from PyQt6.QtCore import Qt, QSize
    
except:
    os.system("pip install pyqt6")
    from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, 
                                QHBoxLayout, QLineEdit, QPushButton, 
                                QLabel, QButtonGroup)
    from PyQt6.QtCore import Qt, QSize

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Генератор паролей")
        self.setFixedSize(QSize(400, 500))

        self.length_text = QLabel("Введите длину пароля: ")
        self.length = QLineEdit()
        self.length.setMaximumHeight(50)
        self.length.textChanged.connect(self.check_input)

        self.punc = False
        self.punc_text = QLabel("Использовать специальные символы?")
        self.punc_true = QPushButton("Да")
        self.punc_true.setCheckable(True)
        self.punc_true.setMaximumHeight(50)
        self.punc_false = QPushButton("Нет")
        self.punc_false.setCheckable(True)
        self.punc_false.setMaximumHeight(50)

        self.punc_group = QButtonGroup()
        self.punc_group.addButton(self.punc_true, 1)
        self.punc_group.addButton(self.punc_false, 2)

        self.punc_group.idClicked.connect(self.on_click_punc)

        self.btn = QPushButton("Сгенерировать")
        self.btn.setEnabled(False)
        self.btn.setMaximumHeight(50)
        self.btn.clicked.connect(self.generate)

        self.password = QLineEdit("Тут появится сгенерированный пароль")
        self.password.setMaximumHeight(50)

        layout = QVBoxLayout()
        line = QHBoxLayout()
        len = QVBoxLayout()
        len.setContentsMargins(10, 0, 10, 20)
        punc = QVBoxLayout()
        punc.setContentsMargins(0, 10, 0, 40)
        line.addWidget(self.punc_true)
        line.addWidget(self.punc_false)
        len.addWidget(self.length_text)
        len.addWidget(self.length)
        punc.addWidget(self.punc_text)
        punc.addLayout(line)
        layout.addLayout(len)
        layout.addLayout(punc)
        layout.addWidget(self.btn)
        layout.addWidget(self.password)

        self.setLayout(layout)

    def on_click_punc(self):
        if self.punc_group.checkedId() == 1:
            self.punc = True
        else:
            self.punc = False
        self.password.setText("Тут появится сгенерированный пароль")

    def check_input(self):
        try:
            int(self.length.text())
            self.btn.setEnabled(True)
        except ValueError:
            self.btn.setEnabled(False)

    def generate(self):
        characters = string.ascii_letters + string.digits
        if self.punc:
            characters += string.punctuation
        password = "".join(choice(characters) for i in range(int(self.length.text())))
        self.password.clear()
        self.password.setText(password)

if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.setStyleSheet(open('style.css').read())
    window.show()
    sys.exit(app.exec())