from chap2.ex26.lib.lib26 import count_uppercase, count_vowels, count_lowercase, count_numbers, count_spaces, \
    count_consonants, count_special_char
from chap2.ex26.ui.MainWindow import Ui_MainWindow


class MainWindow26Ex(Ui_MainWindow):
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow=MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonUppercase.clicked.connect(self.process_upper)
        self.pushButtonVowels.clicked.connect(self.process_vowels)
        self.pushButtonLowercase.clicked.connect(self.process_lower)
        self.pushButtonNumbers.clicked.connect(self.process_numbers)
        self.pushButtonSpaces.clicked.connect(self.process_spaces)
        self.pushButtonConsonants.clicked.connect(self.process_consonants)
        self.pushButtonSpecialCharacters.clicked.connect(self.process_special_char)
    def process_upper(self):
        s = self.lineEditInput.text()
        count_uppercase(s)
        self.lineEditOutput.setText(f'{count_uppercase(s)}')
    def process_vowels(self):
        s = self.lineEditInput.text()
        count_vowels(s)
        self.lineEditOutput.setText(f'{count_vowels(s)}')
    def process_lower(self):
        s = self.lineEditInput.text()
        count_lowercase(s)
        self.lineEditOutput.setText(f'{count_lowercase(s)}')
    def process_numbers(self):
        s = self.lineEditInput.text()
        count_numbers(s)
        self.lineEditOutput.setText(f'{count_numbers(s)}')
    def process_spaces(self):
        s = self.lineEditInput.text()
        count_spaces(s)
        self.lineEditOutput.setText(f'{count_spaces(s)}')
    def process_consonants(self):
        s = self.lineEditInput.text()
        count_consonants(s)
        self.lineEditOutput.setText(f'{count_consonants(s)}')
    def process_special_char(self):
        s = self.lineEditInput.text()
        count_special_char(s)
        self.lineEditOutput.setText(f'{count_special_char(s)}')