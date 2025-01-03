from chap1_function.ex21.lib.func_lib import A, C
from chap1_function.ex21.ui.MainWindow import Ui_MainWindow

class MainWindowEx21(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(    MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()

    def setupSignalAndSlot(self):
        self.pushButtonExecute.clicked.connect(self.process_result)
    def process_result(self):
        n=int(self.lineEditN.text())
        k=int(self.lineEditK.text())
        a=A(n,k)
        c=C(n,k)
        self.lineEditA.setText(f'{a}')
        self.lineEditC.setText(f'{c}')