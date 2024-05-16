import data_config
from ctPlaylist import Playlist_Music
import mysql.connector


def readData():
    connection = data_config.connect_mysql()
    lstdetail = []
    if connection is not None:
        try:
            # Tạo một đối tượng cursor
            cursor = connection.cursor()

            # Thực hiện truy vấn SQL
            cursor.execute("SELECT * FROM playlist_music")

            # Lấy tất cả các dòng kết quả
            rows = cursor.fetchall()

            # In kết quả
            for row in rows:
                detail = Playlist_Music(row[0],row[1],)
                lstdetail.append(detail)

        except mysql.connector.Error as e:
            print("Lỗi truy vấn:", e)

        finally:
            
            # Đóng cursor và kết nối
            if 'cursor' in locals():
                cursor.close()
            if connection.is_connected():
                connection.close()
                print("Đã đóng kết nối")
            return lstdetail
    else:
        print("Không thể kết nối đến cơ sở dữ liệu.")
def addData(id:str,songid:str):
    connection = data_config.connect_mysql()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO playlist_music(Music_ID,Playlist_ID) value(%s,%s)",(songid,id))
    connection.commit()
    cursor.close()
    connection.close()
def deleteData(id:str,songid:str):
    connection = data_config.connect_mysql()
    cursor = connection.cursor()
    cursor.execute("DELETE FROM playlist_music where Playlist_ID = %s and Music_ID = %s ", (id,songid))
    connection.commit()
    cursor.close()
    connection.close()
        