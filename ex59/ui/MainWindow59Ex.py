from chap3.ex59.lib.Fraction import Fraction
from chap3.ex59.ui.MainWindow import Ui_MainWindow


class MainWindow59Ex(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonCong.clicked.connect(self.xuly_cong)
        self.pushButtonTru.clicked.connect(self.xuly_tru)
        self.pushButtonNhan.clicked.connect(self.xuly_nhan)
        self.pushButtonChia.clicked.connect(self.xuly_chia)
    def get_fraction(self):
        tu1 = int(self.lineEditPS1Tu.text())
        mau1 = int(self.lineEditPS1Mau.text())
        tu2 = int(self.lineEditPS2Tu.text())
        mau2 = int(self.lineEditPS2Mau.text())
        ps1 = Fraction(tu1, mau1)
        ps2 = Fraction(tu2, mau2)
        return (ps1,ps2)
    def xuly_cong(self):
        ps1,ps2 = self.get_fraction()
        ps3 = ps1.add(ps2)  #tru thi ps1.subtract(ps2)
        self.lineEditPS3Tu.setText(f'{ps3.numerator}')
        self.lineEditPS3Mau.setText(f'{ps3.denominator}')
        self.labelDauChamHoi.setText('+')
    def xuly_tru(self):
        ps1, ps2 = self.get_fraction()
        ps3 = ps1.subtract(ps2)
        self.lineEditPS3Tu.setText(f'{ps3.numerator}')
        self.lineEditPS3Mau.setText(f'{ps3.denominator}')
        self.labelDauChamHoi.setText('-')
    def xuly_nhan(self):
        ps1, ps2 = self.get_fraction()
        ps3 = ps1.times(ps2)
        self.lineEditPS3Tu.setText(f'{ps3.numerator}')
        self.lineEditPS3Mau.setText(f'{ps3.denominator}')
        self.labelDauChamHoi.setText('*')
    def xuly_chia(self):
        ps1, ps2 = self.get_fraction()
        ps3 = ps1.divide(ps2)
        self.lineEditPS3Tu.setText(f'{ps3.numerator}')
        self.lineEditPS3Mau.setText(f'{ps3.denominator}')
        self.labelDauChamHoi.setText(':')