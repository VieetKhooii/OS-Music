import data_config
from ctCategory import Cate_Music
import mysql.connector


def readData():
    connection = data_config.connect_mysql()
    lstdetail = []
    if connection is not None:
        try:
            # Tạo một đối tượng cursor
            cursor = connection.cursor()

            # Thực hiện truy vấn SQL
            cursor.execute("SELECT * FROM cate_music")

            # Lấy tất cả các dòng kết quả
            rows = cursor.fetchall()

            # In kết quả
            for row in rows:
                detail = Cate_Music(row[0],row[1],)
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
