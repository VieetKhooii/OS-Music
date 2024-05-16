from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
import playlistPer
from Client import Client


class PlaylistGUI(QWidget):

    def __init__(self):
        self.lstPlaylist = ""
        super().__init__()
        self.initUI()
        

    def initUI(self):
        # Thiết lập kích thước và màu nền cho QWidget
        self.content_frame = QtWidgets.QWidget(parent=self)
        self.content_frame.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(parent=self.content_frame)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 730, 460))
        self.scrollArea.setWidgetResizable(True)
        self.count=0
        

        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 741, 460))


        self.layout = QGridLayout()
        self.layout.setHorizontalSpacing(0)
        self.layout.setVerticalSpacing(0)
        self.scrollAreaWidgetContents.setLayout(self.layout)
        
        # Thêm các thành phần vào QFrame
        cont = Client()
        cont.connect()
        self.lstPlaylist = cont.sendSignal("GET_PLAYLIST_LIST")
        print(self.lstPlaylist)
        self.addDataToWidget(self.lstPlaylist)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.scrollAreaWidgetContents.setFixedHeight(80*(self.count+1))
        # Thiết lập QFrame làm content pane của QMainWindow

        # Đặt kích thước cho QWidget
        self.content_frame.setFixedSize(741, 460)
        
        self.btnAddPlaylist = QtWidgets.QPushButton(parent=self)
        self.btnAddPlaylist.setGeometry(QtCore.QRect(20, 0, 75, 23))
        self.btnAddPlaylist.setObjectName("btnAddPlaylist")
        self.btnAddPlaylist.setText("Add Playlist")
        self.btnAddPlaylist.setStyleSheet("background-color: #70bf73; color: white;")
        self.btnAddPlaylist.clicked.connect(self.addPlayList)

        self.setWindowTitle("Example")

    def addDataToWidget(self,lstPlaylist):
        row=0
        for playlist in lstPlaylist:
            self.pl=playlistPer.Ui_Form(str(playlist["id"]),str(playlist["name"]),self.layout)
            self.layout.addWidget(self.pl,row,0)
            self.count+=1
            row+=1
    def addPlayList(self):
        dialog = QDialog()
        dialog.setWindowTitle("Thêm PlayList")
        dialog.setFixedSize(300, 150)  
        layout = QVBoxLayout(dialog)
        label2 = QLabel("Tên PlayList: ")
        layout.addWidget(label2)
        lineEdit2 = QLineEdit()
        layout.addWidget(lineEdit2)
        # Thêm nút
        button = QPushButton("Thêm")
        button.clicked.connect(lambda: self.addPlaylistConfirmed(lineEdit2.text(),dialog))
        layout.addWidget(button)

        dialog.exec()
     

    def addPlaylistConfirmed(self, tenPlaylist,dialog):
        client = Client()
        client.connect()
        lst = client.sendSignal("ADD_PLAYLIST_" +tenPlaylist)
        dialog.close()
        
    
    def returnPlaylist(self):
        return self.lstPlaylist
if __name__ == "__main__":
    app = QApplication(sys.argv)
    pl=PlaylistGUI()
    pl.show()
    sys.exit(app.exec())