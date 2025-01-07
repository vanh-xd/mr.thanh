import functools
import random

from PyQt6.QtWidgets import QPushButton

from chap2.ex39.ui.MainWindow import Ui_MainWindow


class MainWindow39Ex(Ui_MainWindow):
    def __init__(self):  #mac dinh khoi tao(constructor) 1 cai gi do
        self.list=[]  #store the list of button values
        self.selected_index = -1  #-1 nghia la chua chon gi, day la luat
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonRandom.clicked.connect(self.process_random)
        self.pushButtonDelete.clicked.connect(self.process_del)
        self.pushButtonAdd.clicked.connect(self.process_add)
        self.pushButtonUpdate.clicked.connect(self.process_update)
        self.pushButtonAscSort.clicked.connect(self.process_asc)
        self.pushButtonDescSort.clicked.connect(self.process_desc)
        self.pushButtonRemove.clicked.connect(self.process_remove)
    def process_add(self):
        x = random.randint(0,10)
        self.list.append(x)  #append new value to the list
        self.draw_button_into_box()
    def process_update(self):
        if self.selected_index == -1:  #no button selected
            return
        self.list[self.selected_index] //= 10
        self.draw_button_into_box()
    def process_del(self):
        if self.selected_index == -1:  #no selection
            return
        self.list.pop(self.selected_index)
        self.draw_button_into_box()
    def process_random(self):
        n=int(self.lineEditNumber.text())
        self.list.clear()
        for i in range(n):
            x = random.randint(-100,100)
            self.list.append(x)  #luu trong bo nho RAM
        self.draw_button_into_box()
    def process_asc(self):
        self.list.sort()
        self.draw_button_into_box()  #refresh the Ui
    def process_desc(self):
        self.list.sort(reverse=True)
        self.draw_button_into_box()  #refresh the Ui
    def process_remove(self):
        self.list.clear()
        self.selected_index = -1
        self.draw_button_into_box()
    def draw_button_into_box(self):  #tao gtri ngau nhien --> tao tac vu tren giao dien
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.list)):  #qtrong trong bo nho: self.list
            x = self.list[i]
            title = f'{x}'
            btn = QPushButton(text = title)
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail,i))
    def show_detail(self,i):
        self.selected_index = i
        self.lineEditNumber.setText(f'{self.list[i]}')
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())