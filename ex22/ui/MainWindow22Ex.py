from chap1_function.ex22.lib.func_lib22 import P
from chap1_function.ex22.ui.MainWindow import Ui_MainWindow


class MainWindow22Ex(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonExecute.clicked.connect(self.process_result)
    def process_result(self):
        n=int(self.lineEditN.text())
        m=int(self.lineEditM.text())
        d=int(self.lineEditD.text())
        p=float(P(n,m,d))
        p=round(p,3)
        self.lineEditProbability.setText(f'{p}')