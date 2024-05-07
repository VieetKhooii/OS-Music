import socket
import json
import pygame
import tempfile
import os
class Client():
    host = '127.0.0.1'
    port = 3306

    def __init__(self):
        self.socket = None
    def connect(self):
        try:
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.socket.connect((self.host, self.port))
            print("Connected to server")
        except Exception as e:
            print(f"Connection failed: {e}")
    def close(self):
        if self.socket:
            self.socket.close()
            print("Connection closed")
        else:
            print("No active connection")
    def receive_and_parse_json_data(self,clientSocket):
        received_data = b""
        while True:
            chunk = clientSocket.recv(4096)
            if not chunk:
                break
            received_data += chunk
        data_list = json.loads(received_data.decode())  # Chuyển đổi chuỗi JSON thành danh sách
        return data_list
    def sendSignal(self, signal):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        receiveData = b""
        try:
            if self.socket:
                # Gui tin hieu
                self.socket.sendall(signal.encode())
                print(f"Signal '{signal}' sent successfully")
                # nap ket qua vao list
                while True:
                    chunk = self.socket.recv(10000)
                    if not chunk:
                        break
                    receiveData +=chunk
                dataList = json.loads(receiveData.decode())
                return dataList
            else:
                print("Socket connection not established.")
        except Exception as e:
            print(f"Error sending signal: {e}")
    def playSongFromServer(self,songid:str):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        signal = "PLAY_SONG_" + songid
        self.socket.sendall(signal.encode())
        pygame.init()
        pygame.mixer.init()
        temp_audio_file = tempfile.SpooledTemporaryFile(max_size=10000000)  # Adjust max_size as needed
        while True:
            data = self.socket.recv(2048)
            if not data:
                break
            temp_audio_file.write(data)
        # Move the file pointer to the beginning of the temporary file
        temp_audio_file.seek(0)
        # Load the temporary file as music
        try:
            pygame.mixer.music.load(temp_audio_file)
        except pygame.error as err:
            print(f"Lỗi khi tải file âm thanh: {err}")
        else:
            print("Tải file âm thanh thành công!")
        # Play the loaded music
        try:
            pygame.mixer.music.play()
        except pygame.error as err:
            print(f"Lỗi khi tải nhạc: {err}")
        else:
            print("Tải file nhạc thành công!")

    def getSongByID(self,songid:str):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        signal = "PLAY_SONG_" + songid
        self.socket.sendall(signal.encode())
        pygame.init()
        pygame.mixer.init()
        temp_audio_file = tempfile.SpooledTemporaryFile(max_size=10000000)  # Adjust max_size as needed
        while True:
            data = self.socket.recv(2048)
            if not data:
                break
            temp_audio_file.write(data)
        # Move the file pointer to the beginning of the temporary file
        temp_audio_file.seek(0)
        # Load the temporary file as music
        return temp_audio_file

    def getImageFromServer(self,imgid:str):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect((self.host, self.port))
        signal = "GET_IMAGE_" + imgid
        self.socket.sendall(signal.encode())
        temp_image_file = tempfile.SpooledTemporaryFile(max_size=10000000)  # Adjust max_size as needed
        while True:
            data = self.socket.recv(2048)
            if not data:
                break
            temp_image_file.write(data)
                # Kiểm tra kích thước file ảnh
        image_size = temp_image_file.tell()
        if image_size == 0:
            print(f"Không nhận được dữ liệu hình ảnh.")
            return
        # Move the file pointer to the beginning of the temporary file
        temp_image_file.seek(0)
        return temp_image_file

        
client = Client()