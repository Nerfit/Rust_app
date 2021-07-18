# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\rustgui.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(672, 306)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setToolTipDuration(-1)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.nazwa_pliku_obiekt = QtWidgets.QLineEdit(self.tab)
        self.nazwa_pliku_obiekt.setStyleSheet("QLineEdit {\n"
"    border: 0.5px solid grey;\n"
"    border-radius: 3;\n"
"\n"
"}")
        self.nazwa_pliku_obiekt.setObjectName("nazwa_pliku_obiekt")
        self.gridLayout.addWidget(self.nazwa_pliku_obiekt, 0, 1, 1, 4)
        self.open_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.open_button.setFont(font)
        self.open_button.setStyleSheet("QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #a6a4a4);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #000000;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff,stop: 1 #c7c5c5);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 4;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.open_button.setObjectName("open_button")
        self.gridLayout.addWidget(self.open_button, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab)
        self.label_4.setMaximumSize(QtCore.QSize(152, 179))
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setLineWidth(2)
        self.label_4.setMidLineWidth(0)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Open/Icons/Ico.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 6, 6, 1)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.Button_getName = QtWidgets.QPushButton(self.tab)
        self.Button_getName.setMaximumSize(QtCore.QSize(60, 20))
        self.Button_getName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_getName.setStyleSheet("QPushButton {\n"
"background-color:rgb(255,255,255)\n"
"}")
        self.Button_getName.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Open/Icons/SampleName.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_getName.setIcon(icon)
        self.Button_getName.setIconSize(QtCore.QSize(50, 30))
        self.Button_getName.setAutoDefault(True)
        self.Button_getName.setFlat(True)
        self.Button_getName.setObjectName("Button_getName")
        self.gridLayout.addWidget(self.Button_getName, 1, 1, 1, 1)
        self.nazwa_probki_obiekt = QtWidgets.QLineEdit(self.tab)
        self.nazwa_probki_obiekt.setStyleSheet("QLineEdit {\n"
"    border: 0.5px solid grey;\n"
"    border-radius: 3;\n"
"\n"
"}")
        self.nazwa_probki_obiekt.setObjectName("nazwa_probki_obiekt")
        self.gridLayout.addWidget(self.nazwa_probki_obiekt, 1, 2, 1, 3)
        self.start_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #a6a4a4);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #000000;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff,stop: 1 #c7c5c5);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 4;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.start_button.setObjectName("start_button")
        self.gridLayout.addWidget(self.start_button, 2, 3, 1, 1)
        self.save_button = QtWidgets.QPushButton(self.tab)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("QPushButton:pressed\n"
"{\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff, stop: 1 #a6a4a4);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"    color: #000000;\n"
"    background-color: QLinearGradient( x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #ffffff,stop: 1 #c7c5c5);\n"
"    border-width: 1px;\n"
"    border-color: #1e1e1e;\n"
"    border-style: solid;\n"
"    border-radius: 4;\n"
"    padding: 3px;\n"
"    padding-left: 5px;\n"
"    padding-right: 5px;\n"
"}")
        self.save_button.setObjectName("save_button")
        self.gridLayout.addWidget(self.save_button, 2, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab)
        self.label_5.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)
        self.lcd_rust = QtWidgets.QLCDNumber(self.tab)
        self.lcd_rust.setMinimumSize(QtCore.QSize(25, 25))
        self.lcd_rust.setMaximumSize(QtCore.QSize(70, 27))
        self.lcd_rust.setStyleSheet("QLCDNumber {\n"
"    border: 1px solid grey;\n"
"border-radius: 3px;\n"
"color: black;\n"
"}")
        self.lcd_rust.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcd_rust.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_rust.setDigitCount(5)
        self.lcd_rust.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcd_rust.setObjectName("lcd_rust")
        self.gridLayout.addWidget(self.lcd_rust, 3, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab)
        self.label_6.setMaximumSize(QtCore.QSize(70, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 2, 1, 1)
        self.lcd_plate = QtWidgets.QLCDNumber(self.tab)
        self.lcd_plate.setMinimumSize(QtCore.QSize(25, 25))
        self.lcd_plate.setMaximumSize(QtCore.QSize(70, 27))
        self.lcd_plate.setStyleSheet("QLCDNumber {\n"
"    border: 1px solid grey;\n"
"border-radius: 3px;\n"
"color: black;\n"
"}")
        self.lcd_plate.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcd_plate.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_plate.setDigitCount(5)
        self.lcd_plate.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcd_plate.setObjectName("lcd_plate")
        self.gridLayout.addWidget(self.lcd_plate, 3, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.tab)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 3, 4, 1, 1)
        self.lcd_bg = QtWidgets.QLCDNumber(self.tab)
        self.lcd_bg.setMinimumSize(QtCore.QSize(25, 0))
        self.lcd_bg.setMaximumSize(QtCore.QSize(70, 27))
        self.lcd_bg.setStyleSheet("QLCDNumber {\n"
"    border: 1px solid grey;\n"
"border-radius: 3px;\n"
"color: black;\n"
"}")
        self.lcd_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lcd_bg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_bg.setDigitCount(5)
        self.lcd_bg.setSegmentStyle(QtWidgets.QLCDNumber.Filled)
        self.lcd_bg.setObjectName("lcd_bg")
        self.gridLayout.addWidget(self.lcd_bg, 3, 5, 1, 1)
        self.progressBar = QtWidgets.QProgressBar(self.tab)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar, 4, 0, 1, 6)
        self.checkBox_bg_mask = QtWidgets.QCommandLinkButton(self.tab)
        self.checkBox_bg_mask.setMaximumSize(QtCore.QSize(147, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.checkBox_bg_mask.setFont(font)
        self.checkBox_bg_mask.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.checkBox_bg_mask.setMouseTracking(False)
        self.checkBox_bg_mask.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.checkBox_bg_mask.setAcceptDrops(False)
        self.checkBox_bg_mask.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_bg_mask.setAutoFillBackground(False)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Open/Icons/mask.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.checkBox_bg_mask.setIcon(icon1)
        self.checkBox_bg_mask.setIconSize(QtCore.QSize(20, 20))
        self.checkBox_bg_mask.setCheckable(True)
        self.checkBox_bg_mask.setChecked(False)
        self.checkBox_bg_mask.setAutoDefault(True)
        self.checkBox_bg_mask.setObjectName("checkBox_bg_mask")
        self.gridLayout.addWidget(self.checkBox_bg_mask, 5, 0, 1, 2)
        self.bg_color_btn = QtWidgets.QCommandLinkButton(self.tab)
        self.bg_color_btn.setMaximumSize(QtCore.QSize(147, 35))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(12)
        self.bg_color_btn.setFont(font)
        self.bg_color_btn.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.bg_color_btn.setMouseTracking(False)
        self.bg_color_btn.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.bg_color_btn.setAcceptDrops(False)
        self.bg_color_btn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.bg_color_btn.setAutoFillBackground(False)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Open/Icons/bg_color.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bg_color_btn.setIcon(icon2)
        self.bg_color_btn.setIconSize(QtCore.QSize(25, 20))
        self.bg_color_btn.setCheckable(False)
        self.bg_color_btn.setChecked(False)
        self.bg_color_btn.setAutoDefault(True)
        self.bg_color_btn.setObjectName("bg_color_btn")
        self.gridLayout.addWidget(self.bg_color_btn, 5, 2, 1, 2)
        self.status = QtWidgets.QLabel(self.tab)
        self.status.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.gridLayout.addWidget(self.status, 6, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 6, 1, 1, 3)
        self.pushButton_info = QtWidgets.QPushButton(self.tab)
        self.pushButton_info.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_info.setStyleSheet("QPushButton {\n"
"background-color:rgb(255,255,255)\n"
"}")
        self.pushButton_info.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Open/Icons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_info.setIcon(icon3)
        self.pushButton_info.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_info.setFlat(True)
        self.pushButton_info.setObjectName("pushButton_info")
        self.gridLayout.addWidget(self.pushButton_info, 5, 4, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label_10 = QtWidgets.QLabel(self.tab_2)
        self.label_10.setGeometry(QtCore.QRect(200, 40, 16, 20))
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_10.setObjectName("label_10")
        self.spinBox_S = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_S.setGeometry(QtCore.QRect(140, 40, 45, 22))
        self.spinBox_S.setMaximum(255)
        self.spinBox_S.setProperty("value", 0)
        self.spinBox_S.setObjectName("spinBox_S")
        self.label_8 = QtWidgets.QLabel(self.tab_2)
        self.label_8.setGeometry(QtCore.QRect(20, 40, 16, 20))
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_8.setObjectName("label_8")
        self.spinBox_H = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_H.setGeometry(QtCore.QRect(40, 40, 45, 22))
        self.spinBox_H.setMinimum(-255)
        self.spinBox_H.setMaximum(255)
        self.spinBox_H.setProperty("value", -255)
        self.spinBox_H.setObjectName("spinBox_H")
        self.label_9 = QtWidgets.QLabel(self.tab_2)
        self.label_9.setGeometry(QtCore.QRect(120, 40, 16, 20))
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_9.setObjectName("label_9")
        self.spinBox_V = QtWidgets.QSpinBox(self.tab_2)
        self.spinBox_V.setGeometry(QtCore.QRect(220, 40, 45, 22))
        self.spinBox_V.setMaximum(255)
        self.spinBox_V.setProperty("value", 0)
        self.spinBox_V.setObjectName("spinBox_V")
        self.label_11 = QtWidgets.QLabel(self.tab_2)
        self.label_11.setGeometry(QtCore.QRect(20, 10, 241, 20))
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 20))
        self.label_11.setObjectName("label_11")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "File path (name)"))
        self.open_button.setText(_translate("MainWindow", "Open"))
        self.label_2.setText(_translate("MainWindow", "Sample name"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.save_button.setText(_translate("MainWindow", "Save Result"))
        self.label_5.setText(_translate("MainWindow", "Rust [%]:"))
        self.label_6.setText(_translate("MainWindow", "Plate [%]:"))
        self.label_7.setText(_translate("MainWindow", "B-ground [%]:"))
        self.checkBox_bg_mask.setText(_translate("MainWindow", "Bg Mask"))
        self.bg_color_btn.setText(_translate("MainWindow", "Bg Color"))
        self.status.setText(_translate("MainWindow", "..."))
        self.label_3.setText(_translate("MainWindow", "Press ESC to close."))
        self.pushButton_info.setToolTip(_translate("MainWindow", "HELP"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Rust Analysis"))
        self.label_10.setText(_translate("MainWindow", "V:"))
        self.label_8.setText(_translate("MainWindow", "H:"))
        self.label_9.setText(_translate("MainWindow", "S:"))
        self.label_11.setText(_translate("MainWindow", "Manual background color set:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Bg"))

import Zasoby_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

