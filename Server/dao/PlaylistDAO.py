from Playlist import Playlist
from MusicPlaylist import MusicPlaylist
import data_config
from ctPlaylist import Playlist_Music
import mysql.connector

def readData():
    connection = data_config.connect_mysql()
    lstPlaylist = []
    if connection is not None:
        try:
            # Tạo một đối tượng cursor
            cursor = connection.cursor()

            # Thực hiện truy vấn SQL
            cursor.execute("SELECT * FROM playlist")

            # Lấy tất cả các dòng kết quả
            rows = cursor.fetchall()

            # In kết quả
            for row in rows:
                playlist = Playlist(row[0],row[1],)
                lstPlaylist.append(playlist)

        except mysql.connector.Error as e:
            print("Lỗi truy vấn:", e)

        finally:
            
            # Đóng cursor và kết nối
            if 'cursor' in locals():
                cursor.close()
            if connection.is_connected():
                connection.close()
                print("Đã đóng kết nối")
            return lstPlaylist
    else:
        print("Không thể kết nối đến cơ sở dữ liệu.")
def addData(id:str, title:str):
    connection = data_config.connect_mysql()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO playlist(Playlist_ID,Name) value(%s,%s)",(id,title))
    connection.commit()
    cursor.close()
