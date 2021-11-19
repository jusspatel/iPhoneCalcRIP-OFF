# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'iphoneripoff.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt,QCoreApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("iPhoneCalcRIP-OFF")
        MainWindow.setWindowIcon(QtGui.QIcon('logo.png'))
        MainWindow.resize(295, 478)
        MainWindow.setStyleSheet("background-color: rgb(0, 0, 0);border-top-left-radius : 41.5px;border-top-right-radius : 41.5px;border-bottom-left-radius : 41.5px;border-bottom-right-radius : 41.5px;")
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 271, 101))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.PlaceholderText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255, 128))
        brush.setStyle(QtCore.Qt.NoBrush)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.PlaceholderText, brush)
        self.lineEdit.setPalette(palette)
        self.lineEdit.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 30pt \"Segoe UI Semilight\";")
        self.lineEdit.setText("")
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom|QtCore.Qt.AlignTrailing)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(220, 120, 61, 61))
        self.pushButton_2.setStyleSheet("background-color: rgb(255,149,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(220, 190, 61, 61))
        self.pushButton_3.setStyleSheet("background-color: rgb(255,149,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(220, 260, 61, 61))
        self.pushButton_4.setStyleSheet("background-color: rgb(255,149,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(220, 330, 61, 61))
        self.pushButton_8.setStyleSheet("background-color: rgb(255,149,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(220, 400, 61, 61))
        self.pushButton_9.setStyleSheet("background-color: rgb(255,149,0);\n"
"color: rgb(255, 255, 255);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(150, 120, 61, 61))
        self.pushButton_5.setStyleSheet("background-color:rgb(212,212,210);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(80, 120, 61, 61))
        self.pushButton_6.setStyleSheet("background-color:rgb(212,212,210);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(10, 120, 61, 61))
        self.pushButton_7.setStyleSheet("background-color:rgb(212,212,210);\n"
"font: 63 14pt \"Helvetica\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(10, 191, 61, 60))
        self.pushButton_10.setStyleSheet("background-color:rgb(80,80,80);\n"
"color: rgb(212,212,210);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(80, 191, 61, 61))
        self.pushButton_11.setStyleSheet("background-color:rgb(80,80,80);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;\n"
"color: rgb(212,212,210);\n"
"")
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(150, 190, 61, 61))
        self.pushButton_12.setStyleSheet("color: rgb(212,212,210);\n"
"background-color:rgb(80,80,80);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(10, 260, 61, 61))
        self.pushButton_13.setStyleSheet("color: rgb(212,212,210);\n"
"background-color:rgb(80,80,80);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(80, 260, 61, 61))
        self.pushButton_14.setStyleSheet("color: rgb(212,212,210);\n"
"background-color:rgb(80,80,80);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(150, 260, 61, 61))
        self.pushButton_15.setStyleSheet("color: rgb(212,212,210);\n"
"background-color:rgb(80,80,80);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(10, 330, 61, 61))
        self.pushButton_16.setStyleSheet("color: rgb(212,212,210);\n"
"background-color:rgb(80,80,80);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(80, 330, 61, 61))
        self.pushButton_17.setStyleSheet("color: rgb(212,212,210);\n"
"background-color:rgb(80,80,80);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(150, 330, 61, 61))
        self.pushButton_18.setStyleSheet("color: rgb(212,212,210);\n"
"background-color:rgb(80,80,80);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(150, 400, 61, 61))
        self.pushButton_19.setStyleSheet("color: rgb(212,212,210);\n"
"background-color:rgb(80,80,80);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_20 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_20.setGeometry(QtCore.QRect(10, 400, 131, 61))
        self.pushButton_20.setStyleSheet("color: rgb(212,212,210);\n"
"background-color:rgb(80,80,80);\n"
"font: 63 14pt \"Segoe UI Semibold\";\n"
"selection-background-color: rgb(0, 170, 255);\n"
"border-radius :30px;")
        self.pushButton_20.setObjectName("pushButton_20")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QtCore.QRect(70, 474, 151, 5))
        self.pushButton.setStyleSheet(u"background-color:rgb(212,212,210);\n""")
        self.button22 = QtWidgets.QPushButton(self.centralwidget)
  
        # setting geometry of button
        self.button22.setGeometry(14, 10,16, 16)
  
        # adding action to a button
        
  
        # setting image to the button
        self.button22.setStyleSheet("background-image: url(C:/Users/admin/Downloads/close-removebg-preview.ico);")
                
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
         # update self.rect() now
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "÷"))
        self.pushButton_3.setText(_translate("MainWindow", "×"))
        self.pushButton_4.setText(_translate("MainWindow", "-"))
        self.pushButton_8.setText(_translate("MainWindow", "+"))
        self.pushButton_9.setText(_translate("MainWindow", "="))
        self.pushButton_5.setText(_translate("MainWindow", "%"))
        self.pushButton_6.setText(_translate("MainWindow", "Del"))
        self.pushButton_7.setText(_translate("MainWindow", "AC"))
        self.pushButton_10.setText(_translate("MainWindow", "7"))
        self.pushButton_11.setText(_translate("MainWindow", "8"))
        self.pushButton_12.setText(_translate("MainWindow", "9"))
        self.pushButton_13.setText(_translate("MainWindow", "4"))
        self.pushButton_14.setText(_translate("MainWindow", "5"))
        self.pushButton_15.setText(_translate("MainWindow", "6"))
        self.pushButton_16.setText(_translate("MainWindow", "1"))
        self.pushButton_17.setText(_translate("MainWindow", "2"))
        self.pushButton_18.setText(_translate("MainWindow", "3"))
        self.pushButton_19.setText(_translate("MainWindow", "."))
        self.pushButton_20.setText(_translate("MainWindow", "0"))
        self.pushButton_20.clicked.connect(self.action0)
        self.pushButton_16.clicked.connect(self.action1)
        self.pushButton_17.clicked.connect(self.action2)
        self.pushButton_18.clicked.connect(self.action3)
        self.pushButton_13.clicked.connect(self.action4)
        self.pushButton_14.clicked.connect(self.action5)
        self.pushButton_15.clicked.connect(self.action6)
        self.pushButton_10.clicked.connect(self.action7)
        self.pushButton_11.clicked.connect(self.action8)
        self.pushButton_12.clicked.connect(self.action9)
        self.pushButton_2.clicked.connect(self.action_div)
        self.pushButton_3.clicked.connect(self.action_mul)
        self.pushButton_8.clicked.connect(self.action_plus)
        self.pushButton_19.clicked.connect(self.action_point)
        self.pushButton_7.clicked.connect(self.action_clear)
        self.pushButton_4.clicked.connect(self.action_minus)
        self.pushButton_9.clicked.connect(self.action_equal)
        self.pushButton_6.clicked.connect(self.uno)
        self.pushButton_5.clicked.connect(self.moduleo)
        self.button22.clicked.connect(QCoreApplication.instance().quit)
        #self.button23.clicked.connect(self.showMinimized)
    '''def clickme(self):
        w = QtWidgets.QWidget()
        self.w.close()'''
    def action_equal(self):
  
        # get the label text
        equation = self.lineEdit.text()
        try:
        
            # getting the ans
            ans =eval(equation)

            # setting text to the label
            self.lineEdit.setText(str(ans))

        except:
            # setting text to the label
            self.lineEdit.setText("Wrong Input")
    def uno(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text[:len(text)-1])

            
    def moduleo(self):
        text = self.lineEdit.text()
        self.lineEdit.setText(text+ " % ")
        
    def action_plus(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + " + ")
  
    def action_minus(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + " - ")
  
    def action_div(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + " / ")
  
    def action_mul(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + " * ")
  
    def action_point(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + ".")
  
    def action0(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "0")
  
    def action1(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "1")
  
    def action2(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "2")
  
    def action3(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "3")
  
    def action4(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "4")
  
    def action5(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "5")
  
    def action6(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "6")
  
    def action7(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "7")
  
    def action8(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "8")
  
    def action9(self):
        # appending label text
        text = self.lineEdit.text()
        self.lineEdit.setText(text + "9")
  
    def action_clear(self):
        # clearing the label text
        self.lineEdit.setText("")
  
    def action_del(self):
        # clearing a single digit
        text = self.lineEdit.text()
        #print(text[:len(text)-1])
        self.lineEdit.setText(text[:len(text)-1])


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

