from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Main vertical layout
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Title label
        self.lblTitle = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.lblTitle.setFont(font)
        self.lblTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.lblTitle.setText("Employee Management System")
        self.verticalLayout.addWidget(self.lblTitle)

        # Horizontal layout for buttons
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        # Buttons for each operation
        self.btnLoadData = QtWidgets.QPushButton(self.centralwidget)
        self.btnLoadData.setText("Load Data")
        self.horizontalLayout.addWidget(self.btnLoadData)

        self.btnShowAll = QtWidgets.QPushButton(self.centralwidget)
        self.btnShowAll.setText("Show All")
        self.horizontalLayout.addWidget(self.btnShowAll)

        # Add label and line edit for year filtering
        self.lblFilterYear = QtWidgets.QLabel(self.centralwidget)
        self.lblFilterYear.setText("Birth Year:")
        self.horizontalLayout.addWidget(self.lblFilterYear)

        self.lineEditInputFilterYear = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditInputFilterYear.setPlaceholderText("YYYY")
        self.lineEditInputFilterYear.setMaximumWidth(100)
        self.horizontalLayout.addWidget(self.lineEditInputFilterYear)

        self.btnFilterByYear = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterByYear.setText("Filter by Year")
        self.horizontalLayout.addWidget(self.btnFilterByYear)

        self.btnTop3Oldest = QtWidgets.QPushButton(self.centralwidget)
        self.btnTop3Oldest.setText("Top 3 Oldest")
        self.horizontalLayout.addWidget(self.btnTop3Oldest)

        self.btnFilterTesters = QtWidgets.QPushButton(self.centralwidget)
        self.btnFilterTesters.setText("Testers Only")
        self.horizontalLayout.addWidget(self.btnFilterTesters)

        self.btnCountByRole = QtWidgets.QPushButton(self.centralwidget)
        self.btnCountByRole.setText("Count by Role")
        self.horizontalLayout.addWidget(self.btnCountByRole)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Table widget for displaying employee data
        self.tableEmployees = QtWidgets.QTableWidget(self.centralwidget)
        self.tableEmployees.setObjectName("tableEmployees")
        self.tableEmployees.setColumnCount(5)
        self.tableEmployees.setHorizontalHeaderLabels(["ID", "Name", "DoB", "Role", "Gender"])
        self.tableEmployees.horizontalHeader().setStretchLastSection(True)
        self.tableEmployees.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.ResizeMode.Stretch)
        self.verticalLayout.addWidget(self.tableEmployees)

        # Text browser for displaying results
        self.txtResults = QtWidgets.QTextBrowser(self.centralwidget)
        self.txtResults.setObjectName("txtResults")
        self.txtResults.setMaximumHeight(150)
        self.verticalLayout.addWidget(self.txtResults)

        # Set central widget
        MainWindow.setCentralWidget(self.centralwidget)

        # Menu bar
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        # Status bar
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Connect signals and slots
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Employee Management"))
