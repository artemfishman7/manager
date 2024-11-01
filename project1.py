import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import *

class SaveButton(QPushButton):
    
    def __init__(self, table_widget, line_name, line_login, line_password, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.table_widget = table_widget
        self.line_name = line_name
        self.line_login = line_login
        self.line_password = line_password

        # Подключаем функцию сохранения к кнопке
        self.clicked.connect(self.add_info)

    def add_info(self):
        
        # Получаем данные из полей
        name = self.line_name.text().strip()
        login = self.line_login.text().strip()
        password = self.line_password.text().strip()

        if not name or not login or not password:
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
            return
        

        


        # Добавляем данные в таблицу
        row_position = self.table_widget.rowCount()
        self.table_widget.insertRow(row_position)
        self.table_widget.setItem(row_position, 0, QTableWidgetItem(name))
        self.table_widget.setItem(row_position, 1, QTableWidgetItem(login))
        self.table_widget.setItem(row_position, 2, QTableWidgetItem(password))

        # Очищаем поля после добавления
        self.line_name.clear()
        self.line_login.clear()
        self.line_password.clear()

    def new_method(self, a, name):
        if name not in a:
            QMessageBox.warning(self, "Используйте пожалуйста латинские буквы")
            return


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    
    def setup_ui(self):
        self.setWindowTitle("Менеджер паролей")
        self.setGeometry(0, 0, 381, 290)
        
        central_widget = QtWidgets.QWidget(self)
        self.setCentralWidget(central_widget)
        
        # Поля ввода
        self.line_name = QLineEdit(central_widget)
        self.line_name.setPlaceholderText('название')
        self.line_name.setGeometry(10, 10, 113, 21)

        self.line_login = QLineEdit(central_widget)
        self.line_login.setPlaceholderText('логин')
        self.line_login.setGeometry(130, 10, 113, 21)

        self.line_password = QLineEdit(central_widget)
        self.line_password.setPlaceholderText('пароль')
        self.line_password.setGeometry(250, 10, 113, 21)

        # Таблица QTableWidget
        self.table_widget = QTableWidget(0, 3, central_widget)  # Начинаем с 0 строк
        self.table_widget.setGeometry(10, 40, 361, 192)
        self.table_widget.setHorizontalHeaderLabels(["Название", "Логин", "Пароль"])

        # Кнопка удаления
        self.button_delete = QPushButton("удалить", central_widget)
        self.button_delete.setGeometry(260, 230, 121, 32)
        
        # Кнопка для сохранения, с использованием нашего класса SaveButton
        self.button_save = SaveButton(self.table_widget, self.line_name, self.line_login, self.line_password, "сохранить", central_widget)
        self.button_save.setGeometry(160, 230, 113, 32)
        
        # Кнопка Показать/Скрыть
        self.button_add = QPushButton("Показать/Скрыть", central_widget)
        self.button_add.setGeometry(0, 230, 171, 32)

        self.menubar = self.menuBar()
        self.statusbar = self.statusBar()

app = QtWidgets.QApplication(sys.argv)
main_window = MainWindow()
main_window.show()
sys.exit(app.exec())
#остановился на проверке ввода на грамотное написание