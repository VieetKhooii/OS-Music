# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QScrollArea, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QTabWidget
# from PyQt5.uic import loadUi
# from CategoryGUI import CategoryGUI
# from SongGUI import SongGUI
# # from PlaylistGUI import PlaylistGUI 
# from dao.Server import Server

# class MusicAdminGUI(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         loadUi(r"C:\Users\VieetKhooii\OneDrive\Documents\ForkGit\OS-Music\GUI\ADMIN\MusicAdmin.ui", self)
#         # self.server = Server()
#         self.setWindowTitle("ADMIN")
#         self.scroll_area = QScrollArea(self)
#         self.scroll_area.setGeometry(270, 90, 871, 491)
#         self.scroll_area.setWidget(self.containerWidget) 
#         # self.setFixedSize(1141, 622)
#         self.nhacBtn.clicked.connect(self.show_music_tab)
#         # self.playlistBtn.clicked.connect(self.show_playlist_tab)
#         self.theLoaiBtn.clicked.connect(self.show_category_tab)

#     def show_music_tab(self):
#         # self.tabs.setCurrentIndex(0)
#         self.headerLabel.setText("Nhạc")
#         self.show_music_gui()

#     # def show_playlist_tab(self):
#     #     # self.tabs.setCurrentIndex(1)
#     #     self.headerLabel.setText("Playlist")
#     #     self.show_playlist_gui()

#     def show_category_tab(self):
#         # self.tabs.setCurrentIndex(2)
#         self.headerLabel.setText("Thể loại")
#         self.show_category_gui()
    
#     def show_category_gui(self):
#         if hasattr(self, 'current_gui'):
#             self.current_gui.hide()
#         self.category_gui = CategoryGUI(self.containerWidget)
#         self.category_gui.show()
#         self.containerWidget.adjustSize()
#         self.scroll_area.updateGeometry()
#         self.current_gui = self.category_gui

#     def show_music_gui(self):
#         if hasattr(self, 'current_gui'):
#             self.current_gui.hide()
#         self.music_gui = SongGUI(self.containerWidget)
#         self.music_gui.show()
#         self.containerWidget.adjustSize()
#         self.scroll_area.updateGeometry()
#         self.current_gui = self.music_gui

#     def start_server(self):
#         Server.run()

#     # def show_playlist_gui(self):
#     #     if hasattr(self, 'current_gui'):
#     #         self.current_gui.hide()
#     #     self.playlist_gui = PlaylistGUI(self.containerWidget)
#     #     self.playlist_gui.show()
#     #     self.containerWidget.adjustSize()
#     #     self.scroll_area.updateGeometry()
#     #     self.current_gui = self.playlist_gui

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = MusicAdminGUI()
#     window.show()
#     sys.exit(app.exec_())
