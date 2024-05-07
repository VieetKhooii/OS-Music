from PyQt6 import QtCore, QtGui, QtWidgets
import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import Qt


class AlbumGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        # Thiết lập kích thước và màu nền cho QWidget
        content_frame = QFrame(self)
        content_frame.setFrameShape(QFrame.Shape.Box)  # Đặt kiểu viền là Box
        content_frame_layout = QVBoxLayout(content_frame)

        # Thêm các thành phần vào QFrame
        label = QLabel("Đây là trang quản lý Album")
        label.setStyleSheet("font-size: 15px")
        content_frame_layout.addWidget(label)

        # Thiết lập QFrame làm content pane của QMainWindow

        # Đặt kích thước cho QWidget
        content_frame.setFixedSize(741, 550)
        

        self.setWindowTitle("Example")