from chap5_gui.blogEx22_learnQTableWidget.ui.MainWindow import Ui_MainWindow


class MainWindow22Ex(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.tableWidget.itemSelectionChanged.connect(self.processSelectedItem)
    def processSelectedItem(self):
        row = self.tableWidget.currentRow()
        songId = self.tableWidget.item(row, 0)
        songName = self.tableWidget.item(row, 1)
        singer = self.tableWidget.item(row, 2)
        self.lineEditSongID.setText(songId.text())
        self.lineEditSongName.setText(songName.text())
        self.lineEditSinger.setText(singer.text())
    def show(self):
        self.MainWindow.show()
