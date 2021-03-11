import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import re
path = os.path.dirname(__file__) #uic paths from itself, not the active dir, so path needed
qtCreatorFile = "/home/lukas/Programowanie_kod/Do_CV_github/Qt-designer-apps/app2/temple.ui" #Ui file name, from QtDesigner, assumes in same folder as this .py

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) #process through pyuic

class MyApp(QMainWindow, Ui_MainWindow): #gui class
    def __init__(self):
        #The following sets up the gui via Qt
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    ##set up callbacks
        self.ui.b1.clicked.connect(self.on_button1_clicked)
        self.ui.b2.clicked.connect(self.on_button2_clicked)

    def on_button1_clicked(self):
        self.ui.label.setText("Pierwszy")

    def on_button2_clicked(self):
        self.ui.label.setText("Drugi")


if __name__ == "__main__":
    app = QApplication(sys.argv) #instantiate a QtGui (holder for the app)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())