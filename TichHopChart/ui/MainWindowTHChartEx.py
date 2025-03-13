import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar

from chap6.TichHopChart.ui.MainWindow import Ui_MainWindow


class MainWindowTHChartEx(Ui_MainWindow):
    def __init__(self):
        pass

    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.setupPlot()
        self.pushButtonBarChart.clicked.connect(self.showBarChart)
        self.pushButtonLineChart.clicked.connect(self.showLineChart)
        #self.pushButtonPieChart.clicked.connect(self.showPieChart)
        #self.pushButtonExit.clicked.connect(self.processExit)

    def show(self):
        self.MainWindow.show()

    def showBarChart(self):
        df = pd.read_csv('../dataset/NetProfit.csv')
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.ticklabel_format(useOffset=False, style='plain')
        ax.grid()
        ax.bar(df['Year'], df['VNM'])
        ax.set_title('Bar Chart Title')
        #ax.set_xlabel(columnX)
        #ax.set_ylabel(columnY)
        self.canvas.draw()
    def showLineChart(self):
        df = pd.read_csv('../dataset/NetProfit.csv')
        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.ticklabel_format(useOffset=False, style='plain')
        ax.grid()
        sns.lineplot(data = df, x='Year', y='VNM', marker = 'o', color = 'orange')
        ax.set_xlabel('Year')
        ax.set_ylabel('VNM')
        ax.set_title('SNS Line Plot Title')
        ax.legend(loc = 'lower right')
        self.canvas.draw()
    def setupPlot(self):
        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.toolbar = NavigationToolbar(self.canvas, self.MainWindow)
        self.verticalLayoutPlot.addWidget(self.canvas)
        self.verticalLayoutPlot.addWidget(self.toolbar)