import numpy as np
from PyQt6.QtWidgets import QTableWidgetItem, QTableWidget

from chap6.ex117.ui.MainWindow import Ui_MainWindow


class MainWindow117Ex(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()

    def setupSignalAndSlot(self):
        self.pushButtonCalculate.clicked.connect(self.process_statistic)

    def showWindow(self):
        self.MainWindow.show()

    def process_statistic(self):
        s = self.lineEditInput.text()
        arr_int = [int(i) for i in s.split(',')]
        arr_np = np.asarray(arr_int)
        min_label = f'MIN = {np.min(arr_np)}'
        argmin_label = f'ARGMIN = {np.argmin(arr_np)}'
        max_label = f'MAX = {np.max(arr_np)}'
        argmax_label = f'ARGMAX = {np.argmax(arr_np)}'
        mean_label = f'MEAN = {np.mean(arr_np)}'
        median_label = f'MEDIAN = {np.median(arr_np)}'
        std_label = f'STD = {np.std(arr_np)}'
        result = min_label + "\n" + argmin_label + "\n" + \
                 max_label + "\n" + argmax_label + "\n" + \
                 mean_label + "\n" + median_label + "\n" + std_label
        self.labelOutput.setText(result)
        self.tableWidget.setRowCount(0)
        self.insert_row_statistic('MIN', np.min(arr_np))
        self.insert_row_statistic('ARGMIN', np.argmin(arr_np))
        self.insert_row_statistic('MAX', np.max(arr_np))
        self.insert_row_statistic('ARGMAX', np.argmax(arr_np))
        self.insert_row_statistic('MEAN', np.mean(arr_np))
        self.insert_row_statistic('MEDIAN', np.median(arr_np))
        self.insert_row_statistic('STD', np.std(arr_np))

    def insert_row_statistic(self, term_title, value):
        row = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row)
        self.tableWidget.setItem(row, 0, QTableWidgetItem(term_title))
        self.tableWidget.setItem(row, 1, QTableWidgetItem(str(value)))
