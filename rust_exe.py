# -*- coding: utf-8 -*-
"""
Created on Sat Aug 15 09:24:57 2020

@author: Krzysztof Dziarmaga
@mail: dziarmag@student.agh.edu.pl
"""
from sys import argv, exit
from os import getcwd, path, makedirs
from numpy import array, ones, uint8, sum
import cv2, os
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QWidget
from PyQt5 import QtWidgets, QtCore
from rustgui2 import Ui_Form
from help_t import Ui_Dialog
from CollectImages import Collect_Images
from FilterImages import Filter_Images
from PyQt5.QtCore import (pyqtSlot, pyqtSignal)
# Converting files commands
# pyuic5 -x -o rustgui2.py rustgui2.ui
# pyrcc5 -o Zasoby_rc.py Zasoby.qrc
# ------------------second GUI with instructions-------------------
class help_text(QDialog):
    def __init__(self, parent = None):
        super(help_text,self).__init__(parent)
        self.help_ui = Ui_Dialog()
        self.help_ui.setupUi(self)

# ------------------------main GUI---------------------------------
class Wykrywanie_rdzy(QWidget):
    def __init__(self):
        super(Wykrywanie_rdzy,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('Rust detection program')
        self.interface()

# ------------------After 'Start' clicked-----------------------
    def start(self):
        self.change_behaviour('collect_images')
        self.ui.start_button.setEnabled(False)


            
    def help_txt(self):
        help_text(self).show()
#------------------Connecting buttons from GUI with corresponding functions-----------------
    def interface(self):
        self.ui.start_button.clicked.connect(self.start)
        self.ui.save_button.clicked.connect(self.save)
        self.ui.open_button.clicked.connect(self.filename)
        self.ui.Button_getName.clicked.connect(self.getName)
        self.ui.bg_color_btn.clicked.connect(self.okno_bg_color)
        self.ui.pushButton_info.clicked.connect(self.help_txt)
        self.ui.pushButton_analyze_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_analyze))
        self.ui.pushButton_set_col_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_set_col))

    def change_behaviour(self, next_behaviour):
        """
        It takes a string value and assigned it to self.behaviour.
        :param next_behaviour: String value that should ba assigned to 'behaviour' attribute
        :return:
        """
        self.clean_gui()
        self.behaviour = next_behaviour
        self.threadclass.start()

class ThreadClass(QtCore.QThread):
    def __init__(self, parent=Wykrywanie_rdzy):
        super(ThreadClass, self).__init__(None)

    change_state = pyqtSignal(int)
    signal_dialog = pyqtSignal(str)
    signal_progress = pyqtSignal(int, int)
    signal_dir_name_popup = pyqtSignal()
    signal_files_uploaded_popup = pyqtSignal()

    @pyqtSlot()
    def run(self):
        if 'widget' in globals():
            if window.behaviour == 'collect_images':
                collector.start_collecting()
                path = filtr.filtruj()
                window.behaviour = None
            elif window.behaviour == 'local_structure':
                cb_doc.get_local_structure()
                window.behaviour = None


    def show_dialog(self, file_name=''):
        self.signal_dialog.emit(file_name)

    def stop(self):
        self.terminate()
        cb_doc.set_stopped()


if __name__ == "__main__":
    app = QApplication(argv)
    widget = Wykrywanie_rdzy()
    widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    path = os.path.abspath(os.getcwd()) + '\Zdj\\'
    collector = Collect_Images(GUI=widget, path=path)
    filtr = Filter_Images(GUI=widget, path=path)
    widget.show()
    exit(app.exec_())