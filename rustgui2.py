# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rustgui2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(602, 267)
        Form.setMinimumSize(QtCore.QSize(602, 267))
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.frame_3 = QtWidgets.QFrame(Form)
        self.frame_3.setStyleSheet("QFrame {\n"
"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0, y2:1, stop:0 rgba(230, 239, 194, 255), stop:0.125 rgba(162, 213, 172, 255), stop:0.340909 rgba(58, 175, 169, 255), stop:0.568182 rgba(85, 124, 131, 255), stop:1 rgba(91, 81, 80, 255));\n"
"}")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(7, 7, 7, 4)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.frame_3)
        self.frame.setStyleSheet("QFrame {\n"
"background: transparent;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setMinimumSize(QtCore.QSize(140, 181))
        self.frame_6.setMaximumSize(QtCore.QSize(140, 181))
        self.frame_6.setStyleSheet("QFrame {\n"
"background: transparent;\n"
"}")
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setMaximumSize(QtCore.QSize(152, 179))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.label_4.setLineWidth(2)
        self.label_4.setMidLineWidth(0)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap(":/Open/Icons/Ico_transparentAGH.png"))
        self.label_4.setScaledContents(True)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_7.addWidget(self.label_4, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_5 = QtWidgets.QFrame(self.frame_4)
        self.frame_5.setStyleSheet("QPushButton {\n"
"border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 170);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(154, 154, 154, 100);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(140, 140, 140, 100);\n"
"border: 1px solid  rgba(140, 140, 140, 200);\n"
"}")
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_analyze_page = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_analyze_page.setMinimumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.pushButton_analyze_page.setFont(font)
        self.pushButton_analyze_page.setObjectName("pushButton_analyze_page")
        self.verticalLayout_6.addWidget(self.pushButton_analyze_page)
        self.pushButton_set_col_page = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_set_col_page.setMinimumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.pushButton_set_col_page.setFont(font)
        self.pushButton_set_col_page.setObjectName("pushButton_set_col_page")
        self.verticalLayout_6.addWidget(self.pushButton_set_col_page)
        self.verticalLayout_4.addWidget(self.frame_5, 0, QtCore.Qt.AlignVCenter)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignLeft)
        self.frame_2 = QtWidgets.QFrame(self.frame_3)
        self.frame_2.setStyleSheet("QFrame {\n"
"background: transparent;\n"
"}")
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_2)
        self.stackedWidget.setStyleSheet("QFrame {\n"
"background: rgba(255, 255, 255, 100);\n"
"border-radius: 15px;\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_analyze = QtWidgets.QWidget()
        self.page_analyze.setStyleSheet("QWidget{\n"
"background: transparent;\n"
"}")
        self.page_analyze.setObjectName("page_analyze")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.page_analyze)
        self.verticalLayout_10.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.frame_btn_style = QtWidgets.QFrame(self.page_analyze)
        self.frame_btn_style.setStyleSheet("QCommandLinkButton {\n"
"border-radius: 10px;\n"
"background-color: rgba(255, 255, 255, 150);\n"
"}\n"
"QCommandLinkButton:hover {\n"
"background-color: rgba(154, 154, 154, 100);\n"
"}\n"
"QCommandLinkButton:checked {\n"
"background-color: rgba(140, 140, 140, 100);\n"
"border: 1px solid  rgba(140, 140, 140, 200);\n"
"}\n"
"QPushButton {\n"
"border-radius: 5px;\n"
"background-color: rgba(255, 255, 255, 170);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(154, 154, 154, 100);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(140, 140, 140, 100);\n"
"border: 1px solid  rgba(140, 140, 140, 200);\n"
"}")
        self.frame_btn_style.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_btn_style.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btn_style.setObjectName("frame_btn_style")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.frame_btn_style)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(10)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_10 = QtWidgets.QFrame(self.frame_btn_style)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_10)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(5)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.frame_8 = QtWidgets.QFrame(self.frame_10)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.frame_8)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setSpacing(5)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame_18 = QtWidgets.QFrame(self.frame_8)
        self.frame_18.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_18.setObjectName("frame_18")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_18)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.frame_18)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.nazwa_pliku_obiekt = QtWidgets.QLineEdit(self.frame_18)
        self.nazwa_pliku_obiekt.setStyleSheet("QLineEdit {\n"
"    border: 0.5px solid grey;\n"
"    border-radius: 3;\n"
"\n"
"}")
        self.nazwa_pliku_obiekt.setObjectName("nazwa_pliku_obiekt")
        self.horizontalLayout_4.addWidget(self.nazwa_pliku_obiekt)
        self.verticalLayout_12.addWidget(self.frame_18)
        self.frame_17 = QtWidgets.QFrame(self.frame_8)
        self.frame_17.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_17.setObjectName("frame_17")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_17)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.frame_17)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.Button_getName = QtWidgets.QPushButton(self.frame_17)
        self.Button_getName.setMaximumSize(QtCore.QSize(60, 20))
        self.Button_getName.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.Button_getName.setStyleSheet("")
        self.Button_getName.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Open/Icons/SampleName.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Button_getName.setIcon(icon)
        self.Button_getName.setIconSize(QtCore.QSize(50, 30))
        self.Button_getName.setAutoDefault(True)
        self.Button_getName.setFlat(True)
        self.Button_getName.setObjectName("Button_getName")
        self.horizontalLayout_3.addWidget(self.Button_getName)
        self.nazwa_probki_obiekt = QtWidgets.QLineEdit(self.frame_17)
        self.nazwa_probki_obiekt.setStyleSheet("QLineEdit {\n"
"    border: 0.5px solid grey;\n"
"    border-radius: 3;\n"
"\n"
"}")
        self.nazwa_probki_obiekt.setObjectName("nazwa_probki_obiekt")
        self.horizontalLayout_3.addWidget(self.nazwa_probki_obiekt)
        self.verticalLayout_12.addWidget(self.frame_17)
        self.frame_16 = QtWidgets.QFrame(self.frame_8)
        self.frame_16.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_16.setObjectName("frame_16")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_16)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.start_button = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.start_button.sizePolicy().hasHeightForWidth())
        self.start_button.setSizePolicy(sizePolicy)
        self.start_button.setMinimumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.start_button.setFont(font)
        self.start_button.setStyleSheet("")
        self.start_button.setObjectName("start_button")
        self.horizontalLayout_2.addWidget(self.start_button)
        self.save_button = QtWidgets.QPushButton(self.frame_16)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.save_button.sizePolicy().hasHeightForWidth())
        self.save_button.setSizePolicy(sizePolicy)
        self.save_button.setMinimumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("")
        self.save_button.setObjectName("save_button")
        self.horizontalLayout_2.addWidget(self.save_button)
        self.verticalLayout_12.addWidget(self.frame_16, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_5.addWidget(self.frame_8)
        self.frame_9 = QtWidgets.QFrame(self.frame_10)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.open_button = QtWidgets.QPushButton(self.frame_9)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy)
        self.open_button.setMinimumSize(QtCore.QSize(75, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(9)
        self.open_button.setFont(font)
        self.open_button.setStyleSheet("")
        self.open_button.setObjectName("open_button")
        self.horizontalLayout_10.addWidget(self.open_button, 0, QtCore.Qt.AlignTop)
        self.horizontalLayout_5.addWidget(self.frame_9)
        self.verticalLayout_9.addWidget(self.frame_10)
        self.frame_11 = QtWidgets.QFrame(self.frame_btn_style)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_13.setSpacing(10)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.frame_lcd_style = QtWidgets.QFrame(self.frame_11)
        self.frame_lcd_style.setStyleSheet("QLCDNumber {\n"
"    border: 1px solid grey;\n"
"border-radius: 3px;\n"
"color: black;\n"
"}")
        self.frame_lcd_style.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_lcd_style.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_lcd_style.setObjectName("frame_lcd_style")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_lcd_style)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(5)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.label_5 = QtWidgets.QLabel(self.frame_lcd_style)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setTextFormat(QtCore.Qt.PlainText)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_9.addWidget(self.label_5)
        self.lcd_rust = QtWidgets.QLCDNumber(self.frame_lcd_style)
        self.lcd_rust.setMinimumSize(QtCore.QSize(70, 27))
        self.lcd_rust.setMaximumSize(QtCore.QSize(70, 27))
        self.lcd_rust.setStyleSheet("")
        self.lcd_rust.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_rust.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lcd_rust.setDigitCount(5)
        self.lcd_rust.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_rust.setObjectName("lcd_rust")
        self.horizontalLayout_9.addWidget(self.lcd_rust)
        self.label_6 = QtWidgets.QLabel(self.frame_lcd_style)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setTextFormat(QtCore.Qt.PlainText)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_9.addWidget(self.label_6)
        self.lcd_plate = QtWidgets.QLCDNumber(self.frame_lcd_style)
        self.lcd_plate.setMinimumSize(QtCore.QSize(70, 27))
        self.lcd_plate.setMaximumSize(QtCore.QSize(70, 27))
        self.lcd_plate.setStyleSheet("")
        self.lcd_plate.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_plate.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_plate.setDigitCount(5)
        self.lcd_plate.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_plate.setObjectName("lcd_plate")
        self.horizontalLayout_9.addWidget(self.lcd_plate)
        self.label_7 = QtWidgets.QLabel(self.frame_lcd_style)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setTextFormat(QtCore.Qt.PlainText)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_9.addWidget(self.label_7)
        self.lcd_bg = QtWidgets.QLCDNumber(self.frame_lcd_style)
        self.lcd_bg.setMinimumSize(QtCore.QSize(70, 27))
        self.lcd_bg.setMaximumSize(QtCore.QSize(70, 27))
        self.lcd_bg.setStyleSheet("")
        self.lcd_bg.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcd_bg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcd_bg.setDigitCount(5)
        self.lcd_bg.setSegmentStyle(QtWidgets.QLCDNumber.Flat)
        self.lcd_bg.setObjectName("lcd_bg")
        self.horizontalLayout_9.addWidget(self.lcd_bg)
        self.verticalLayout_13.addWidget(self.frame_lcd_style)
        self.frame_13 = QtWidgets.QFrame(self.frame_11)
        self.frame_13.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_13.setObjectName("frame_13")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_13)
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.progressBar = QtWidgets.QProgressBar(self.frame_13)
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.progressBar.setFont(font)
        self.progressBar.setStyleSheet("QProgressBar {\n"
"background-color: rgba(87, 109, 113, 150);\n"
"color: #ffffff;\n"
"border-radius: 7px;\n"
"text-align: center; \n"
"}\n"
"QProgressBar::chunk {\n"
"background-color: #10255b;\n"
"border-radius: 7px;\n"
" }")
        self.progressBar.setMinimum(0)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setTextVisible(True)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout_8.addWidget(self.progressBar)
        self.verticalLayout_13.addWidget(self.frame_13)
        self.frame_14 = QtWidgets.QFrame(self.frame_11)
        self.frame_14.setStyleSheet("")
        self.frame_14.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_14.setObjectName("frame_14")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_14)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(5)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.checkBox_bg_mask = QtWidgets.QCommandLinkButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.checkBox_bg_mask.sizePolicy().hasHeightForWidth())
        self.checkBox_bg_mask.setSizePolicy(sizePolicy)
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
        self.horizontalLayout_7.addWidget(self.checkBox_bg_mask, 0, QtCore.Qt.AlignVCenter)
        self.bg_color_btn = QtWidgets.QCommandLinkButton(self.frame_14)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg_color_btn.sizePolicy().hasHeightForWidth())
        self.bg_color_btn.setSizePolicy(sizePolicy)
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
        self.horizontalLayout_7.addWidget(self.bg_color_btn, 0, QtCore.Qt.AlignVCenter)
        spacerItem = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.pushButton_info = QtWidgets.QPushButton(self.frame_14)
        self.pushButton_info.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.pushButton_info.setStyleSheet("")
        self.pushButton_info.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Open/Icons/info.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_info.setIcon(icon3)
        self.pushButton_info.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_info.setFlat(True)
        self.pushButton_info.setObjectName("pushButton_info")
        self.horizontalLayout_7.addWidget(self.pushButton_info)
        self.verticalLayout_13.addWidget(self.frame_14)
        self.frame_15 = QtWidgets.QFrame(self.frame_11)
        self.frame_15.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_15.setObjectName("frame_15")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_15)
        self.horizontalLayout_6.setContentsMargins(5, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(10)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.status = QtWidgets.QLabel(self.frame_15)
        self.status.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(8)
        font.setBold(False)
        font.setWeight(50)
        self.status.setFont(font)
        self.status.setObjectName("status")
        self.horizontalLayout_6.addWidget(self.status)
        spacerItem1 = QtWidgets.QSpacerItem(120, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.label_3 = QtWidgets.QLabel(self.frame_15)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_6.addWidget(self.label_3)
        self.verticalLayout_13.addWidget(self.frame_15, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_9.addWidget(self.frame_11)
        self.verticalLayout_10.addWidget(self.frame_btn_style)
        self.stackedWidget.addWidget(self.page_analyze)
        self.page_set_col = QtWidgets.QWidget()
        self.page_set_col.setStyleSheet("QWidget{\n"
"background: transparent;\n"
"}")
        self.page_set_col.setObjectName("page_set_col")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.page_set_col)
        self.verticalLayout_14.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.frame_19 = QtWidgets.QFrame(self.page_set_col)
        self.frame_19.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_19.setObjectName("frame_19")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_19)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(10)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.frame_20 = QtWidgets.QFrame(self.frame_19)
        self.frame_20.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_20.setObjectName("frame_20")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.frame_20)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_11 = QtWidgets.QLabel(self.frame_20)
        self.label_11.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_12.addWidget(self.label_11)
        self.verticalLayout_11.addWidget(self.frame_20)
        self.frame_21 = QtWidgets.QFrame(self.frame_19)
        self.frame_21.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_21.setObjectName("frame_21")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.frame_21)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(5)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_9 = QtWidgets.QLabel(self.frame_21)
        self.label_9.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_13.addWidget(self.label_9)
        self.spinBox_H = QtWidgets.QSpinBox(self.frame_21)
        self.spinBox_H.setMinimum(-255)
        self.spinBox_H.setMaximum(255)
        self.spinBox_H.setProperty("value", -255)
        self.spinBox_H.setObjectName("spinBox_H")
        self.horizontalLayout_13.addWidget(self.spinBox_H)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.label_10 = QtWidgets.QLabel(self.frame_21)
        self.label_10.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_13.addWidget(self.label_10)
        self.spinBox_S = QtWidgets.QSpinBox(self.frame_21)
        self.spinBox_S.setMaximum(255)
        self.spinBox_S.setProperty("value", 0)
        self.spinBox_S.setObjectName("spinBox_S")
        self.horizontalLayout_13.addWidget(self.spinBox_S)
        spacerItem3 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem3)
        self.label_12 = QtWidgets.QLabel(self.frame_21)
        self.label_12.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.spinBox_V = QtWidgets.QSpinBox(self.frame_21)
        self.spinBox_V.setMaximum(255)
        self.spinBox_V.setProperty("value", 0)
        self.spinBox_V.setObjectName("spinBox_V")
        self.horizontalLayout_13.addWidget(self.spinBox_V)
        self.verticalLayout_11.addWidget(self.frame_21)
        self.verticalLayout_14.addWidget(self.frame_19, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.stackedWidget.addWidget(self.page_set_col)
        self.verticalLayout_2.addWidget(self.stackedWidget)
        self.frame_7 = QtWidgets.QFrame(self.frame_2)
        self.frame_7.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_11.setContentsMargins(0, 2, 0, 0)
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_8 = QtWidgets.QLabel(self.frame_7)
        self.label_8.setMaximumSize(QtCore.QSize(16777215, 20))
        font = QtGui.QFont()
        font.setFamily("Century Gothic")
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("QLabel {\n"
"color: #ffffff\n"
"}")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_11.addWidget(self.label_8)
        self.verticalLayout_2.addWidget(self.frame_7, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_8.addWidget(self.frame_3)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_analyze_page.setText(_translate("Form", "Analiza płytek"))
        self.pushButton_set_col_page.setText(_translate("Form", "Ustaw kolor ręcznie"))
        self.label.setText(_translate("Form", "File path (name)"))
        self.label_2.setText(_translate("Form", "Sample name"))
        self.start_button.setText(_translate("Form", "Start"))
        self.save_button.setText(_translate("Form", "Zapisz wynik"))
        self.open_button.setText(_translate("Form", "Otwórz"))
        self.label_5.setText(_translate("Form", "Korozja [%]:"))
        self.label_6.setText(_translate("Form", "Płytka [%]:"))
        self.label_7.setText(_translate("Form", "Tło [%]:"))
        self.checkBox_bg_mask.setText(_translate("Form", "Maska tła"))
        self.bg_color_btn.setText(_translate("Form", "Kolor tła"))
        self.pushButton_info.setToolTip(_translate("Form", "HELP"))
        self.status.setText(_translate("Form", "..."))
        self.label_3.setText(_translate("Form", "Naciśnij ESC żeby przerwać"))
        self.label_11.setText(_translate("Form", "Manualny wybór koloru tła"))
        self.label_9.setText(_translate("Form", "H:"))
        self.label_10.setText(_translate("Form", "S:"))
        self.label_12.setText(_translate("Form", "V:"))
        self.label_8.setText(_translate("Form", "© K. Dziarmaga 2021"))
import Zasoby_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
