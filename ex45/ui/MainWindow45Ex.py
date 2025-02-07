import functools

from PyQt6.QtWidgets import QPushButton, QMessageBox

from chap2.ex45.ui.MainWindow import Ui_MainWindow


class MainWindow45Ex(Ui_MainWindow):
    def __init__(self):  #constructor
        self.dataset = []  #luu tap du lieu co kieu list, moi tap la 1 dict
        self.selected_index = -1
        self.previous_button = None
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupSignalAndSlot()
    def showWindow(self):
        self.MainWindow.show()
    def setupSignalAndSlot(self):
        self.pushButtonSave.clicked.connect(self.process_save_book)
        self.pushButtonRemove.clicked.connect(self.process_remove_book)
        self.pushButtonSearchTitle.clicked.connect(self.search_by_title)
        self.pushButtonSearchISBN.clicked.connect(self.search_by_isbn)
        self.pushButtonFilterYears.clicked.connect(self.filter_by_year)
        self.pushButtonFilterPublisher.clicked.connect(self.filter_by_publisher)
    def check_duplicated_isbn(self, isbn):
        for book in self.dataset:
            if book['isbn'] == isbn:
                return True
        return False
    def process_save_book(self):
        isbn = self.lineEditISBN.text()
        title = self.lineEditTitle.text()
        author = self.lineEditAuthor.text()
        publisher = self.lineEditPublisher.text()
        year = self.lineEditYear.text()

        if not isbn or not title or not author or not publisher or not year:
            QMessageBox.warning(self.MainWindow, "Input Error", "All fields are required!")
            return

        book = {'isbn':isbn,
                'title':title, 'author':author,
                'publisher':publisher, 'year':year}
        if self.check_duplicated_isbn(isbn) == False:
            self.dataset.append(book)
        else:
            self.dataset[self.selected_index] = book  #chinh sua book dang chon
        self.show_book_on_gui()
    def process_remove_book(self):
        if self.selected_index == -1:
            QMessageBox.warning(self.MainWindow, "Selection Error", "No book selected to remove!")
            return

        del self.dataset[self.selected_index]
        self.selected_index = -1
        self.clear_book_details()
        self.show_book_on_gui()
    def search_by_title(self):
        title = self.lineEditTitle.text().strip().lower()
        self.filter_books(lambda book: title in book['title'].lower())
    def search_by_isbn(self):
        isbn = self.lineEditISBN.text().strip()
        self.filter_books(lambda book: book['isbn'] == isbn)
    def filter_by_year(self):
        year = self.lineEditYear.text().strip()
        self.filter_books(lambda book: book['year'] == year)
    def filter_by_publisher(self):
        publisher = self.lineEditPublisher.text().strip().lower()
        self.filter_books(lambda book: publisher in book['publisher'].lower())
    def filter_books(self, condition):
        self.clearLayout(self.verticalLayoutBook)
        for i, book in enumerate(self.dataset):
            if condition(book):
                btn = QPushButton(text=f'{book["title"]}')
                btn.setStyleSheet('background-color: rgb(155, 156, 152);')
                self.verticalLayoutBook.addWidget(btn)
                btn.clicked.connect(functools.partial(self.show_detail, i))
    def show_book_on_gui(self):
        self.clearLayout(self.verticalLayoutBook)
        for i in range(len(self.dataset)):  # qtrong trong bo nho: self.list
            book = self.dataset[i]
            title = f'{book['title']}'
            btn = QPushButton(text=title)
            btn.setStyleSheet('background-color: rgb(155, 156, 152);')
            self.verticalLayoutBook.addWidget(btn)
            btn.clicked.connect(functools.partial(self.show_detail, i))
    def show_detail(self, i):
        book = self.dataset[i]
        self.lineEditISBN.setText(book['isbn'])
        self.lineEditTitle.setText(book['title'])
        self.lineEditAuthor.setText(book['author'])
        self.lineEditYear.setText(book['year'])
        self.lineEditPublisher.setText(book['publisher'])
        self.selected_index = i  #luu vi tri o nho, de cac bien trong def kh bi thu hoi; = -1 la remove
        btn = self.MainWindow.sender()
        if self.previous_button != None:
            self.previous_button.setStyleSheet('background-color: rgb(155, 156, 152);')
        btn.setStyleSheet('background-color: rgb(235, 225, 52);')
        self.previous_button = btn

    def clearLayout(self, layout):
        if layout is not None:
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget is not None:
                    widget.deleteLater()
                else:
                    self.clearLayout(item.layout())

    def clear_book_details(self):
        self.lineEditISBN.clear()
        self.lineEditTitle.clear()
        self.lineEditAuthor.clear()
        self.lineEditYear.clear()
        self.lineEditPublisher.clear()
        self.selected_index = -1