from dao.CategoryDAO import CategoryDAO

if __name__ == "__main__":
    dao = CategoryDAO()
    list = dao.get_category()
    for i in list:
        print(i.name)