import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTableWidgetItem, QVBoxLayout
from PyQt5.uic import loadUi
from AdminCategoryDao import AdminCategoryDAO

class CategoryGUI(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        loadUi(r"C:\Users\VieetKhooii\OneDrive\Documents\ForkGit\OS-Music\GUI\ADMIN\Category.ui", self)
        self.setWindowTitle("Category")
        # self.setFixedSize(600, 400)
        self.category_dao = AdminCategoryDAO()  # Create an instance of CategoryDAO
        self.saveBtn.clicked.connect(self.save_category)
        self.updateBtn.clicked.connect(self.update_category)
        self.tableWidget.itemClicked.connect(self.show_selected_category)
        self.populate_table()

    def populate_table(self):
        try:
            categories = self.category_dao.get_category()

            self.tableWidget.setRowCount(0)

            for row_number, category in enumerate(categories):
                self.tableWidget.insertRow(row_number)
                self.tableWidget.setItem(row_number, 0, QTableWidgetItem(str(category.id)))
                self.tableWidget.setItem(row_number, 1, QTableWidgetItem(category.name))
        except Exception as e:
            print("An error occurred while populating the table:", e)

    def save_category(self):
        name = self.categoryNameTxt.toPlainText()
        id = self.categoryIdTxt.toPlainText()
        if name and not id:
            if self.category_dao.create_category(name):
                print("Category created successfully.")
                self.categoryNameTxt.clear()
            else:
                print("Failed to create category.")
        else:
            print("Please enter a category name and empty the ID")

    def show_selected_category(self):
        selected_row = self.tableWidget.currentRow()
        if selected_row >= 0:
            item_id = self.tableWidget.item(selected_row, 0).text()
            item_name = self.tableWidget.item(selected_row, 1).text()
            self.categoryIdTxt.setPlainText(item_id)
            self.categoryNameTxt.setPlainText(item_name)

    def update_category(self):
        name = self.categoryNameTxt.toPlainText()
        id = self.categoryIdTxt.toPlainText()
        if name and id:
            if self.category_dao.update_category(name, id):
                print("Category updated successfully.")
                # Optionally, you can clear the text field after saving
                self.categoryNameTxt.clear()
                self.populate_table()
            else:
                print("Failed to update category.")
        else:
            print("Please choose a category to update")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CategoryGUI()
    window.show()
    sys.exit(app.exec_())
