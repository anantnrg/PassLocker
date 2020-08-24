
from PyQt5 import QtCore, QtGui, QtWidgets, QtGui
import dal as dl
import datetime
from PyQt5.QtWidgets import QMessageBox
from xml.dom import minidom
import base64
import PassLocker_Main as pl

class New_Entry(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("New_Entry")
        Dialog.setFixedSize(510, 499)
        Dialog.setWindowIcon(QtGui.QIcon("newEntry.png"))
        Dialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        Dialog.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 71, 40))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(25)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(20, 160, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(25)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(20, 200, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(25)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 47, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(25)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setGeometry(QtCore.QRect(20, 80, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(25)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(20, 280, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(25)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.group = QtWidgets.QComboBox(Dialog)
        self.group.setEnabled(True)
        self.group.setGeometry(QtCore.QRect(200, 40, 191, 22))
        self.group.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.group.setObjectName("group")
        self.group.addItem("E-MAIL")
        self.group.addItem("INTERNET")
        self.group.addItem("NETWORK")
        self.group.addItem("E-COMMERCE")
        self.group.addItem("HOME BANKING")
        self.group.addItem("MAC OS X")
        self.group.addItem("WINDOWS")
        self.group.addItem("LINUX")
        self.group.addItem("UNIX")
        self.group.addItem("SUN SOLARISIS")
        self.title = QtWidgets.QLineEdit(Dialog)
        self.title.setGeometry(QtCore.QRect(200, 80, 191, 21))
        self.title.setObjectName("title")
        self.title.setPlaceholderText("Give the title of your entry here")
        self.password = QtWidgets.QLineEdit(Dialog)
        self.password.setGeometry(QtCore.QRect(200, 160, 191, 21))
        self.password.setObjectName("password")
        self.password.setPlaceholderText("Give the password here")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.user = QtWidgets.QLineEdit(Dialog)
        self.user.setGeometry(QtCore.QRect(200, 120, 191, 21))
        self.user.setObjectName("password")
        self.user.setPlaceholderText("Give the user name here")
        self.password2 = QtWidgets.QLineEdit(Dialog)
        self.password2.setGeometry(QtCore.QRect(200, 200, 191, 21))
        self.password2.setObjectName("password2")
        self.password2.setPlaceholderText("Repeat the same password as above")
        #self.password2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.url = QtWidgets.QLineEdit(Dialog)
        self.url.setGeometry(QtCore.QRect(200, 240, 191, 21))
        self.url.setObjectName("url")
        self.url.setPlaceholderText("Give the URL of your entry here")
        self.notes = QtWidgets.QPlainTextEdit(Dialog)
        self.notes.setGeometry(QtCore.QRect(200, 280, 251, 161))
        self.notes.setObjectName("notes")
        self.notes.setPlaceholderText("Give any notes if you have here")
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(240, 460, 251, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Save)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName("buttonBox")
        self.buttonBox.clicked.connect(self.clickMethod)
            
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        

    def clickMethod(self):
        import sys
        if self.password.text() == self.password2.text():
                self.buttonBox.setDisabled(2)
                date = datetime.datetime.now()
                ID = '%s%s%s%s%s%s' % (date.year, date.month, date.day, date.hour,date.minute,date.second) 
                psw =  self.password.text()
                psw = psw.encode("utf-8")
                psw = base64.b64encode(psw) 
                psw = psw.decode("utf-8")
                print(psw)
                dl.writeLineToCSV(ID, self.group.currentText().strip(), 
                            self.title.text().strip(), self.user.text().strip(), psw , self.url.text().strip(), self.notes.toPlainText().strip())
               
                                
        else:
                pass


    
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "NEW ENTRY"))
        self.label.setText(_translate("Dialog", "Group"))
        self.label_2.setText(_translate("Dialog", "User Name"))
        self.label_3.setText(_translate("Dialog", "Password"))
        self.label_4.setText(_translate("Dialog", "Confirm Passowrd"))
        self.label_5.setText(_translate("Dialog", "URL"))
        self.label_6.setText(_translate("Dialog", "Title"))
        self.label_7.setText(_translate("Dialog", "Notes"))
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = New_Entry()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

