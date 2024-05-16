import PlaylistDAO
class PlaylistBUS:
    def __init__(self):
        self.lstPlaylist = PlaylistDAO.readData()
    def getData(self):
        return self.lstPlaylist
    def addData(self, id, title):
        PlaylistDAO.addData(id, title)