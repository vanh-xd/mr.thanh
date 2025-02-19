import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from chap4.ex85.ui.AssetMainWindow import Ui_MainWindow
from chap4.ex85.libs.JsonFileFactory import JsonFileFactory
from chap4.ex85.models.asset import Asset



class AssetMainWindowEx(Ui_MainWindow):
    def __init__(self):
        self.sm = None
        self.selected_index = -1

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        self.load_assets()
        self.display_asset_layout()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save)
        self.pushButtonRemove.clicked.connect(self.process_remove)
        self.pushButtonSearchIDCard.clicked.connect(self.process_search_id_card)
        self.pushButtonFilterYear.clicked.connect(self.process_filter_year)
    def process_save(self):
        pass
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

    def display_asset_layout(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.assets)):  #qtrong trong bo nho: self.list
            x = self.assets[i]
            title = f'{x.assetID}-{x.assetName}-{x.importYear}\t{x.value}'
            btn = QPushButton(text = title)
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail,i))  #hien thi nv dong thu i

    def show_detail(self,i):
        self.selected_index = i
        at = self.assets[i]
        self.lineEditID.setText(at.assetID)
        self.line

        selected_button = self.verticalLayoutButton.itemAt(i).widget()
        selected_button.setStyleSheet('background-color: rgb(240, 128, 128);')

    def load_assets(self):
        filename = 'assets.json'
        path = f'../dataset/{filename}'
        jff = JsonFileFactory()
        self.assets = jff.read_data(path, Asset)
