import sys
from PyQt6 import QtWidgets
from MainWindow124Ex import MainWindow124Ex

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow124Ex()
    window.show()
    sys.exit(app.exec())

