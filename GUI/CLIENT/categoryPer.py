# Form implementation generated from reading ui file 'playlist-baihat.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt
from Client import Client
import pygame
import musicPer

class Ui_Form(QWidget):
    def __init__(self,id,name,qd:QGridLayout):
        super().__init__()
        self.id=id
        self.name=name
        self.qd=qd
        self.setupUi()

    def setupUi(self):
        self.resize(585, 94)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(10, 10, 571, 80))
        self.frame.setStyleSheet("background-color: rgb(114,176,186);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")

        self.image = QtWidgets.QLabel(parent=self.frame)
        self.image.setGeometry(QtCore.QRect(20, 10, 61, 61))
        self.image.setText("")
        self.image.setObjectName("label")
        # self.setImageToQLabelFromPlaylist()

        self.TenCate = QtWidgets.QLabel(parent=self.frame)
        self.TenCate.setGeometry(QtCore.QRect(130, 20, 441, 20))
        self.TenCate.setStyleSheet("color: rgb(255, 255, 255);")
        self.TenCate.setObjectName("lblTenBaiHat")

        self.lblma = QtWidgets.QLabel(parent=self.frame)
        self.lblma.setStyleSheet("color: rgb(255, 255, 255);")
        self.lblma.setObjectName("lblmaPlaylist")


        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(""), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)

        self.btnCate = QtWidgets.QPushButton(parent=self.frame)
        self.btnCate.setGeometry(QtCore.QRect(390, 10, 51, 61))
        self.btnCate.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(""), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.btnCate.setIcon(icon1)
        self.btnCate.setIconSize(QtCore.QSize(50, 50))
        self.btnCate.setObjectName("btnCate")
        self.btnCate.clicked.connect(lambda:self.showMusiclst(self.qd))



        self.retranslateUi()

    def retranslateUi(self):
        self.TenCate.setText(self.name)
    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def showMusiclst(self,f:QGridLayout):
        self.clearLayout(f)
        # Lấy dữ liệu và thêm các widget mới vào bố trí
        client = Client()
        client.connect()
        lstCategoryDetail = client.sendSignal("GET_SONGS_OF_CATEGORY_" + self.id)
        lstMusic = client.sendSignal("GET_MUSIC_LIST")
        row = 0
   
        for categorydetail in lstCategoryDetail:
            musicID = int(categorydetail["songid"])
            for music in lstMusic:
                if music["id"] == musicID:
                    self.baihat=musicPer.Ui_Form(str(music["id"]),str(music["name"]),str(music["artist"]),str(music["img"]),str(music["link"]))
                    f.addWidget(self.baihat,row,0)
                    row+=1 



    def setImageToQLabelFromPlaylist(self):

        client = Client()
        client.connect()
        lstPlaylistDetail = client.sendSignal("GET_SONGS_OF_PLAYLIST_" + self.id)
        # Lấy id của bài hát đầu tiên
        first_song_id = lstPlaylistDetail[0]["songid"]
        print(first_song_id)
        # Load ảnh bài hát đầu tiên
        self.setImageToQLabel(str(first_song_id))

    def setImageToQLabel(self, listid):
        conn = Client()
        conn.connect()
        # Đọc dữ liệu ảnh từ file tạm
        image_data = conn.getImageFromServer(listid)
        # Đọc nội dung ảnh từ tệp tạm
        image_bytes = image_data.read()
        # Chuyển đổi dữ liệu ảnh sang QPixmap
        pixmap = QPixmap()
        pixmap.loadFromData(image_bytes)

        # Đặt pixmap vào QLabel
        self.image.setPixmap(pixmap)


        # Lấy kích thước QLabel
        label_width = self.image.width()
        label_height = self.image.height()

        # Lấy tỷ lệ khung hình của pixmap
        pixmap_ratio = pixmap.width() / pixmap.height()

        # Tính toán chiều rộng mới cho pixmap
        new_width = min(label_width, label_height * pixmap_ratio)

        # Tính toán chiều cao mới cho pixmap
        new_height = min(label_height, label_width / pixmap_ratio)

        # Tạo pixmap mới với kích thước đã tính toán
        scaled_pixmap = pixmap.scaled(new_width, new_height) # type: ignore
        # Thay đổi kích thước QLabel để phù hợp với ảnh
        self.image.setPixmap(scaled_pixmap)



if __name__ == "__main__":
    pl = Ui_Form()
