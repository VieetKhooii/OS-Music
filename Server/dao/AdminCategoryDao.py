import sys
from connection.Connection import Connection
from dto.Category import Category
class AdminCategoryDAO:

    def __init__(self):
        data = Connection()
        self.connection = data.connect_mysql()
    
    def get_category(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM category")
            records = cursor.fetchall()
            cursor.close()
            
            categories = []
            for record in records:
                category = Category(record[0], record[1])
                categories.append(category)
                
            return categories
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
    
    def create_category(self, name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO category (Name) VALUES (%s)", (name,))
            self.connection.commit()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
    
    def update_category(self, name, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE category SET Name = %s WHERE Category_ID = %s;",(name, id))
            self.connection.commit()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()  # Rollback changes in case of error
            return False
        finally:
            if cursor:
                cursor.close()

    def delete_category(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM category WHERE Category_ID = %s;",(id,))
            self.connection.commit()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()  # Rollback changes in case of error
            return False
        finally:
            if cursor:
                cursor.close()