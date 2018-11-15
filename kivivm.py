from PyQt5.QtWidgets import(QProgressBar,
                            QPushButton,QApplication)
from PyQt5.QtWidgets import(QMainWindow,QAction,
                            qApp,QApplication)
from PyQt5.QtWidgets import QMenu,QLabel
from PyQt5.QtCore import QBasicTimer,Qt
from PyQt5.QtGui import QIcon
import sys
import datetime
class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbOSKey = QLabel(self)
        self.lbOSKey.move(20,70)
        self.lbOSKey.setText("操作系统:")
        self.lbOSValue = QLabel(self)
        self.lbOSValue.move(120,70)
        self.lbOSValue.setText("unknow")

        self.lbLocationKey = QLabel(self)
        self.lbLocationKey.move(20,70+30)
        self.lbLocationKey.setText("机房位置:")
        self.lbLocationValue = QLabel(self)
        self.lbLocationValue.move(120,70+30)
        self.lbLocationValue.setText("unknow")

        self.lbIPKey = QLabel(self)
        self.lbIPKey.move(20,100+30)
        self.lbIPKey.setText("IP地址:")
        self.lbLocationValue = QLabel(self)
        self.lbLocationValue.move(120,100+30)
        self.lbLocationValue.setText("unknow")

        self.lbSSHPortKey = QLabel(self)
        self.lbSSHPortKey.move(20,130+30)
        self.lbSSHPortKey.setText("SSH端口:")
        self.lbSSHPortValue = QLabel(self)
        self.lbSSHPortValue.move(120,130+30)
        self.lbSSHPortValue.setText("unknow")

        self.lbStatusKey = QLabel(self)
        self.lbStatusKey.move(20,160+30)
        self.lbStatusKey.setText("运行状态:")
        self.lbStatusValue = QLabel(self)
        self.lbStatusValue.move(120,160+30)
        self.lbStatusValue.setText("unknow")

        self.lbRamKey = QLabel(self)
        self.lbRamKey.move(20,200+30)
        self.lbRamKey.setText("内存:")
        self.pbarRam = QProgressBar(self)
        self.pbarRam.setGeometry(120,205+30,200,15)
        self.pbarRam.setValue(40)
        self.lbRamValue = QLabel(self)
        self.lbRamValue.move(120,215+30)
        self.lbRamValue.setText("40/100 MB")

        self.lbSwpKey = QLabel(self)
        self.lbSwpKey.move(20,245+30)
        self.lbSwpKey.setText("SWAP:")
        self.pbarSwp = QProgressBar(self)
        self.pbarSwp.setGeometry(120,250+30,200,15)
        self.pbarSwp.setValue(32)
        self.lbSwpValue = QLabel(self)
        self.lbSwpValue.move(120,260+30)
        self.lbSwpValue.setText("32/100 MB")

        self.lbDiskKey = QLabel(self)
        self.lbDiskKey.move(20,290+30)
        self.lbDiskKey.setText("磁盘:")
        self.pbarDisk = QProgressBar(self)
        self.pbarDisk.setGeometry(120,295+30,200,15)
        self.pbarDisk.setValue(69)
        self.lbDiskValue = QLabel(self)
        self.lbDiskValue.move(120,305+30)
        self.lbDiskValue.setText("69/100 MB")

        self.lbBandKey = QLabel(self)
        self.lbBandKey.move(20,290+45+30)
        self.lbBandKey.setText("流量:")
        self.pbarBand = QProgressBar(self)
        self.pbarBand.setGeometry(120,295+45+30,200,15)
        self.pbarBand.setValue(69)
        self.lbBandValue = QLabel(self)
        self.lbBandValue.move(120,305+45+30)
        self.lbBandValue.setText("69/100 MB")

        self.btnStart = QPushButton('start',self)
        self.btnStart.move(0,400+30)
        self.btnStart.clicked.connect(self.doAction)

        self.btnStop = QPushButton('start',self)
        self.btnStop.move(0,400+30)
        self.btnStop.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0
        self.setGeometry(300,300,580,570)
        self.setWindowTitle('QProgressBar')

        startAct = QAction(QIcon('imgs/start.png'),'start',self)
        startAct.setShortcut('F5')
        startAct.setIconText("start")
        startAct.triggered.connect(qApp.quit)
        stopAct = QAction(QIcon('imgs/stop.png'),'start',self)
        stopAct.setShortcut('F6')
        stopAct.setIconText("stop")
        stopAct.triggered.connect(qApp.quit)
        resetAct = QAction(QIcon('imgs/reset.png'),'start',self)
        resetAct.setShortcut('F7')
        resetAct.setIconText("reset")
        resetAct.triggered.connect(qApp.quit)
        self.toolbar = self.addToolBar('退出')
        self.toolbar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.toolbar.addAction(startAct)
        self.toolbar.addAction(stopAct)
        self.toolbar.addAction(resetAct)

        time_stamp = datetime.datetime.now()
        self.statusBar().showMessage(time_stamp.strftime('%Y.%m.%d-%H:%M:%S'))

        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&文件')
        impMenu = QMenu('保存',self)
        impAct = QAction('save',self)
        impMenu.addAction(impAct)
        newAct = QAction('new',self)
        fileMenu.addAction(newAct)
        fileMenu.addMenu(impMenu)
        self.show()

    def contextMenuEvent(self,event):
        cmenu = QMenu(self)
        refreshAct = cmenu.addAction("刷新")
        quitAct = cmenu.addAction("退出")
        action = cmenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAct:
            qApp.quit()


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
