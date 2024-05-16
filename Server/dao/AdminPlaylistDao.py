from connection.Connection import Connection
from MusicPlaylist import MusicPlaylist
class AdminPlaylistDAO:

    def __init__(self):
        data = Connection()
        self.connection = data.connect_mysql()
    
    def get_playlist(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("SELECT p.Playlist_ID, p.Name, COALESCE(pm.Music_ID, 'None') AS Music_ID " +
            "FROM playlist p " +
            "LEFT JOIN playlist_music pm ON p.Playlist_ID = pm.Playlist_ID " +
            "LEFT JOIN music m ON pm.Music_ID = m.Music_ID;")
            records = cursor.fetchall()
            cursor.close()
            
            playlists = []
            for record in records:
                playlist = MusicPlaylist(record[0], record[1], record[2])
                playlists.append(playlist)
                
            return playlists
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
    
    def create_playlist(self, name):
        try:
            cursor = self.connection.cursor()
            cursor.execute("INSERT INTO playlist (Name) VALUES (%s)", (name,))
            self.connection.commit()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()
            return False
        finally:
            if cursor:
                cursor.close()
    
    def update_playlist(self, name, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("UPDATE playlist SET Name = %s WHERE Playlist_ID = %s;",(name, id))
            self.connection.commit()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()  # Rollback changes in case of error
            return False
        finally:
            if cursor:
                cursor.close()

    def delete_playlist(self, id):
        try:
            cursor = self.connection.cursor()
            cursor.execute("DELETE FROM playlist WHERE Playlist_ID = %s;",(id,))
            self.connection.commit()
            return True
        except Exception as e:
            print("An error occurred:", e)
            self.connection.rollback()  # Rollback changes in case of error
            return False
        finally:
            if cursor:
                cursor.close()