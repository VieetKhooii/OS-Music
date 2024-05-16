import CategoryDAO
class CategoryBUS:
    def __init__(self):
        self.lstCategory = CategoryDAO.readData()
    def getData(self):
        return self.lstCategory