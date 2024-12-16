# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'client\GUI\gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1820, 890)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 1921, 881))
        self.frame.setStyleSheet("QFrame{\n"
"background-color:rgb(56,58,89);\n"
"color:rgb(220,220,220);\n"
"border-radius:10px;\n"
"}\n"
"")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(20, 10, 341, 70))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox  {\n"
"    font: 11pt \"Constantia\";\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}")
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.series_combo = QtWidgets.QComboBox(self.groupBox)
        self.series_combo.setGeometry(QtCore.QRect(10, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.series_combo.setFont(font)
        self.series_combo.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"background-color:rgb(56,58,89);")
        self.series_combo.setObjectName("series_combo")
        self.groupBox_8 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_8.setGeometry(QtCore.QRect(20, 100, 341, 70))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_8.setFont(font)
        self.groupBox_8.setStyleSheet("QGroupBox  {\n"
"    font: 11pt \"Constantia\";\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}")
        self.groupBox_8.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_8.setObjectName("groupBox_8")
        self.model_combo = QtWidgets.QComboBox(self.groupBox_8)
        self.model_combo.setGeometry(QtCore.QRect(10, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.model_combo.setFont(font)
        self.model_combo.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"background-color:rgb(56,58,89);")
        self.model_combo.setObjectName("model_combo")
        self.model_combo.addItem("")
        self.model_combo.setItemText(0, "")
        self.groupBox_5 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_5.setGeometry(QtCore.QRect(20, 270, 341, 330))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet("QGroupBox  {\n"
"    font: 11pt \"Constantia\";\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}")
        self.groupBox_5.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_6.setGeometry(QtCore.QRect(10, 30, 321, 131))
        self.groupBox_6.setObjectName("groupBox_6")
        self.out_pic = QtWidgets.QComboBox(self.groupBox_6)
        self.out_pic.setGeometry(QtCore.QRect(10, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.out_pic.setFont(font)
        self.out_pic.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"background-color:rgb(56,58,89);")
        self.out_pic.setObjectName("out_pic")
        self.out_pic_lbl = QtWidgets.QLabel(self.groupBox_6)
        self.out_pic_lbl.setGeometry(QtCore.QRect(250, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.out_pic_lbl.setFont(font)
        self.out_pic_lbl.setStyleSheet(" \n"
"font: 11pt \"Constantia\";\n"
"color: white;\n"
"")
        self.out_pic_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_pic_lbl.setObjectName("out_pic_lbl")
        self.out_pvh = QtWidgets.QComboBox(self.groupBox_6)
        self.out_pvh.setGeometry(QtCore.QRect(10, 80, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.out_pvh.setFont(font)
        self.out_pvh.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"background-color:rgb(56,58,89);")
        self.out_pvh.setObjectName("out_pvh")
        self.out_pvh_lbl = QtWidgets.QLabel(self.groupBox_6)
        self.out_pvh_lbl.setGeometry(QtCore.QRect(250, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.out_pvh_lbl.setFont(font)
        self.out_pvh_lbl.setStyleSheet(" \n"
"font: 11pt \"Constantia\";\n"
"color: white;")
        self.out_pvh_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.out_pvh_lbl.setObjectName("out_pvh_lbl")
        self.groupBox_7 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 170, 321, 141))
        self.groupBox_7.setObjectName("groupBox_7")
        self.in_pic = QtWidgets.QComboBox(self.groupBox_7)
        self.in_pic.setGeometry(QtCore.QRect(10, 30, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.in_pic.setFont(font)
        self.in_pic.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"background-color:rgb(56,58,89);")
        self.in_pic.setObjectName("in_pic")
        self.in_pic_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.in_pic_lbl.setGeometry(QtCore.QRect(250, 40, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.in_pic_lbl.setFont(font)
        self.in_pic_lbl.setStyleSheet(" \n"
"font: 11pt \"Constantia\";\n"
"color: white;\n"
"")
        self.in_pic_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.in_pic_lbl.setObjectName("in_pic_lbl")
        self.in_pvh = QtWidgets.QComboBox(self.groupBox_7)
        self.in_pvh.setGeometry(QtCore.QRect(10, 80, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.in_pvh.setFont(font)
        self.in_pvh.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"background-color:rgb(56,58,89);")
        self.in_pvh.setObjectName("in_pvh")
        self.in_pvh_lbl = QtWidgets.QLabel(self.groupBox_7)
        self.in_pvh_lbl.setGeometry(QtCore.QRect(250, 90, 61, 21))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.in_pvh_lbl.setFont(font)
        self.in_pvh_lbl.setStyleSheet(" \n"
"font: 11pt \"Constantia\";\n"
"color: white;")
        self.in_pvh_lbl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.in_pvh_lbl.setObjectName("in_pvh_lbl")
        self.groupBox_9 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_9.setGeometry(QtCore.QRect(370, 10, 411, 411))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_9.setFont(font)
        self.groupBox_9.setStyleSheet("QGroupBox  {\n"
"    font: 11pt \"Constantia\";\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"   color: white;\n"
"}")
        self.groupBox_9.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_9.setObjectName("groupBox_9")
        self.option_check_1 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_1.setGeometry(QtCore.QRect(20, 20, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_1.setFont(font)
        self.option_check_1.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"")
        self.option_check_1.setObjectName("option_check_1")
        self.option_check_2 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_2.setGeometry(QtCore.QRect(20, 50, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_2.setFont(font)
        self.option_check_2.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;")
        self.option_check_2.setObjectName("option_check_2")
        self.option_check_3 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_3.setGeometry(QtCore.QRect(20, 80, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_3.setFont(font)
        self.option_check_3.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;")
        self.option_check_3.setObjectName("option_check_3")
        self.option_check_4 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_4.setGeometry(QtCore.QRect(20, 110, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_4.setFont(font)
        self.option_check_4.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;")
        self.option_check_4.setObjectName("option_check_4")
        self.option_check_5 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_5.setGeometry(QtCore.QRect(20, 140, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_5.setFont(font)
        self.option_check_5.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"")
        self.option_check_5.setObjectName("option_check_5")
        self.option_check_6 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_6.setGeometry(QtCore.QRect(20, 170, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_6.setFont(font)
        self.option_check_6.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;")
        self.option_check_6.setObjectName("option_check_6")
        self.option_check_7 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_7.setGeometry(QtCore.QRect(20, 200, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_7.setFont(font)
        self.option_check_7.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"")
        self.option_check_7.setObjectName("option_check_7")
        self.option_check_8 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_8.setGeometry(QtCore.QRect(20, 230, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_8.setFont(font)
        self.option_check_8.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"")
        self.option_check_8.setObjectName("option_check_8")
        self.option_check_9 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_9.setGeometry(QtCore.QRect(20, 260, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_9.setFont(font)
        self.option_check_9.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"")
        self.option_check_9.setObjectName("option_check_9")
        self.option_check_10 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_10.setGeometry(QtCore.QRect(20, 290, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_10.setFont(font)
        self.option_check_10.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;")
        self.option_check_10.setObjectName("option_check_10")
        self.option_check_11 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_11.setGeometry(QtCore.QRect(20, 320, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_11.setFont(font)
        self.option_check_11.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"")
        self.option_check_11.setObjectName("option_check_11")
        self.option_check_12 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_12.setGeometry(QtCore.QRect(20, 350, 390, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_12.setFont(font)
        self.option_check_12.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;")
        self.option_check_12.setObjectName("option_check_12")
        self.option_check_13 = QtWidgets.QCheckBox(self.groupBox_9)
        self.option_check_13.setGeometry(QtCore.QRect(20, 380, 390, 21))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.option_check_13.setFont(font)
        self.option_check_13.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;")
        self.option_check_13.setObjectName("option_check_13")
        self.groupBox_10 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_10.setGeometry(QtCore.QRect(20, 190, 341, 70))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_10.setFont(font)
        self.groupBox_10.setStyleSheet("QGroupBox  {\n"
"    font: 11pt \"Constantia\";\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}")
        self.groupBox_10.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_10.setObjectName("groupBox_10")
        self.version_combo = QtWidgets.QComboBox(self.groupBox_10)
        self.version_combo.setGeometry(QtCore.QRect(10, 30, 321, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.version_combo.setFont(font)
        self.version_combo.setStyleSheet("font: 11pt \"Constantia\";\n"
"color: white;\n"
"background-color:rgb(56,58,89);")
        self.version_combo.setObjectName("version_combo")
        self.version_combo.addItem("")
        self.version_combo.setItemText(0, "")
        self.groupBox_2 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_2.setGeometry(QtCore.QRect(20, 610, 341, 130))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet("QGroupBox  {\n"
"    font: 11pt \"Constantia\";\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"}")
        self.groupBox_2.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_2.setObjectName("groupBox_2")
        self.width_inp = QtWidgets.QLineEdit(self.groupBox_2)
        self.width_inp.setGeometry(QtCore.QRect(10, 30, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.width_inp.setFont(font)
        self.width_inp.setStyleSheet("border-radius: 5px;\n"
"font: 11pt \"Constantia\";\n"
"color: black;")
        self.width_inp.setObjectName("width_inp")
        self.label = QtWidgets.QLabel(self.groupBox_2)
        self.label.setGeometry(QtCore.QRect(190, 40, 71, 21))
        self.label.setStyleSheet(" \n"
"font: 11pt \"Constantia\";\n"
"color: white;")
        self.label.setObjectName("label")
        self.height_inp = QtWidgets.QLineEdit(self.groupBox_2)
        self.height_inp.setGeometry(QtCore.QRect(10, 70, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.height_inp.setFont(font)
        self.height_inp.setStyleSheet("border-radius: 5px;\n"
"font: 11pt \"Constantia\";\n"
"color: black;")
        self.height_inp.setText("")
        self.height_inp.setObjectName("height_inp")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(190, 80, 91, 21))
        self.label_2.setStyleSheet(" \n"
"font: 11pt \"Constantia\";\n"
"color: white;\n"
"")
        self.label_2.setObjectName("label_2")
        self.groupBox_11 = QtWidgets.QGroupBox(self.frame)
        self.groupBox_11.setGeometry(QtCore.QRect(370, 430, 411, 411))
        font = QtGui.QFont()
        font.setFamily("Constantia")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.groupBox_11.setFont(font)
        self.groupBox_11.setStyleSheet("QGroupBox  {\n"
"    font: 14pt \"Constantia\";\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"   color: white;\n"
"}")
        self.groupBox_11.setTitle("")
        self.groupBox_11.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox_11.setObjectName("groupBox_11")
        self.text_info = QtWidgets.QTextEdit(self.groupBox_11)
        self.text_info.setGeometry(QtCore.QRect(10, 10, 391, 411))
        self.text_info.setStyleSheet(" \n"
"font: 11pt \"Constantia\";\n"
"color: black;\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.text_info.setObjectName("text_info")
        self.check_but = QtWidgets.QPushButton(self.frame)
        self.check_but.setGeometry(QtCore.QRect(20, 750, 131, 41))
        self.check_but.setStyleSheet("\n"
"    font: 14pt \"Constantia\";\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"")
        self.check_but.setObjectName("check_but")
        self.image_but = QtWidgets.QPushButton(self.frame)
        self.image_but.setGeometry(QtCore.QRect(20, 800, 131, 41))
        self.image_but.setStyleSheet("\n"
"    font: 14pt \"Constantia\";\n"
"    border: 1px solid gray;\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"")
        self.image_but.setObjectName("image_but")
        self.img_label = QtWidgets.QLabel(self.frame)
        self.img_label.setGeometry(QtCore.QRect(800, 90, 1091, 751))
        self.img_label.setText("")
        self.img_label.setObjectName("img_label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "Серия"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Модель"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Отделка"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Лицевая"))
        self.out_pic_lbl.setText(_translate("MainWindow", "Рисунок"))
        self.out_pvh_lbl.setText(_translate("MainWindow", "Цвет"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Внутренняя"))
        self.in_pic_lbl.setText(_translate("MainWindow", "Рисунок"))
        self.in_pvh_lbl.setText(_translate("MainWindow", "Цвет"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Опции"))
        self.option_check_1.setText(_translate("MainWindow", "Опция"))
        self.option_check_2.setText(_translate("MainWindow", "Опция"))
        self.option_check_3.setText(_translate("MainWindow", "Опция"))
        self.option_check_4.setText(_translate("MainWindow", "Опция"))
        self.option_check_5.setText(_translate("MainWindow", "Опция"))
        self.option_check_6.setText(_translate("MainWindow", "Опция"))
        self.option_check_7.setText(_translate("MainWindow", "Опция"))
        self.option_check_8.setText(_translate("MainWindow", "Опция"))
        self.option_check_9.setText(_translate("MainWindow", "Опция"))
        self.option_check_10.setText(_translate("MainWindow", "Опция"))
        self.option_check_11.setText(_translate("MainWindow", "Опция"))
        self.option_check_12.setText(_translate("MainWindow", "Опция"))
        self.option_check_13.setText(_translate("MainWindow", "Опция"))
        self.groupBox_10.setTitle(_translate("MainWindow", "Вариант исполнения"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Размеры"))
        self.label.setText(_translate("MainWindow", "Ширина"))
        self.label_2.setText(_translate("MainWindow", "Высота"))
        self.text_info.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Constantia\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p></body></html>"))
        self.check_but.setText(_translate("MainWindow", "Проверка"))
        self.image_but.setText(_translate("MainWindow", "Эскиз"))