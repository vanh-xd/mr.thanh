import functools
import random

from PyQt6.QtWidgets import QPushButton, QMessageBox

from chap2.ex38.ui.MainWindow import Ui_MainWindow


class MainWindow38Ex(Ui_MainWindow):
    def __init__(self):
        self.list = []
        self.selected_index = -1
        self.click_count = 0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonRandom.clicked.connect(self.process_random)
        self.pushButtonAdd.clicked.connect(self.process_add)
        self.pushButtonAsc.clicked.connect(self.process_asc)
        self.pushButtonDesc.clicked.connect(self.process_desc)
        self.pushButtonCountK.clicked.connect(self.process_count_k)
        self.pushButtonSumOfPerfectNum.clicked.connect(self.process_sum_perfectnum)
        self.pushButtonDelAnElement.clicked.connect(self.process_del_element)
        self.pushButtonDelNegativeNum.clicked.connect(self.process_del_negativenum)
        self.pushButtonDelAll.clicked.connect(self.process_del_all)

    def draw_button_into_box(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.list)):
            x = self.list[i]
            title = f'{x}'
            btn = QPushButton(text = title)
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail, i))
    def show_detail(self, i):
        for j in range(len(self.list)):
            button = self.verticalLayoutButton.itemAt(j).widget()
            button.setStyleSheet('')  #reset to default color
        self.selected_index = i
        selected_button = self.verticalLayoutButton.itemAt(i).widget()
        selected_button.setStyleSheet('background-color: rgb(240, 128, 128);')
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def process_random(self):
        self.list.clear()
        for i in range(10):
            x = random.randint(-100, 100)
            self.list.append(x)
        self.draw_button_into_box()  #refresh giao dien ui
    def process_add(self):
        x = random.randint(-100, 100)
        self.list.append(x)
        self.draw_button_into_box()
    def process_asc(self):
        self.list.sort()
        self.draw_button_into_box()
    def process_desc(self):
        self.list.reverse()
        self.draw_button_into_box()
    def process_count_k(self):
        k = self.lineEditEnterK.text()
        if not k:
            self.show_msg_box('enter K first')
            return

        count = 0
        k = int(self.lineEditEnterK.text())
        for i in self.list:
            if i == k:
                count += 1
        self.lineEditEnterK.setText(f'{k} appears {count} times')
        self.draw_button_into_box()
    def show_msg_box(self, message):
        msg_box = QMessageBox(self.MainWindow)
        msg_box.setWindowTitle('INPUT REQUIRED')
        msg_box.setText(message)
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()
    def check_perfectnum(self, n):
        if n<0:
            return False
        else:
            divisors = []
            for i in range(1,n):
                if n%i == 0:
                    divisors.append(i)
            sum_divisors = sum(divisors)
            return sum_divisors == n
    def process_sum_perfectnum(self):
        sum_perfectnum = 0
        for x in self.list:
            if self.check_perfectnum(x):
                sum_perfectnum += x
        self.lineEditEnterK.setText(f'sum of perfect numbers = {sum_perfectnum}')
        self.draw_button_into_box()
    def process_del_element(self):
        if self.selected_index == -1:  # no selection
            return
        self.list.pop(self.selected_index)
        self.draw_button_into_box()
    def process_del_negativenum(self):
        for x in range(len(self.list) -1, -1, -1):
            if self.list[x] < 0:
                self.list.pop(x)
        self.draw_button_into_box()
    def process_del_all(self):
        self.list.clear()
        self.selected_index = -1
        self.draw_button_into_box()