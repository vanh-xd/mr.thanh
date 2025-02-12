import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from chap3.ex63.models.nonOfficialProduct import nonOfficialProduct
from chap3.ex63.models.officialProduct import officialProduct
from chap3.ex63.models.productManagement import productManagement
from chap3.ex63.ui.MainWindow import Ui_MainWindow


class MainWindow63Ex(Ui_MainWindow):
    def __init__(self):
        self.pm = productManagement()
        self.selected_index = -1
        self.last_selected_button = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save)
        self.pushButtonRemove.clicked.connect(self.process_remove)
        self.pushButtonSearchName.clicked.connect(self.search_name)
        self.pushButtonFilterPrice.clicked.connect(self.filter_price)
    def process_save(self):
        if self.radioButtonOfficial.isChecked():
            p = officialProduct()
        else:
            p = nonOfficialProduct()
            p.discount = self.lineEditDiscount.setText('10%')
        p.id = self.lineEditID.text()
        p.name = self.lineEditName.text()
        try:
            p.price = float(self.lineEditPrice.text())
        except:
            QMessageBox.warning(self.MainWindow, 'ERROR', 'Price entered should be number.')
            self.lineEditPrice.clear()
            self.lineEditPrice.setFocus()
        self.pm.add_product(p)
        self.display_layout()
    def process_remove(self):
        if self.selected_index == -1:  #no selection
            return
        self.pm.database.pop(self.selected_index)
        self.display_layout()
    def search_name(self):
        search = self.lineEditEnterName.text().strip()
        for product in self.pm.database:
            if product.name == search:
                QMessageBox.information(self.MainWindow, 'SEARCH RESULT', f'Found PRODUCT {product.name} - {search}')
                return
        QMessageBox.warning(self.MainWindow, 'SEARCH RESULT', 'NAME Not Found')
    def filter_price(self):
        try:
            filter = float(self.lineEditEnterPrice.text().strip())
        except:
            QMessageBox.warning(self.MainWindow, 'INPUT ERROR', 'Price entered should be number.')
            return
        for product in self.pm.database:
            if product.price == filter:
                QMessageBox.information(self.MainWindow, 'SEARCH RESULT', f'Found PRODUCT {product.name} - {filter}')
                return
        QMessageBox.warning(self.MainWindow, 'SEARCH RESULT', 'PRICE Not Found')
    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())
    def display_layout(self):
        self.clearLayout(self.verticalLayoutButton)
        for i in range(len(self.pm.database)):
            x = self.pm.database[i]
            title = f'{x.id}-{x.name}-{x.price}'
            btn = QPushButton(text = title)
            if isinstance(x, officialProduct):
                btn.setStyleSheet('background-color: rgb(0, 153, 0);')
            else:
                pass
            self.verticalLayoutButton.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail, i))
    def show_detail(self, i):
        if self.last_selected_button is not None:
            if isinstance(self.pm.database[self.selected_index], officialProduct):
                self.last_selected_button.setStyleSheet('background-color: rgb(0, 153, 0);')
            else:
                self.last_selected_button.setStyleSheet('')
        self.selected_index = i
        p = self.pm.database[i]
        selected_button = self.verticalLayoutButton.itemAt(i).widget()
        selected_button.setStyleSheet('background-color: rgb(255, 102, 255);')
        self.last_selected_button = selected_button