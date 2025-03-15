import sys
from PySide6.QtCore import Slot
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout,
    QHBoxLayout, QPushButton, QMainWindow, QGridLayout
)


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        # é um widget generico, só serve para agrupar os widgets
        self.central_widget = QWidget()

        self.button = self.make_button("Button text")
        self.button.clicked.connect(self.secound_action_checked)

        # ja vem com um menu e um status bar
        self.setCentralWidget(self.central_widget)
        # Altera o nome da janela
        self.setWindowTitle("My beautiful window")

        self.button2 = QPushButton("Button text 2")
        self.button2.setStyleSheet(
            "background-color: black; color: white; font-size: 80px;")

        self.button3 = QPushButton("Button text 3")
        self.button3.setStyleSheet(
            "background-color: green; color: white; font-size: 150px;")

        # Para colocar os widgets na grade
        self.grid_layout = QGridLayout()

        # coloca o botão na primeira linha e primeira coluna
        self.grid_layout.addWidget(self.button, 1, 1, 1, 1)
        self.grid_layout.addWidget(self.button2, 1, 2, 1, 1)
        # rowSpan e columnSpan, para pegar mais de uma linha ou coluna
        self.grid_layout.addWidget(self.button3, 3, 1, 1, 2)

        # para setar meus widgets dentro do meu grid_layout
        self.central_widget.setLayout(self.grid_layout)

        # mostrar a status bar
        self.status_bar = self.statusBar()
        self.status_bar.showMessage("Status bar")

        self.menu = self.menuBar()
        self.first_menu = self.menu.addMenu("First menu")
        self.first_action = self.first_menu.addAction("First action")
        self.first_action.triggered.connect(self.change_status_bar_message)

        self.secound_menu = self.menu.addMenu("Secound menu")
        self.secound_action = self.secound_menu.addAction("Secound action")
        self.secound_action.setCheckable(True)
        self.secound_action.toggled.connect(self.secound_action_checked)
        self.secound_action.hovered.connect(self.secound_action_checked)

    @Slot()
    def change_status_bar_message(self):
        self.status_bar.showMessage("Você clicou no botão!")

    @Slot()
    def secound_action_checked(self):
        print('Is checked?:', self.secound_action.isChecked())

    def make_button(self, text):
        btn = QPushButton(text)
        btn.setStyleSheet(
            "font-size: 80px; background-color: black; color: white;")
        return btn


if __name__ == "__main__":
    # aplicação principal
    app = QApplication(sys.argv)

    # instancia a classe MyWindow
    window = MyWindow()

    # coloca ela na arvore de execução
    window.show()

    # loop da aplicação
    app.exec()
