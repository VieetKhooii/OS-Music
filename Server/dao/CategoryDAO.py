import sys
from Category import Category
import mysql.connector
import data_config
def readData():
    connection = data_config.connect_mysql()
    lstCategory = []
    if connection is not None:
        try:
            # Tạo một đối tượng cursor
            cursor = connection.cursor()

            # Thực hiện truy vấn SQL
            cursor.execute("SELECT * FROM category")

            # Lấy tất cả các dòng kết quả
            rows = cursor.fetchall()

            # In kết quả
            for row in rows:
                category = Category(row[0],row[1],)
                lstCategory.append(category)

        except mysql.connector.Error as e:
            print("Lỗi truy vấn:", e)

        finally:
            
            # Đóng cursor và kết nối
            if 'cursor' in locals():
                cursor.close()
            if connection.is_connected():
                connection.close()
                print("Đã đóng kết nối")
            return lstCategory
    else:
        print("Không thể kết nối đến cơ sở dữ liệu.")

