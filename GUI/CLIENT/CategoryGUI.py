from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import categoryPer
from Client import Client


class CategoryGUI(QWidget):

    def __init__(self):
        self.lstCategory = ""
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
        self.lstCategory = cont.sendSignal("GET_CATEGORY_LIST")
        print(self.lstCategory)
        self.addDataToWidget(self.lstCategory)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setFixedHeight(80*(self.count+1))
        # Thiết lập QFrame làm content pane của QMainWindow

        # Đặt kích thước cho QWidget
        self.content_frame.setFixedSize(741, 440)
        

        self.setWindowTitle("Example")

    def addDataToWidget(self,lstCategory):
        row=0
        for category in lstCategory:
            self.ct=categoryPer.Ui_Form(str(category["id"]),str(category["name"]),self.layout)
            self.layout.addWidget(self.ct,row,0)
            self.count+=1
            row+=1
    
    def returnPlaylist(self):
        return self.lstCategory
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pl=CategoryGUI()
    pl.show()
    sys.exit(app.exec())