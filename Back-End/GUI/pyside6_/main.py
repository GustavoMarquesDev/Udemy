import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QHBoxLayout, QPushButton, QMainWindow, QGridLayout
)

app = QApplication(sys.argv)  # aplicação principal
window = QMainWindow()
central_widget = QWidget()  # é um widget generico, só serve para agrupar os widgets
window.setCentralWidget(central_widget)  # ja vem com um menu e um status bar
window.setWindowTitle("My beautiful window")  # Altera o nome da janela

button = QPushButton("Button text")
button.setStyleSheet("background-color: red; color: white; font-size: 20px;")

button2 = QPushButton("Button text 2")
button2.setStyleSheet(
    "background-color: black; color: white; font-size: 80px;")

button3 = QPushButton("Button text 3")
button3.setStyleSheet(
    "background-color: green; color: white; font-size: 150px;")

# layout = QVBoxLayout() # Para colocar os widgets na vertical
# layout = QHBoxLayout()  # Para colocar os widgets na horizontal
layout = QGridLayout()  # Para colocar os widgets na grade

# coloca o botão na primeira linha e primeira coluna
layout.addWidget(button, 1, 1, 1, 1)
layout.addWidget(button2, 1, 2, 1, 1)
# rowSpan e columnSpan, para pegar mais de uma linha ou coluna
layout.addWidget(button3, 3, 1, 1, 2)

# para setar meus widgets dentro do meu layout
central_widget.setLayout(layout)


@Slot()
def slot_example(status_bar):
    def inner():
        status_bar.showMessage("Você clicou no botão!")
    return inner


@Slot()
def other_slot(checked):
    print('Is checked?:', checked)


@Slot()
def third_slot(action):
    def inner():
        other_slot(action.isChecked())
    return inner


# mostrar a status bar
status_bar = window.statusBar()
status_bar.showMessage("Status bar")

menu = window.menuBar()
first_menu = menu.addMenu("First menu")
first_action = first_menu.addAction("First action")
first_action.triggered.connect(slot_example(status_bar))

secound_action = first_menu.addAction("Secound action")
secound_action.setCheckable(True)
secound_action.toggled.connect(other_slot)
secound_action.hovered.connect(third_slot(secound_action))

button.clicked.connect(third_slot(secound_action))

window.show()
app.exec()  # loop da aplicação
