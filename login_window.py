import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton

class LoginWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login window using pyqt6")
        self.setGeometry(200, 200, 300, 150)

        self.username_label = QLabel("Username:", self)
        self.username_label.move(50, 30)

        self.username_input = QLineEdit(self)
        self.username_input.move(120, 30)

        self.password_label = QLabel("Password:", self)
        self.password_label.move(50, 70)

        self.password_input = QLineEdit(self)
        self.password_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.password_input.move(120, 70)

        self.login_button = QPushButton("Login", self)
        self.login_button.move(70, 110)
        self.login_button.clicked.connect(self.login)

        self.cancel_button = QPushButton("Cancel", self)
        self.cancel_button.move(160, 110)
        self.cancel_button.clicked.connect(self.cancel)

    def login(self):
        username = self.username_input.text()
        password = self.password_input.text()
        print("Username:", username)
        print("Password:", password)    
        # Add your login logic here

    def cancel(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    sys.exit(app.exec())
