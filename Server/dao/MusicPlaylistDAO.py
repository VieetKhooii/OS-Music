# # from connection.Connection import Connection
# from dto.MusicPlaylist import MusicPlaylist
# class MusicPlaylistDao:
     
#     # def __init__(self):
#     #     data = Connection()
#     #     self.connection = data.connect_mysql()

#     def add_to_playlist(self, musicId, playlistId):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute("INSERT INTO playlist_music (Music_ID, Playlist_ID) VALUES (%s, %s)", (musicId, playlistId))
#             self.connection.commit()
#             return True
#         except Exception as e:
#             print("An error occurred:", e)
#             self.connection.rollback()
#             return False
#         finally:
#             if cursor:
#                 cursor.close()

#     def delete_from_playlist(self, musicId, playlistId):
#         try:
#             cursor = self.connection.cursor()
#             cursor.execute("DELETE FROM playlist_music WHERE Music_ID = %s AND Playlist_ID = %s;",(musicId, playlistId))
#             self.connection.commit()
#             return True
#         except Exception as e:
#             print("An error occurred:", e)
#             self.connection.rollback()  # Rollback changes in case of error
#             return False
#         finally:
#             if cursor:
#                 cursor.close()