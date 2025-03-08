from PyQt6.QtCore import Qt

from chap6.learnPyQtGraphPart2.ui.MainWindow import Ui_MainWindow
import pyqtgraph as pg

class MainWindowGraph2Ex(Ui_MainWindow):
    def __init__(self):
        super().__init__()
    def setupUi(self, MainWindow):
        super().setupUi(MainWindow)
        self.MainWindow = MainWindow
        self.graphWidget = pg.PlotWidget()
        #self.graphWidget.setTitle('Temperature per hour', color = 'b', size = '20pt', bold = True, italic = True)
        self.graphWidget.setTitle('<span style=\'color:blue;font-size:20pt\'>Temperature per hour</span>')
        styles = {'color': '#f00', 'font-size': '20px'}
        self.graphWidget.setLabel('left', 'Temperature (°C)', **styles)
        self.graphWidget.setLabel('bottom', 'Hour (H)', **styles)
        styles_top_right = {'color': 'green', 'font-size': '15px'}
        self.graphWidget.setLabel('top', 'Learn PyQtGraph', **styles_top_right)
        self.graphWidget.setLabel('right', 'banhbeo.com', **styles_top_right)
        self.graphWidget.setBackground('#f5dadf')
        self.graphWidget.showGrid(x = True, y = True)
        #create plot data
        hour = [1,2,3,4,5,6,7,8,9,10,11,12]
        temperature = [20, 21, 20, 32, 33, 31, 29, 31, 32, 35, 37, 45]
        temperature2 = [25, 18, 30, 10, 47, 29, 26, 32, 35, 45, 40, 42]
        # Step 4: call plot method
        pen = pg.mkPen(color=(255, 0, 0), width=15, style=Qt.PenStyle.DotLine)
        pen2 = pg.mkPen(color=(0, 0, 255), width=8, style=Qt.PenStyle.SolidLine)
        symbolPen = pg.mkPen(color=(196, 196, 196), width=2)
        symbolPen2 = pg.mkPen(color=(255, 255, 0), width=2)
        self.graphWidget.addLegend()
        # self.graphWidget.setXRange(1, 8, padding=0)
        # self.graphWidget.setYRange(10, 80, padding=0)
        self.graphWidget.plot(hour, temperature, name="Sensor X",
                              pen=pen,
                              symbol='+',
                              symbolSize=15,
                              symbolBrush=('b'),
                              symbolPen=symbolPen)
        plot2 = self.graphWidget.plot(hour, temperature2, name="Sensor Y",
                              pen=pen2,
                              symbol='d',
                              symbolSize=8,
                              symbolBrush=('r'),
                              symbolPen=symbolPen2)
        temperature2[3] = 100
        plot2.setData(hour, temperature2)
        #add graphWidget into Layout
        self.myLayout.addWidget(self.graphWidget)
    def show(self):
        self.MainWindow.show()