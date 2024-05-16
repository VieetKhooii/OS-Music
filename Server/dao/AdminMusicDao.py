from connection.Connection import Connection
from dto.Music import Music
class AdminMusicDAO:

    def __init__(self):
        data = Connection()
        self.connection = data.connect_mysql()
    

    def get_music(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("select m.*, c.Category_ID "
            +"from music m "
            +"LEFT JOIN cate_music cm ON m.Music_ID = cm.Music_ID "
            +"LEFT JOIN category c ON c.Category_ID = cm.Category_ID")
            records = cursor.fetchall()
            cursor.close()
            playlists = []
            for record in records:
                playlist = Music(record[0], record[1], record[2], record[3], record[4], record[5])
                playlists.append(playlist)
                
            return playlists
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()

    def create_music(self, name, artist, image, link, category_id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO music (Name, Artist, Image, Link) VALUES (%s, %s, %s, %s)", (name, artist, image, link))
            music_id = cursor.lastrowid
            cursor.execute("INSERT INTO cate_music (Category_ID, Music_ID) VALUES (%s, %s)", (category_id, music_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()

    def update_music(self, name, artist, image, category_id, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE music SET Name = %s, Artist = %s, Image = %s WHERE music_ID = %s;",(name, artist, image, id))
            cursor.execute("UPDATE cate_music SET Category_ID = %s WHERE music_ID = %s;",(category_id, id))
            self.connection.commit()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()  # Rollback changes in case of error
            return False
        finally:
            if cursor:
                cursor.close()

    def delete_music(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM music WHERE Music_ID = %s;",(id,))
            cursor.execute("DELETE FROM cate_music WHERE Music_ID = %s;",(id,))
            self.connection.commit()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()  # Rollback changes in case of error
            return False
        finally:
            if cursor:
                cursor.close()

    def search_music_by_name_or_artist(self, name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM music WHERE Name LIKE %s OR Artist LIKE %s", ('%' + name + '%', '%' + name + '%'))
            records = cursor.fetchall()
            return records
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()  # Rollback changes in case of error
        finally:
            if cursor:
                cursor.close()