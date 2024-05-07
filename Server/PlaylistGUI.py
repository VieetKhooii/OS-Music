import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem
from PyQt5.uic import loadUi
from dao.PlaylistDAO import PlaylistDAO
from dao.MusicPlaylistDAO import MusicPlaylistDao
from dao.MusicDAO import MusicDAO

class PlaylistGUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi(r"C:\Users\VieetKhooii\OneDrive\Desktop\OSMusic\OS-Music\GUI\ADMIN\Playlist.ui", self)
        self.setWindowTitle("Playlist")
        # self.setFixedSize(600, 400)
        self.playlist_dao = PlaylistDAO()
        self.music_dao = MusicDAO()
        self.music_playlist_dao = MusicPlaylistDao()
        self.saveBtn.clicked.connect(self.save_playlist)
        self.updateBtn.clicked.connect(self.update_playlist)
        self.addToPlaylistBtn.clicked.connect(self.add_to_playlist)
        self.removeBtn.clicked.connect(self.delete_from_playlist)
        self.tableWidget.itemClicked.connect(self.show_selected_playlist)
        self.populate_table()

    def populate_table(self):
        try:
            playlists = self.playlist_dao.get_playlist()
            music = self.music_dao.get_music()
            self.tableWidget.setRowCount(0)

            for row_number, playlist in enumerate(playlists):
                self.tableWidget.insertRow(row_number)
                self.tableWidget.setItem(row_number, 0, QTableWidgetItem(str(playlist.playlistId)))
                self.tableWidget.setItem(row_number, 1, QTableWidgetItem(playlist.playlist_name))
                self.tableWidget.setItem(row_number, 2, QTableWidgetItem(str(playlist.musicId)))
            self.songComboBox.clear()
            for category_item in music:
                self.songComboBox.addItem(category_item.name + " ID: " + str(category_item.id))
        except Exception as e:
            print("Lỗi lấy playlist:", e)

    def save_playlist(self):
        name = self.playlistNameTxt.toPlainText()
        id = self.playlistIdTxt.toPlainText()
        if name and not id:
            if self.playlist_dao.create_playlist(name):
                print("playlist created successfully.")
                # Optionally, you can clear the text field after saving
                self.playlistNameTxt.clear()
                self.populate_table()
            else:
                print("Failed to create playlist.")
        else:
            print("Please enter a playlist name and empty the ID")
    
    def add_to_playlist(self):
        playlistId = self.playlistIdTxt.toPlainText()
        combo_box_data = self.songComboBox.currentText()
        data_parts = combo_box_data.split()
        musicId = data_parts[-1]
        print(combo_box_data)
        if playlistId and musicId:
            if self.music_playlist_dao.add_to_playlist(musicId, playlistId):
                print("Add to playlist successfully.")
                self.populate_table()
            else:
                print("Failed to create playlist.")
        else:
            print("Please enter a playlist name and empty the ID")

    def delete_from_playlist(self):
        selected_row = self.tableWidget.currentRow()
        playlistId = self.playlistIdTxt.toPlainText()
        musicId = self.tableWidget.item(selected_row, 2).text()
        if musicId and playlistId:
            if self.music_playlist_dao.delete_from_playlist(musicId, playlistId):
                print("Remove from playlist successfully.")
                self.populate_table()
            else:
                print("Failed to create playlist.")
        else:
            print("Please enter a playlist name and empty the ID")

    def show_selected_playlist(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            item_id = self.tableWidget.item(selected_row, 0).text()
            item_name = self.tableWidget.item(selected_row, 1).text()
            item_musicId = self.tableWidget.item(selected_row, 2).text()
            self.playlistIdTxt.setPlainText(item_id)
            self.playlistNameTxt.setPlainText(item_name)
            index = -1
            for i in range(self.songComboBox.count()):
                if item_musicId in self.songComboBox.itemText(i):
                    index = i
                    break

            if index >= 0:
                self.songComboBox.setCurrentIndex(index)

    def update_playlist(self):
        name = self.playlistNameTxt.toPlainText()
        id = self.playlistIdTxt.toPlainText()
        if name and id:
            if self.playlist_dao.update_playlist(name, id):
                print("playlist updated successfully.")
                # Optionally, you can clear the text field after saving
                self.playlistNameTxt.clear()
                self.populate_table()
            else:
                print("Failed to update playlist.")
        else:
            print("Please choose a playlist to update")
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PlaylistGUI()
    window.show()
    sys.exit(app.exec_())
