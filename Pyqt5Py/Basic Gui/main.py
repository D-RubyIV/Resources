
import os, sys
from PyQt5 import QtCore,QtWidgets,QtGui,QtTest
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtCore import QPropertyAnimation, QPoint,QTimer,QCoreApplication
from PyQt5.QtWidgets import * 
from PyQt5.QtCore import *
from PyQt5.QtGui import QIcon
os.system("pyuic5 untitled.ui -o untitled.py")
from untitled import  Ui_MainWindow

class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self). __init__()
        global UI
        self.UI = UI =  Ui_MainWindow()
        self.UI.setupUi(self)
        self.setWindowTitle("Telegram Online Member - By @ImDion_204")
     



def main():
    app = QApplication(sys.argv)
    application = ApplicationWindow()
    application.show()
    try:
        sys.exit(app.exec_())
    except SystemExit:
        print("Closing App")
        sys.exit()


if __name__ == "__main__":
    main()
