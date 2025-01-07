import traceback

from PyQt6.QtWidgets import QMessageBox

from chap1_function.ex23.ui.MainWindow import Ui_MainWindow
from chap1_function.ex23.lib.func_lib23 import calc

class MainWindow23Ex(Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.total_customer = 0
        self.total_student = 0
        self.total_revenue = 0
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
        self.lineEditCustomerName.setFocus()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonCalculate.clicked.connect(self.process_calc)
        self.pushButtonStatistic.clicked.connect(self.process_sta)
        self.pushButtonNewSelling.clicked.connect(self.process_new_selling)
    def process_calc(self):
        try:
            cus_name = str(self.lineEditCustomerName.text())
            if not cus_name.strip():
                self.show_error('Customer Name must be entered')
                self.lineEditCustomerName.setFocus()
                return

            q = int(self.lineEditQuantity.text())
            if q <= 0:
                self.show_error('Quantity must be a positive integer')
                return

            calculate = calc(q)
            if self.checkBox.isChecked():
                calculate *= 0.95
                self.total_student += 1
            self.total_revenue += calculate
            self.total_customer += 1

            self.lineEditPayment.setText(f'{calculate}')
        except:
            traceback.print_exc()
            self.show_error('Unexpected Error')
            self.lineEditCustomerName.setFocus()
    def process_sta(self):
        self.lineEditNumberOfCustomers.setText(f'{self.total_customer}')
        self.lineEditStudentCuston.setText(f'{self.total_student}')
        self.lineEditRevenue.setText(f'{self.total_revenue}')
    def process_new_selling(self):
        self.lineEditCustomerName.clear()
        self.lineEditQuantity.clear()
        self.lineEditPayment.clear()
        self.checkBox.setChecked(False)
        self.lineEditCustomerName.setFocus()
    def show_error(self, message):
        msg_box = QMessageBox()
        msg_box.setIcon(QMessageBox.Icon.Warning)
        msg_box.setWindowTitle('ERROR')
        msg_box.setText(message)
        msg_box.setStandardButtons(QMessageBox.StandardButton.Ok)
        msg_box.exec()
