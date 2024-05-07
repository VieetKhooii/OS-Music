from connection.Connection import Connection
from dto.Music import Music
class MusicDAO:

    def __init__(self):
        data = Connection()
        self.connection = data.connect_mysql()
    
    def readData(self):
        try:
            lstMusic = []
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM music")
            rows = cursor.fetchall()
            for row in rows:
                music = Music(row[0],row[1],row[2],row[3],row[4],)
                lstMusic.append(music)
            return lstMusic
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()

    def addData(self, music:Music):
        cursor = self.connection.cursor()
        sql = "INSERT INTO music VALUE()"
        cursor.execute(sql)

    def get_music(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT * FROM music")
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
            cursor.execute("INSERT INTO music (Name, Artist, Image, Link, Category_ID) VALUES (%s, %s, %s, %s, %s)", (name, artist, image, link, category_id))
            self.connection.commit()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
    
    def update_music(self, name, artist, image, link, category_id, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE music SET Name = %s, Artist = %s, Image = %s, Link = %s, Category_ID = %s WHERE music_ID = %s;",(name, artist, image, link, category_id, id))
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
