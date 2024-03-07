import typing
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QMainWindow, QTableWidget, QComboBox,QTableWidgetItem, QDialog, QToolBar, QStatusBar, QMessageBox
from PyQt6.QtGui import QAction, QIcon
import sys
import mysql.connector

class DatabaseConnection:
    def __init__(self, host="localhost", database='school', user="root", password="HanaHana2010$"):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    def connect(self):
        connection = mysql.connector.connect(host=self.host, database=self.database, user=self.user, password=self.password)
        return connection
    
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")
        self.setMinimumSize(800, 600)

        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")
        edit_menu_item = self.menuBar().addMenu("&Edit")

        add_student_action = QAction(QIcon('./icons/add.png'), "Add student", self)
        add_student_action.triggered.connect(self.insert_data)
        file_menu_item.addAction(add_student_action)

        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        about_action.triggered.connect(self.show_about)
        about_action.setMenuRole(QAction.MenuRole.NoRole)

        search_action = QAction(QIcon('./icons/search.png'),"Search", self)
        edit_menu_item.addAction(search_action)
        search_action.triggered.connect(self.search_data)
        

        # Create tables
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)
        # self.table.clicked.connect(self.on_table_cell_clicked)

        # Create toolbar
        toolbar = QToolBar()
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(add_student_action)
        toolbar.addAction(search_action)

        # Create status bar
        self.statusbar = QStatusBar()
        self.setStatusBar(self.statusbar)
        self.table.cellClicked.connect(self.cell_clicked)

    def cell_clicked(self):
        edit_button = QPushButton("Edit Record")
        edit_button.clicked.connect(self.edit)
        delete_button = QPushButton("Delete Record")
        delete_button.clicked.connect(self.delete)

        children = self.findChildren(QPushButton)
        if children:
            for child in children:
                self.statusbar.removeWidget(child)
        self.statusbar.addWidget(edit_button)
        self.statusbar.addWidget(delete_button)

    def load_data(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM students")
        result = cursor.fetchall()
        self.table.setRowCount(0)
        for row, data in enumerate(result):
            self.table.insertRow(row)
            for col, col_data in enumerate(data):
                self.table.setItem(row, col, QTableWidgetItem(str(col_data)))

        connection.close()

    def edit(self):
        dialog = EditDialog()
        dialog.exec()

    def delete(self):
        dialog = Delete()
        dialog.exec()        

    def insert_data(self):
        dialog = InsertDialog()
        dialog.exec()

    def search_data(self):
        search = Search()
        search.exec()

    def show_about(self):
        dialog = About()
        dialog.exec()
               

class InsertDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Insert Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', "Physics", 'Computer Science', 'Liberal Arts']
        self.course_name.addItems(courses)
        layout.addWidget(self.course_name)

        self.mobile_phone_number = QLineEdit()
        self.mobile_phone_number.setPlaceholderText("Please provide your mobile phone number here")
        layout.addWidget(self.mobile_phone_number)

        submit_button = QPushButton("Register?")
        submit_button.clicked.connect(self.add_student)
        layout.addWidget(submit_button)

        self.setLayout (layout) 

    def add_student(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        name = self.student_name.text()
        course = self.course_name.itemText(self.course_name.currentIndex())
        mobile = self.mobile_phone_number.text()
        event = (name, course, mobile)
        sql = """INSERT INTO students(name, course, mobile)VALUES(%s,%s,%s)"""
        cursor.execute(sql, event)
        connection.commit()
        connection.close()
        main_window.load_data()

class Search(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Search student")
        self.setFixedHeight(300)
        self.setFixedWidth(300)

        layout = QVBoxLayout()

        self.student_name = QLineEdit()
        self.student_name.setPlaceholderText("Name")
        layout.addWidget(self.student_name)

        search_button = QPushButton("Search?")
        search_button.clicked.connect(self.search_student)
        layout.addWidget(search_button)

        self.setLayout (layout) 
    
    def search_student(self):
        connection = DatabaseConnection().connect()
        name = self.student_name.text()
        sql = "SELECT * FROM students WHERE name=%s"
        cursor = connection.cursor()
        cursor.execute(sql, (name,))
        result = cursor.fetchall()
        connection.commit()
        rows = list(result)
        print(rows)
        items = main_window.table.findItems(name, Qt.MatchFlag.MatchFixedString)
        for item in items:
            print(item)
            main_window.table.item(item.row(),1).setSelected(True)

        cursor.close()
        connection.close()
        
class EditDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Update Student Data")
        self.setFixedHeight(300)
        self.setFixedWidth(300)
        
        layout = QVBoxLayout()

        current_row = main_window.table.currentRow()
        self.id = main_window.table.item(current_row, 0).text()
        name = main_window.table.item(current_row,1).text()
        course = main_window.table.item(current_row,2).text()
        mobile = main_window.table.item(current_row,3).text()


        self.student_name = QLineEdit()
        self.student_name.setText(name)
        layout.addWidget(self.student_name)

        self.course_name = QComboBox()
        courses = ['Biology', 'Math', 'Astronomy', "Physics", 'Computer Science', 'Liberal Arts']
        self.course_name.addItems(courses)
        self.course_name.setCurrentText(course)
        layout.addWidget(self.course_name)

        self.mobile_phone_number = QLineEdit()
        self.mobile_phone_number.setText(mobile)
        layout.addWidget(self.mobile_phone_number)

        submit_button = QPushButton("Update?")
        submit_button.clicked.connect(self.update)
        layout.addWidget(submit_button)

        self.setLayout (layout) 

    def update(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        sql = "UPDATE students SET name=%s, course=%s, mobile=%s WHERE id=%s"
        values = (self.student_name.text(), self.course_name.itemText(self.course_name.currentIndex()), self.mobile_phone_number.text(), self.id)
        cursor.execute(sql, values)
        connection.commit()
        connection.close()
        main_window.load_data()

class Delete(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Delete Student Data")

        current_row = main_window.table.currentRow()
        self.id = main_window.table.item(current_row, 0).text()
        name = main_window.table.item(current_row, 1).text()

        layout = QGridLayout()
        notice = QLabel(f"Are you sure to delete the data for {name}?")
        layout.addWidget(notice, 0, 0, 1, 2)

        yes_button = QPushButton("Yes?")
        yes_button.clicked.connect(self.delete)
        layout.addWidget(yes_button, 1, 0)

        no_button = QPushButton("No?")
        no_button.clicked.connect(self.abort)
        layout.addWidget(no_button, 1, 1)
        self.setLayout (layout) 

    def delete(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        sql = "DELETE FROM students WHERE id=%s"
        cursor.execute(sql, (self.id,))
        connection.commit()
        connection.close()
        main_window.load_data()

        self.close()
        notice_widget = QMessageBox()
        notice_widget.setWindowTitle("Success")
        notice_widget.setText("The data was deleted successfully!")
        notice_widget.exec()

    def abort(self):
        self.close()
        notice_widget = QMessageBox()
        notice_widget.setWindowTitle("Aborting Delete Action")
        notice_widget.setText("Aborting delete action!")
        notice_widget.exec()
        main_window.load_data()

class About(QMessageBox):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("About")
        content = """
        This app was created during the course 'The Python Mega Course'.
        Feel free to modify and reuse this app.
        """
        self.setText(content)
        
    def about(self):
        pass 
app = QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
main_window.load_data()
sys.exit(app.exec())
