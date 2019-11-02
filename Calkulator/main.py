import sys
import os
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic
import re
from functools import partial

path = os.path.dirname(__file__) #uic paths from itself, not the active dir, so path needed
qtCreatorFile = "Qt designer apps/Calkulator/temple.ui" #Ui file name, from QtDesigner, assumes in same folder as this .py

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile) #process through pyuic

class MyApp(QMainWindow, Ui_MainWindow): #gui class
    
    a = 0
    b = 0
    c = 0
    makro2 = 0
    makro3 = 0
    makro4 = 0
    mem = []
    x =0
    z = 0

    def __init__(self):
        #The following sets up the gui via Qt
        super(MyApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    ##set up callbacks

        self.ui.b0.clicked.connect(partial(self.function, self.ui.b0))
        self.ui.b1.clicked.connect(partial(self.function, self.ui.b1))
        self.ui.b2.clicked.connect(partial(self.function, self.ui.b2))
        self.ui.b3.clicked.connect(partial(self.function, self.ui.b3))
        self.ui.b4.clicked.connect(partial(self.function, self.ui.b4))
        self.ui.b5.clicked.connect(partial(self.function, self.ui.b5))
        self.ui.b6.clicked.connect(partial(self.function, self.ui.b6))
        self.ui.b7.clicked.connect(partial(self.function, self.ui.b7))
        self.ui.b8.clicked.connect(partial(self.function, self.ui.b8))
        self.ui.b9.clicked.connect(partial(self.function, self.ui.b9))
        self.ui.dell.clicked.connect(partial(self.function, self.ui.dell))

        self.ui.b_dzieli.clicked.connect(partial(self.function, self.ui.b_dzieli))
        self.ui.b_plus.clicked.connect(partial(self.function, self.ui.b_plus))
        self.ui.b_minus.clicked.connect(partial(self.function, self.ui.b_minus))
        self.ui.b_mnozy.clicked.connect(partial(self.function, self.ui.b_mnozy))
        self.ui.rowna.clicked.connect(partial(self.function, self.ui.rowna))

    def function(self, btn): 

        if btn == self.ui.b0:
            self.mem.append(0)

        elif btn == self.ui.b1:
            q = 1
            self.mem = self.mem + [q]

        elif btn == self.ui.b2:
            q = 2
            self.mem = self.mem + [q] 
            
        elif btn == self.ui.b3:
            self.mem.append(3)

        elif btn == self.ui.b4:
            self.mem.append(4)

        elif btn == self.ui.b5:
            self.mem.append(5)

        elif btn == self.ui.b6:
            self.mem.append(6)

        elif btn == self.ui.b7:
            self.mem.append(7)

        elif btn == self.ui.b8:
            self.mem.append(8)

        elif btn == self.ui.b9:
            self.mem.append(9)
            
        elif btn == self.ui.b_dzieli:
            self.makro2 = 1
            self.makro3 = self.z
            self.z = 0
            self.mem = []
            self.ui.lcd.display('-')
          
        elif btn ==self.ui.b_plus:
            self.makro2 = 2
            self.makro3 = self.z
            self.z = 0
            self.mem = []
            self.ui.lcd.display('-')
           
        elif btn == self.ui.b_minus:
            self.makro2 = 3
            self.makro3 = self.z
            self.z = 0
            self.mem = []
            self.ui.lcd.display('-')
       
        elif btn == self.ui.b_mnozy:
            self.makro2 = 4
            self.makro3 = self.z
            self.z = 0
            self.mem = [] 
            self.ui.lcd.display('-')

        elif btn == self.ui.dell:
            self.ui.lcd.display('-')
            self.z = 0
            self.mem = []
            self.makro4 = 0
            
        elif btn == self.ui.rowna:
            print(self.makro4,' makro4 in rowna\n--------------------------')    
            self.equations()
            self.mem = [] 

        for self.x in range(len(self.mem)):
            aa = self.mem[self.x]
            self.z = str(aa)+str(self.z)

        self.mem = []
        self.z = str(self.z)
        self.z = re.sub('[$0]', '', self.z)

        if ((self.makro2 == 1) or (self.makro2 == 2) or (self.makro2 == 3) or (self.makro2 == 4) or (self.makro2 == 0)):
            self.ui.lcd.display(self.z)
        else:
            self.ui.lcd.display(self.makro4)
        print(self.makro4,' makro4 in function\n--------------------------')     

    def equations(self):   
        
        a=float(self.makro3)
        b=float(self.z)  
        print(self.makro4,' makro4 in equations begin\n--------------------------') 

        if self.makro2==1:
            if self.makro4 ==0:  
                c = a/b
                self.makro4=c
            else:
                o=float(self.makro4)  
                c = o/b
                self.makro4=c
            
        elif self.makro2==2:
            if self.makro4 ==0:  
                c = a+b
                self.makro4=c
            else:
                o=float(self.makro4)  
                c = o+b
                self.makro4=c
            
        elif self.makro2==3:
            if self.makro4 ==0:
                c = a-b
                self.makro4=c
            else:
                o=float(self.makro4)  
                c = o-b
                self.makro4=c
             
        elif self.makro2==4:
            if self.makro4 ==0:  
                c = a*b
                self.makro4=c
            else:
                o=float(self.makro4)  
                c = o*b
                self.makro4=c
        
        self.makro2 = 5
        print(a,' a')
        print(b,' b')
        # print(c,' c')
        print(self.makro4,' makro4 in equations end\n--------------------------') 
        
if __name__ == "__main__":
    app = QApplication(sys.argv) #instantiate a QtGui (holder for the app)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())