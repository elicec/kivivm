from PyQt5.QtWidgets import(QProgressBar,
                            QPushButton,QApplication)
from PyQt5.QtWidgets import(QMainWindow,QAction,
                            qApp,QApplication)
from PyQt5.QtWidgets import QMenu,QLabel
from PyQt5.QtCore import QBasicTimer,Qt,QThread,pyqtSignal
from PyQt5.QtGui import QIcon,QPalette,QColor
import sys
import datetime
from VPS import VPS
class ControlPanel(QMainWindow):
    def __init__(self):
        super().__init__()
        self.updateThread = updateThread()
        self.updateThread.signal.connect(self.updateUsage)
        self.initUI()
        self.updateThread.start()

    def initUI(self):
        self.lbOSKey = QLabel(self)
        self.lbOSKey.move(20,70+10)
        self.lbOSKey.setText("操作系统:")
        self.lbOSValue = QLabel(self)
        self.lbOSValue.setMinimumWidth(200)
        self.lbOSValue.move(120,70+10)
        self.lbOSValue.setText("unknow")

        self.lbLocationKey = QLabel(self)
        self.lbLocationKey.move(20,70+30+10)
        self.lbLocationKey.setText("机房位置:")
        self.lbLocationValue = QLabel(self)
        self.lbLocationValue.setWordWrap(True)
        self.lbLocationValue.setMinimumWidth(300)
        self.lbLocationValue.move(120,70+30+10)
        self.lbLocationValue.setText("unknow")

        self.lbIPKey = QLabel(self)
        self.lbIPKey.move(20,100+30+10)
        self.lbIPKey.setText("IP地址:")
        self.lbIPValue = QLabel(self)
        self.lbIPValue.move(120,100+30+10)
        self.lbIPValue.setText("unknow")

        self.lbSSHPortKey = QLabel(self)
        self.lbSSHPortKey.move(20,130+30+10)
        self.lbSSHPortKey.setText("SSH端口:")
        self.lbSSHPortValue = QLabel(self)
        self.lbSSHPortValue.move(120,130+30+10)
        self.lbSSHPortValue.setText("unknow")

        self.lbStatusKey = QLabel(self)
        self.lbStatusKey.move(20,160+30+10)
        self.lbStatusKey.setText("运行状态:")
        self.lbStatusValue = QLabel(self)
        self.lbStatusValue.setMinimumWidth(240)
        self.lbStatusValue.move(120,160+30+10)
        self.lbStatusValue.setText("unknow")

        self.lbRamKey = QLabel(self)
        self.lbRamKey.move(20,200+30+10)
        self.lbRamKey.setText("内存:")
        self.pbarRam = QProgressBar(self)
        self.pbarRam.setGeometry(120,205+30+10,200,15)
        self.pbarRam.setValue(40)
        self.pbarRam.setTextVisible(False)
        self.lbRamValue = QLabel(self)
        self.lbRamValue.move(120,215+30+10)

        self.lbSwpKey = QLabel(self)
        self.lbSwpKey.move(20,245+30+10)
        self.lbSwpKey.setText("SWAP:")
        self.pbarSwp = QProgressBar(self)
        self.pbarSwp.setGeometry(120,250+30+10,200,15)
        self.pbarSwp.setValue(32)
        self.pbarSwp.setTextVisible(False)
        self.lbSwpValue = QLabel(self)
        self.lbSwpValue.move(120,260+30+10)

        self.lbDiskKey = QLabel(self)
        self.lbDiskKey.move(20,290+30+10)
        self.lbDiskKey.setText("磁盘:")
        self.pbarDisk = QProgressBar(self)
        self.pbarDisk.setGeometry(120,295+30+10,200,15)
        self.pbarDisk.setValue(69)
        self.pbarDisk.setTextVisible(False)
        self.lbDiskValue = QLabel(self)
        self.lbDiskValue.move(120,305+30+10)

        self.lbBandKey = QLabel(self)
        self.lbBandKey.move(20,290+45+30+10)
        self.lbBandKey.setText("流量:")
        self.pbarBand = QProgressBar(self)
        self.pbarBand.setGeometry(120,295+45+30+10,200,15)
        self.pbarBand.setValue(69)
        self.pbarBand.setTextVisible(False)
        self.lbBandValue = QLabel(self)
        self.lbBandValue.move(120,305+45+30+10)

        # self.btnStop = QPushButton('start',self)
        # self.btnStop.move(0,400+30+10)
        # self.btnStop.clicked.connect(self.doAction)

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
        if action == refreshAct:
            self.updateThread.start()

    def setPbarColor(self,p,color):
        palette = QPalette(p.palette())
        palette.setColor(QPalette.Highlight,QColor(color))
        p.setPalette(palette)

    def updateUsage(self,vps):
        self.lbIPValue.setText(vps.getIp())
        self.lbSSHPortValue.setText(vps.getSSHPort())
        self.lbOSValue.setText(vps.getOs())
        self.lbLocationValue.setText(vps.getLocation())
        self.lbStatusValue.setText(vps.getLA())

        t0 = (vps.getRamTotal()-vps.getRamFree())/1024/1024
        t1 = vps.getRamTotal()/1024/1024
        s = str(round(t0,2))+"/"+str(t1)+" MB"
        self.lbRamValue.setText(s)
        self.pbarRam.setValue(t0*100/t1)
        if t0*100/t1 > 80:
            self.setPbarColor(self.pbarRam,Qt.red)

        t0 = (vps.getUsagDisk())/1024/1024/1024
        t1 = vps.getPlanDisk()/1024/1024/1024
        s = str(round(t0,2))+"/"+str(t1)+" GB"
        self.lbDiskValue.setText(s)
        self.pbarDisk.setValue(t0*100/t1)
        if t0*100/t1 > 80:
            self.setPbarColor(self.pbarDisk,Qt.red)

        t0 = (vps.getUsagData())/1024/1024/1024
        t1 = vps.getPlanData()/1024/1024/1024
        s = str(round(t0,2))+"/"+str(t1)+" GB"
        self.lbBandValue.setText(s)
        self.pbarBand.setValue(t0*100/t1)
        if t0*100/t1 > 80:
            self.setPbarColor(self.pbarBand,Qt.red)

        t0 = (vps.getPlanSwap()-vps.getFreeSwap())/1024/1024
        t1 = vps.getPlanSwap()/1024/1024
        s = str(round(t0,2))+"/"+str(round(t1,0))+" MB"
        self.lbSwpValue.setText(s)
        self.pbarSwp.setValue(t0*100/t1)
        if t0*100/t1 > 80:
            self.setPbarColor(self.pbarSwp,Qt.red)

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

class updateThread(QThread):
    signal = pyqtSignal('PyQt_PyObject')
    def __init__(self):
        QThread.__init__(self)

    def __del__(self):
        self.wait()

    def run(self):
        vps = VPS()
        self.signal.emit(vps)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ControlPanel()
    sys.exit(app.exec())
