from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from test1 import Ui_Dialog
import sys

app = QApplication(sys.argv)
widget = QWidget()
ui = Ui_Dialog()
ui.setupUi(widget)   #general fixed codes before line10, just pull the resource from pyqt

tmp = ""

#def buttonClick():
    #text = float(ui.lineEdit_3.text())
    #text2 = float(ui.lineEdit_4.text())
    #result = str(text + text2)
    #ui.label.setText(result)

    #messageBox = QMessageBox()
    #messageBox.setWindowTitle("Result")  #how about Mac??
    #messageBox.setInformativeText(result) #informative func uses string only
    #messageBox.exec_()

#ui.pushButton.clicked.connect(buttonClick)

def set_value(value):
    global tmp
    tmp = tmp + value
    ui.label_4.setText(tmp)

def buttonClick1():
    set_value("1")  #shortened the code by putting the routine jobs to a function from line27~30

def buttonClick2():
    global tmp
    tmp = tmp + "2"
    ui.label_4.setText(tmp)

def buttonClick3():
    global tmp
    global tmp2
    tmp = ""
    tmp2 = ""
    ui.label_4.setText(tmp)
    ui.label_3.setText(tmp2)

def buttonClick4():
    global tmp
    tmp = tmp + "3"
    ui.label_4.setText(tmp)

def add(): #to sum
    global tmp
    global tmp2
    ui.label_3.setText(tmp + "+")
    ui.label_4.setText("")
    tmp2 = tmp
    tmp = ""

def equal():
    global tmp
    global tmp2
    result = int(tmp) + int(tmp2)
    ui.label_4.setText(str(result))
    tmp = ""
    tmp2 = ""
    ui.label_3.setText("")
    

ui.pushButton_2.clicked.connect(buttonClick1)
ui.pushButton_3.clicked.connect(buttonClick2)
ui.pushButton.clicked.connect(buttonClick3)
ui.pushButton_4.clicked.connect(buttonClick4)
ui.pushButtonAdd.clicked.connect(add)
ui.pushButtonEqual.clicked.connect(equal)


widget.show()    #general fixed codes 
app.exec_()   #general fixed codes 