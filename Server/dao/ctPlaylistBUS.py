import ctPlaylistDAO
class ctPlaylistBUS:
    def __init__(self):
        self.lstPlaylistDetail = ctPlaylistDAO.readData()
    def getData(self):
        return self.lstPlaylistDetail
    def getPlayListByID(self,id:str):
        lst = []
        for item in self.lstPlaylistDetail:
            
            if str(item.playlistID) == id:
                
                lst.append(item)
        return lst
    def addData(self,id:str,songid:str):
        ctPlaylistDAO.addData(id,songid)  
    def delData(self,id:str,songid:str):
        ctPlaylistDAO.deleteData(id,songid)