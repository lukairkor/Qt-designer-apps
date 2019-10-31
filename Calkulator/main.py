import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import re
path = os.path.dirname(__file__) #uic paths from itself, not the active dir, so path needed
qtCreatorFile = "Qt designer apps/Calkulator/temple.ui" #Ui file name, from QtDesigner, assumes in same folder as this .py

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) #process through pyuic

class MyApp(QMainWindow, Ui_MainWindow): #gui class
    def __init__(self):
        #The following sets up the gui via Qt
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    ##set up callbacks
        # self.ui.b1.clicked.connect(self.on_button1_clicked)
        # self.ui.b2.clicked.connect(self.on_button2_clicked)
        self.ui.b1.clicked.connect(self.on_button2_clicked)
        self.ui.b2.clicked.connect(self.on_button2_clicked)
        self.ui.b3.clicked.connect(self.on_button2_clicked)
        self.ui.b4.clicked.connect(self.on_button2_clicked)
        self.ui.b5.clicked.connect(self.on_button2_clicked)
        self.ui.b6.clicked.connect(self.on_button2_clicked)
        self.ui.b7.clicked.connect(self.on_button2_clicked)
        self.ui.b8.clicked.connect(self.on_button2_clicked)
        self.ui.b9.clicked.connect(self.on_button2_clicked)

        self.ui.b_mnozy.clicked.connect(self.on_b_mnozy_clicked)
        self.ui.b_dzieli.clicked.connect(self.on_b_dzieli_clicked)
        self.ui.b_plus.clicked.connect(self.on_b_plus_clicked)
        self.ui.b_minus.clicked.connect(self.on_b_minus_clicked)

    # def on_button1_clicked(self):
    #     self.ui.label.setText("Pierwszy")

    def on_button2_clicked(self):
        number = 0
        if on_button2_clicked == ui.b1:
            self.ui.lcd.display(4.5792)

    #Operration Functions
    def on_b_mnozy_clicked(self):
        self.ui.lcd.display(4.5792)
    def on_b_dzieli_clicked(self):
        self.ui.lcd.display(4.5792)
    def on_b_plus_clicked(self):
        self.ui.lcd.display(4.5792)
    def on_b_minus_clicked(self):
        self.ui.lcd.display(4.5792)


if __name__ == "__main__":
    app = QApplication(sys.argv) #instantiate a QtGui (holder for the app)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())