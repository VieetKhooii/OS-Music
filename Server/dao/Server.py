import socket
import threading
from PyQt6.QtCore import QThread,pyqtSignal
from MusicBUS import NhacBUS
from ctPlaylistBUS import ctPlaylistBUS
from ctCategoryBUS import ctCategoryBUS
from PlaylistBUS import PlaylistBUS
from CategoryBUS import CategoryBUS
import os
import pygame
import json

class Server(QThread):
    message_received = pyqtSignal(str)
    stopped =pyqtSignal()
    host = 'localhost'#192.168.93.104
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
    def sendPlaylistLIST(self):
        playlistBUS = PlaylistBUS()
        dataplaylist = [vars(obj) for obj in playlistBUS.getData()]
        jsonData = json.dumps(dataplaylist)
        self.clientSocket.sendall(jsonData.encode())
    def sendSongsInPlaylist(self,playListID):
        detailBUS = ctPlaylistBUS()
        datadict = [vars(obj) for obj in detailBUS.getPlayListByID(playListID)]
        jsonData = json.dumps(datadict)
        self.clientSocket.sendall(jsonData.encode())
    def sendCategoryLIST(self):
        categoryBUS = CategoryBUS()
        datadict = [vars(obj) for obj in categoryBUS.getData()]
        jsonData = json.dumps(datadict)
        self.clientSocket.sendall(jsonData.encode())
    def sendSongsInCategory(self,categoryID):
        detailBUS = ctCategoryBUS()
        datadict = [vars(obj) for obj in detailBUS.getCategoryByID(categoryID)]
        jsonData = json.dumps(datadict)
        self.clientSocket.sendall(jsonData.encode())
    def addPlayList(self,plid:str,songid:str):
        ctplbus = ctPlaylistBUS()  
        for pl in ctplbus.getPlayListByID(plid):
            if songid == str(pl.songid):
                self.clientSocket.sendall("0".encode())
                return
        ctplbus.addData(plid,songid)
        self.clientSocket.sendall("1".encode())
    def removePlayList(self,plid:str,songid:str):
        ctplbus = ctPlaylistBUS()  
        for pl in ctplbus.getPlayListByID(plid):
            if songid == str(pl.songid):
                ctplbus.delData(plid,songid)
                self.clientSocket.sendall("1".encode())
                return
        self.clientSocket.sendall("0".encode())
    def addNewPlayList(self,title:str):
        pl = PlaylistBUS()
        count = len(pl.getData()) + 1
        pl.addData(count, title)
        self.clientSocket.sendall("1".encode())

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
        elif "GET_PLAYLIST_LIST" in signal:
            self.sendPlaylistLIST()
        elif "GET_SONGS_OF_PLAYLIST" in signal:
            playlistid = signal.replace("GET_SONGS_OF_PLAYLIST_","")
            self.sendSongsInPlaylist(playlistid)
        elif (signal == "GET_CATEGORY_LIST"):
            self.sendCategoryLIST()
        elif "GET_SONGS_OF_CATEGORY" in signal:
            categoryid = signal.replace("GET_SONGS_OF_CATEGORY_","")
            self.sendSongsInCategory(categoryid)
        elif "ADD_TO_PLAYLIST" in signal:
            data = signal.replace("ADD_TO_PLAYLIST_","")
            self.message_received.emit(self.message)
            lstdata = data.split("_")
            plid = lstdata[0]
            songid=lstdata[1]
            self.addPlayList(plid,songid)
        elif "REMOVE_TO_PLAYLIST" in signal:
            data = signal.replace("REMOVE_TO_PLAYLIST_","")
            self.message_received.emit(self.message)
            lstdata = data.split("_")
            plid = lstdata[0]
            songid=lstdata[1]
            self.removePlayList(plid,songid)

        elif "ADD_PLAYLIST" in signal:
            data = signal.replace("ADD_PLAYLIST_","")
            self.message_received.emit(self.message)
            self.addNewPlayList(data)


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