import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from chap3.ex64.models.officialEmployee import officialEmployee
from chap3.ex64.models.staffManagement import staffManagement
from chap3.ex64.models.temporaryEmployee import temmporaryEmployee
from chap3.ex64.ui.MainWindow import Ui_MainWindow


class MainWindow64Ex(Ui_MainWindow):
    def __init__(self):
        self.sm = staffManagement()
        self.selected_index = -1

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save)
        self.pushButtonRemove.clicked.connect(self.process_remove)
        self.pushButtonSearchIDCard.clicked.connect(self.process_search_id_card)
        self.pushButtonFilterYear.clicked.connect(self.process_filter_year)
    def process_save(self):
        if self.checkBox.isChecked():
            emp = officialEmployee()
        else:
            emp = temmporaryEmployee()
        emp.id = self.lineEditID.text()
        emp.idcard = self.lineEditIDCard.text()
        emp.name = self.lineEditName.text()
        emp.birthday = self.lineEditBirthday.text()
        self.sm.add_employee(emp)
        self.display_employee_layout()
    def process_remove(self):
        if self.selected_index == -1:  # no selection
            return
        self.sm.database.pop(self.selected_index)
        self.display_employee_layout()
    def process_search_id_card(self):
        search = self.lineEditSearchIDCard.text().strip()
        for emp in self.sm.database:
            if emp.idcard == search:
                QMessageBox.warning(self.MainWindow, 'Search Result', f'Employee {emp.name} - {search}')
                return
        QMessageBox.warning(self.MainWindow, 'Search Result', 'ID Card not found')
    def process_filter_year(self):
        filter = self.lineEditFilterYear.text().strip()
        for emp in self.sm.database:
            if emp.birthday.endswith(filter):
                QMessageBox.warning(self.MainWindow, 'Search Result', f'Employee {emp.name} - {filter}')
                return
            QMessageBox.warning(self.MainWindow, 'Search Result', 'Year not found')
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def display_employee_layout(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.sm.database)):  #qtrong trong bo nho: self.list
            x = self.sm.database[i]
            title = f'{x.id}-{x.name}-{x.birthday}'
            btn = QPushButton(text = title)
            if isinstance(x, officialEmployee):
                btn.setStyleSheet('background-color: rgb(255, 85, 127);')
            else:
                pass
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail,i))  #hien thi nv dong thu i

    def show_detail(self,i):
        self.selected_index = i
        emp = self.sm.database[i]
        selected_button = self.verticalLayoutButton.itemAt(i).widget()
        selected_button.setStyleSheet('background-color: rgb(240, 128, 128);')