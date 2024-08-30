from backend import Database

from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QListWidget,
)

class About_us(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(400,500)
        self.setWindowTitle("Bosh sahifa")
        self.setStyleSheet("font-size: 25px")

        self.title_label = QLabel("Bosh sahifa")
        self.title_label.setStyleSheet('font-size: 40px')

        self.sign_in_btn = QPushButton("Tizimga kirish")
        self.sign_in_btn.setFixedWidth(240)
        self.sign_in_btn.setStyleSheet("""
            background-color: green; 
            color: white;
            border-radius: 10px;
            padding: 5px
        """)
        self.sign_in_btn.clicked.connect(self.sign_in_page)

        self.sign_up_btn = QPushButton("Ro'yhatdan o'tish")
        self.sign_up_btn.setFixedWidth(240)
        self.sign_up_btn.setStyleSheet("""
            background-color: green; 
            color: white; 
            border-radius: 10px;
            padding: 5px
        """)
        self.sign_up_btn.clicked.connect(self.sign_up_page)

        self.v_box = QVBoxLayout()
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.title_label,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addStretch(6)
        self.v_box.addWidget(self.sign_in_btn,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(30)
        self.v_box.addWidget(self.sign_up_btn,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addStretch(8)

        self.setLayout(self.v_box)

        self.show()

    def sign_up_page(self):
        self.close()
        self.next_page = Sign_up()

    def sign_in_page(self):
        self.close()
        self.kirish_qismi = Sign_in()

class Sign_up(QWidget):
    def __init__(self):
        super().__init__()
        self.database = Database()

        self.setFixedSize(400,500)
        self.setWindowTitle("Ro'yhatdan o'tish")
        self.setStyleSheet("font-size: 25px")

        self.full_name = QLineEdit()
        self.full_name.setPlaceholderText('Ism Familiya')

        self.phone_number = QLineEdit()
        self.phone_number.setPlaceholderText("Telefon raqami")

        self.username = QLineEdit()
        self.username.setPlaceholderText('Username')

        self.password = QLineEdit()
        self.password.setPlaceholderText("Parol")

        self.info_label = QLabel()
        self.info_label.setStyleSheet('font-size: 17px')

        self.sign_up_btn = QPushButton("Ro'yhatdan o'tish")
        self.sign_up_btn.setStyleSheet("""
            background-color: green; 
            color: white; 
            border-radius: 10px;
            padding: 5px
        """)
        self.sign_up_btn.clicked.connect(self.sign_up)

        self.v_box = QVBoxLayout()
        self.v_box.addStretch(5)
        self.v_box.addWidget(self.full_name,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(10)
        self.v_box.addWidget(self.phone_number,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(10)
        self.v_box.addWidget(self.username,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(10)
        self.v_box.addWidget(self.password,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(15)
        self.v_box.addWidget(self.info_label,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(15)
        self.v_box.addWidget(self.sign_up_btn,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addStretch(6)

        self.setLayout(self.v_box)

        self.show()

    def sign_up(self):
        self.info_label.clear()

        full_name = self.full_name.text()
        phone_number = self.phone_number.text()
        username = self.username.text()
        password = self.password.text()

        if full_name and phone_number and username and password:
            user = {
                'full_name' : full_name,
                'phone_number' : phone_number,
                'username' : username,
                'password' : password
            }

            answer = self.database.add_user(user)

            if answer:
                self.close()
                self.next_page = Comments(username)
            else:
                self.info_label.setText("Tizimda xatolik, qayta urinib ko'ring!")
        else:
            self.info_label.setText("Barcha qatorlarni to'ldiring!")

class Sign_in(QWidget):
    def __init__(self):
        super().__init__()
        self.database = Database()

        self.setFixedSize(400,500)
        self.setWindowTitle("Tizimga kirish")
        self.setStyleSheet("font-size: 25px")

        self.username = QLineEdit()
        self.username.setPlaceholderText('Username')

        self.password = QLineEdit()
        self.password.setPlaceholderText("Parol")

        self.info_label = QLabel()
        self.info_label.setStyleSheet('font-size: 17px')

        self.sign_in_btn = QPushButton("Tizimga kirish")
        self.sign_in_btn.setStyleSheet("""
            background-color: green; 
            color: white; 
            border-radius: 10px;
            padding: 5px
        """)
        self.sign_in_btn.clicked.connect(self.sign_in)

        self.v_box = QVBoxLayout()
        self.v_box.addStretch(2)
        self.v_box.addWidget(self.username,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(10)
        self.v_box.addWidget(self.password,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(15)
        self.v_box.addWidget(self.info_label,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(15)
        self.v_box.addWidget(self.sign_in_btn,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addStretch(5)

        self.setLayout(self.v_box)

        self.show()

    def sign_in(self):
        self.info_label.clear()

        username = self.username.text()
        password = self.password.text()

        if username and password:
            user = {
                'username' : username,
                'password' : password
            }

            answer = self.database.check_user(user)

            if answer == 'empty':
                self.info_label.setText('Bunday foydalanuvchi mavjud emas!')
            elif answer == 'err':
                self.info_label.setText("Tizimda xatolik, qayta urinib ko'ring")
            else:
                self.close()
                self.next_page = Comments(username)
        else:
            self.info_label.setText("Barcha qatorlarni to'ldiring!")

class Comments(QWidget):
    def __init__(self, username: str):
        super().__init__()
        self.database = Database()

        self.username = username
        self.setFixedSize(400,500)
        self.setWindowTitle("Post")
        self.setStyleSheet("font-size: 15px")

        self.write_comment_btn = QPushButton("Post yozish")
        self.write_comment_btn.setStyleSheet("""
            background-color: green; 
            color: white; 
            border-radius: 10px;
            padding: 5px
        """)
        self.write_comment_btn.setFixedWidth(100)
        self.write_comment_btn.clicked.connect(self.write_comment_page)

        self.my_comments_btn = QPushButton("Postlarim")
        self.my_comments_btn.setStyleSheet("""
            background-color: green; 
            color: white;
            border-radius: 10px;
            padding: 5px
        """)
        self.my_comments_btn.setFixedWidth(100)
        self.my_comments_btn.clicked.connect(self.my_comments_page)

        self.h_box = QHBoxLayout()
        self.h_box.addWidget(self.write_comment_btn,0,Qt.AlignmentFlag.AlignLeft)
        self.h_box.addWidget(self.my_comments_btn,0,Qt.AlignmentFlag.AlignRight)

        self.all_comments = QListWidget()

        self.show_all_comments()

        self.v_box = QVBoxLayout()
        self.v_box.addLayout(self.h_box)
        self.v_box.addWidget(self.all_comments)

        self.setLayout(self.v_box)

        self.show()

    def show_all_comments(self):
        data = self.database.bring_all_comments()       

        for val in data:
            self.all_comments.addItem(f'Muallif: {val[0]}\n\n{val[1]}\n\n\nSana: {val[2]}')

    def write_comment_page(self):
        self.close()
        self.next_page = Write_comment(self.username)

    def my_comments_page(self):
        self.close()
        self.next_page = My_comments(self.username)

class Write_comment(QWidget):
    def __init__(self, username: str):
        super().__init__()
        self.database = Database()
        self.username = username

        self.setFixedSize(400,500)
        self.setWindowTitle("Post yozish")
        self.setStyleSheet("font-size: 20px")

        self.title_label = QLabel("Post yozish")
        self.title_label.setStyleSheet('font-size: 40px')

        self.comment_line = QLineEdit()
        self.comment_line.setPlaceholderText("Post yozing")

        self.info_label = QLabel()
        self.info_label.setStyleSheet('font-size: 17px')

        self.push_btn = QPushButton("Yuklash")
        self.push_btn.setStyleSheet("""
            background-color: green; 
            color: white; 
            border-radius: 10px;
            padding: 5px
        """)
        self.push_btn.clicked.connect(self.save_comment)

        self.get_back_btn = QPushButton('Ortga')
        self.get_back_btn.setStyleSheet("""
            background-color: blue;
            color: white;
            border-radius: 10px;
            padding: 5px
        """)
        self.get_back_btn.clicked.connect(self.previous_page)

        self.v_box = QVBoxLayout()
        self.v_box.addStretch(2)
        self.v_box.addWidget(self.title_label,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addStretch(3)
        self.v_box.addWidget(self.comment_line,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(15)
        self.v_box.addWidget(self.info_label,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addSpacing(15)
        self.v_box.addWidget(self.push_btn,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addStretch(7)
        self.v_box.addWidget(self.get_back_btn,0,Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self.v_box)

        self.show()

    def save_comment(self):
        self.info_label.clear()

        comment = self.comment_line.text()

        if comment:
            user = {
                'username' : self.username,
                'comment' : comment
            }

            answer = self.database.write_comment(user)

            if answer:
                self.info_label.setText('Post muvafaqqiyatli yuklandi')
            else:
                self.info_label.setText("Tizimda xatolik, qayta urinib ko'ring!")
        else:
            self.info_label.setText("Post yozing!")

    def previous_page(self):
        self.close()
        self.next = Comments(self.username)

class My_comments(QWidget):
    def __init__(self, username: str):
        super().__init__()
        self.username = username
        self.database = Database()

        self.setFixedSize(400,500)
        self.setWindowTitle("Mening postlarim")
        self.setStyleSheet("font-size: 15px")

        self.title_label = QLabel("Mening postlarim")
        self.title_label.setStyleSheet('font-size: 40px')

        self.my_comments = QListWidget()

        self.get_back_btn = QPushButton('Ortga')
        self.get_back_btn.setStyleSheet("""
            background-color: blue;
            color: white;
            border-radius: 10px;
            padding: 5px
        """)
        self.get_back_btn.clicked.connect(self.previous_page)

        self.show_my_comments()

        self.v_box = QVBoxLayout()
        self.v_box.addWidget(self.title_label,0,Qt.AlignmentFlag.AlignCenter)
        self.v_box.addWidget(self.my_comments)
        self.v_box.addWidget(self.get_back_btn,0,Qt.AlignmentFlag.AlignLeft)

        self.setLayout(self.v_box)

        self.show()

    def previous_page(self):
        self.close()
        self.next = Comments(self.username)

    def show_my_comments(self):
        data = self.database.bring_my_comments(self.username)

        if data:
            for val in data:
                self.my_comments.addItem(f"Muallif: {val[0]}\n\n{val[1]}\n\n\nSana: {val[2]}")

dastur = QApplication([])
oyna = About_us()
dastur.exec()