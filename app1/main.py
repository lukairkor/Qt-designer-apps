#!/usr/bin/env python3
import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic





if __name__ == "__main__":

    app = QtWidgets.QApplication(sys.argv)
    self.dlg = uic.loadUi("temple_ui.ui", self)



    # MainWindow = QtWidgets.QMainWindow()
    # ui = Ui_MainWindow()    
    # ui.setupUi(MainWindow)
    dlg.show()
    
    sys.exit(app.exec_())