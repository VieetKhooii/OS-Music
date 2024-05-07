from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import musicPer
from Client import Client


class MusicGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        

    def initUI(self):
        # Thiết lập kích thước và màu nền cho QWidget
        self.content_frame = QtWidgets.QWidget(parent=self)
        self.content_frame.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(parent=self.content_frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 730, 450))
        self.scrollArea.setWidgetResizable(True)
        self.count=0
        

        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 741, 440))


        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.scrollAreaWidgetContents.setLayout(self.layout)
        
        # Thêm các thành phần vào QFrame
        cont = Client()
        cont.connect()
        lstMusic = cont.sendSignal("GET_MUSIC_LIST")
        print(lstMusic)
        self.addDataToWidget(lstMusic)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setFixedHeight(80*(self.count+1))
        # Thiết lập QFrame làm content pane của QMainWindow

        # Đặt kích thước cho QWidget
        self.content_frame.setFixedSize(741, 440)
        

        self.setWindowTitle("Example")

    def addDataToWidget(self,lstMusic):
        row=0
        for music in lstMusic:
            self.baihat=musicPer.Ui_Form(str(music["id"]),str(music["name"]),str(music["artist"]),str(music["img"]),str(music["link"]))
            self.layout.addWidget(self.baihat,row,0)
            self.count+=1
            row+=1
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pl=MusicGUI()
    pl.show()
    sys.exit(app.exec())