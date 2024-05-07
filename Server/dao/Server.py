import socket
import threading
from PyQt6.QtCore import QThread,pyqtSignal
from MusicBUS import NhacBUS
import os
import pygame
import json

class Server(QThread):
    message_received = pyqtSignal(str)
    stopped =pyqtSignal()
    host = '192.168.93.104'
    port = 3306
    def __init__(self):
        super().__init__()
        self.running = False
        self.host = Server.host
        self.port = Server.port
        self.serverSocket = None
        self.clientSocket = None
        self.clientAddress = None
        
        self.message = ""
    def run(self):
        self.running = True
        try:
            self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.serverSocket.bind((self.host, self.port))
            self.serverSocket.listen(1)
            print(f"Server is listening on {self.host}: {self.port}")
            self.message = f"Server is listening on {self.host}: {self.port}"
            while True:
                self.getSignal()
                self.message_received.emit(self.message)
        except Exception as e:
            print (f'Error starting server: {e}')
            self.stopped.emit()
    def stop(self):
        self.running = False
        try:
            if self.clientSocket:
                self.clientSocket.close()
            if self.serverSocket:
                self.serverSocket.close()
            print("Server stopped")
        except Exception as e:
            print(f"Error stopping server: {e}")
    def sendMusic(self,songID):
        nhacBUS = NhacBUS()
        mp3 = nhacBUS.getMP3FileByID(songID)
        filePath = os.path.join("Server/dao/songs", mp3)
        absolutePath = os.path.abspath(filePath)
        print(absolutePath)
        with open(absolutePath, "rb") as music_file:
            data = music_file.read(2048)
            while data:
                self.clientSocket.sendall(data)
                data = music_file.read(2048)
    def sendMusicLIST(self):
        musicBUS = NhacBUS()
        datadict = [vars(obj) for obj in musicBUS.getData()]
        jsonData = json.dumps(datadict)
        self.clientSocket.sendall(jsonData.encode())
    def getSignal(self):
        self.clientSocket, self.clientAddress = self.serverSocket.accept()
        print(f"Connection established with {self.clientAddress}")
        signal = self.clientSocket.recv(1024).decode("utf-8")
        self.message = signal
        print( "Tin hieu tu client: ",signal)
        if "PLAY_SONG" in signal:
            songid = signal.replace("PLAY_SONG_","")
            self.sendMusic(songid)
        elif "GET_MUSIC_LIST" in signal:
            self.sendMusicLIST()
        elif "GET_IMAGE" in signal:
            imgid = signal.replace("GET_IMAGE_","")
            self.sendImage(imgid)

        self.clientSocket.close()

        
    def sendImage(self, imageID):
        musicBUS = NhacBUS()  # Thay thế HinhAnhBUS bằng lớp nghiệp vụ hình ảnh của bạn
        image_path = musicBUS.getImageByID(imageID)

        if image_path is None:
        # Xử lý trường hợp image_path rỗng (None)
        # Ví dụ: sử dụng giá trị mặc định cho filePath
            filePath = os.path.join("Server/dao/imgs", "ni.jpg")
        else:
            filePath = os.path.join("Server/dao/imgs", image_path)
        
        absolute_path = os.path.abspath(filePath)   

        # Mở file ảnh ở chế độ đọc binary
        with open(absolute_path, "rb") as image_file:
            data = image_file.read(2048)
            while data:
                self.clientSocket.sendall(data)
                data = image_file.read(2048)
server = Server()
server.run()