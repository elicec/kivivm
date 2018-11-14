from PyQt5.QtWidgets import(QWidget,QProgressBar,
                            QPushButton,QApplication)
from PyQt5.QtWidgets import(QMainWindow,QAction,
                            qApp,QApplication)
from PyQt5.QtCore import QBasicTimer
from PyQt5.QtGui import QIcon
import sys
import datetime
class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(0,40,100,25)
        self.btn = QPushButton('start',self)
        self.btn.move(0,80)
        self.btn.clicked.connect(self.doAction)
        self.timer = QBasicTimer()
        self.step = 0
        self.setGeometry(300,300,280,170)
        self.setWindowTitle('QProgressBar')

        refreshAct = QAction(QIcon('imgs/refresh.png'),'刷新',self)
        refreshAct.setShortcut('F5')
        refreshAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('退出')
        self.toolbar.addAction(refreshAct)

        time_stamp = datetime.datetime.now()
        self.statusBar().showMessage(time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))
        self.show()

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(200,self)
            self.btn.setText('Stop')

    def timerEvent(self,e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ControlPanel()
    sys.exit(app.exec())
