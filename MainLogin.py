from PyQt5 import QtWidgets, QtGui
import PassLocker_Main as ps

class Login(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super(Login, self).__init__(parent)
        self.setWindowTitle( "MASTER PASSWORD")
        self.setWindowIcon(QtGui.QIcon("PassLockerIcon.png"))
        self.resize(220, 100)
        self.textName = QtWidgets.QLabel("MASTER PASSWORD", self)
        self.textPass = QtWidgets.QLineEdit(self)
        self.textPass.setEchoMode(QtWidgets.QLineEdit.Password)
        self.buttonLogin = QtWidgets.QPushButton('Login', self)
        self.buttonLogin.clicked.connect(self.handleLogin)
        layout = QtWidgets.QVBoxLayout(self)
        layout.addWidget(self.textName)
        layout.addWidget(self.textPass)
        layout.addWidget(self.buttonLogin)

    def handleLogin(self):
        if (self.textPass.text() == 'admin'):
            self.accept()        
            
        else:
            QtWidgets.QMessageBox.critical(self, 'Wrong Password', 'You typed the wrong password ! Please correct it.')
            self.textPass.clear()
                
if __name__ == '__main__':

    import sys
    app = QtWidgets.QApplication(sys.argv)
    login = Login()

    if login.exec_() == QtWidgets.QDialog.Accepted:
        window = ps.PassLocker_Main()
        window.show()
        sys.exit(app.exec_())