import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from New_entry import New_Entry

class Add_Pass(New_Entry):
    def __init__(self, dialog):
        New_Entry.__init__(self)
        self.setupUi(dialog)
		



	
if __name__ == '__main__':
	app = QtWidgets.QApplication(sys.argv)
	dialog = QtWidgets.QDialog()

	prog = Add_Pass(dialog)

	dialog.show()
	sys.exit(app.exec_())