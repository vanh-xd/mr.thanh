import random

from PyQt6.QtWidgets import QMessageBox

from chap1_function.ex24_baikho.ui.MainWindow import Ui_MainWindow


class MainWindow24Ex(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.machine_money = 100
        self.player_money = 100
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonRandom.clicked.connect(self.process_random)
        self.pushButtonNewGame.clicked.connect(self.process_new_game)
    def process_random(self):
        if self.player_money < 30:
            self.show_error("you don't have enough $, POOR BJTCH!!" )
            return
        self.player_money -= 30
        self.machine_money += 30

        box1=random.randint(0,9)
        self.labelBox1.setText(f'{box1}')
        if box1 == 7:
            self.player_money += 100 + 0.5*self.machine_money
            self.machine_money -= 0.5*self.machine_money
            return

        box2 = random.randint(0, 10)
        self.labelBox2.setText(f'{box2}')
        if box2 == 7:
            self.player_money += 30 + 0.5*self.machine_money
            self.machine_money -= 0.5 * self.machine_money
            return

        box3 = random.randint(0, 11)
        self.labelBox3.setText(f'{box3}')
        if box3 == 7:
            self.player_money += 10
            return

        self.money_display()

    def process_new_game(self):
        self.labelBox1.clear()
        self.labelBox2.clear()
        self.labelBox3.clear()
        self.machine_money = 100
        self.player_money = 100
        self.money_display()
    def money_display(self):
        self.lineEditMachineMoney.setText(f'{self.machine_money}')
        self.lineEditPlayerMoney.setText(f'{self.player_money}')
    def show_error(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle('ERROR')
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()