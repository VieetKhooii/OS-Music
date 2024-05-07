import sys
import os
import shutil
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QFileDialog, QPushButton, QWidget
from PyQt5.uic import loadUi
from dao.MusicDAO import MusicDAO
from dao.CategoryDAO import CategoryDAO

class SongGUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi(r"C:\Users\VieetKhooii\OneDrive\Desktop\OSMusic\OS-Music\GUI\ADMIN\SongUI.ui", self)
        self.setWindowTitle("Song")
        # self.setFixedSize(600, 400)
        self.music_dao = MusicDAO()
        self.category_dao = CategoryDAO()
        self.saveBtn.clicked.connect(self.save_music)
        self.updateBtn.clicked.connect(self.update_music)
        self.tableWidget.itemClicked.connect(self.show_selected_music)
        self.importBtn.clicked.connect(self.importFile)
        self.file_path = None
        self.populate_table()

    def importFile(self):
        options = QFileDialog.Options()
        fileName, _ = QFileDialog.getOpenFileName(self, "Select File to Import", "","All Files (*);;Text Files (*.txt)", options=options)
        if fileName:
            self.file_path = fileName
            self.fileTxt.setPlainText(self.get_last_segment(fileName))
        return fileName
    def get_last_segment(self, url):
        segments = url.split('/')
        last_segment = segments[-1]
        return last_segment

    def populate_table(self):
        try:
            music = self.music_dao.get_music()
            category = self.category_dao.get_category()
            self.tableWidget.setRowCount(0)

            for row_number, music in enumerate(music):
                self.tableWidget.insertRow(row_number)
                self.tableWidget.setItem(row_number, 0, QTableWidgetItem(str(music.id)))
                self.tableWidget.setItem(row_number, 1, QTableWidgetItem(music.name))
                self.tableWidget.setItem(row_number, 2, QTableWidgetItem(music.artist))
                self.tableWidget.setItem(row_number, 3, QTableWidgetItem(music.img))
                self.tableWidget.setItem(row_number, 4, QTableWidgetItem(music.link))
                self.tableWidget.setItem(row_number, 5, QTableWidgetItem(str(music.category_id)))
            self.categoryComboBox.clear()
            for category_item in category:
                # print(category_item.id)
                self.categoryComboBox.addItem(category_item.name + " - " + str(category_item.id))
        except Exception as e:
            print("lỗi lấy nhạc:", e)

    def save_music(self):
        if self.file_path:
            name = self.musicNameTxt.toPlainText()
            artist = self.artistTxt.toPlainText()
            thumbnail = self.thumbNailTxt.toPlainText()
            link = self.fileTxt.toPlainText()
            id = self.musicIdTxt.toPlainText()
            selected_item = self.categoryComboBox.currentText()
            category_id = selected_item.split(' - ')[-1]
            if name and not id:
                if self.music_dao.create_music(name, artist,"", link, category_id):
                    print("music created successfully.")
                    destination_dir = "C:/Users/VieetKhooii/OneDrive/Desktop/OSMusic/OS-Music/Server/songs"
                    shutil.copy(self.file_path, destination_dir)
                    print("File copied to:", destination_dir)
                    self.musicNameTxt.clear()
                    self.populate_table()
                else:
                    print("Failed to create music.")
            else:
                print("Please enter a music name and empty the ID")
        else:
            print("Vui lòng chọn nhạc trước khi thêm và không nhập ID")

    def show_selected_music(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            item_id = self.tableWidget.item(selected_row, 0).text()
            item_name = self.tableWidget.item(selected_row, 1).text()
            item_artist = self.tableWidget.item(selected_row, 2).text()
            item_image = self.tableWidget.item(selected_row, 3).text()
            item_link = self.tableWidget.item(selected_row, 4).text()
            category_id = self.tableWidget.item(selected_row, 5).text()
            self.musicIdTxt.setPlainText(item_id)
            self.musicNameTxt.setPlainText(item_name)
            self.artistTxt.setPlainText(item_artist)
            self.thumbNailTxt.setPlainText(item_image)
            self.fileTxt.setPlainText(item_link)
            index = -1
            for i in range(self.categoryComboBox.count()):
                if category_id in self.categoryComboBox.itemText(i):
                    index = i
                    break

            if index >= 0:
                self.categoryComboBox.setCurrentIndex(index)

    def update_music(self):
        name = self.musicNameTxt.toPlainText()
        id = self.musicIdTxt.toPlainText()
        if name and id:
            if self.music_dao.update_music(name, id):
                print("music updated successfully.")
                # Optionally, you can clear the text field after saving
                self.musicNameTxt.clear()
                self.populate_table()
            else:
                print("Failed to update music.")
        else:
            print("Please choose a music to update")
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SongGUI()
    window.show()
    sys.exit(app.exec_())
