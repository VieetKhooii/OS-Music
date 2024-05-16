import ctCategoryDAO
class ctCategoryBUS:
    def __init__(self):
        self.lstCategoryDetail = ctCategoryDAO.readData()
    def getData(self):
        return self.lstCategoryDetail
    def getCategoryByID(self,id:str):
        lst = []
        for item in self.lstCategoryDetail:
            
            if str(item.cateid) == id:
                
                lst.append(item)
        return lst
            
        