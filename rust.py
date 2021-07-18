# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 11:39:50 2019

@author: Krzysztof Dziarmaga
@mail: krzysztof.dziarmaga@bwigroup.com
"""
from sys import argv, exit
from os import getcwd, path, makedirs
import numpy as np
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog
from PyQt5 import QtWidgets, QtCore
from rustgui import Ui_MainWindow
from help_t import Ui_Dialog
# ------------------second GUI with instructions-------------------
class help_text(QDialog):
    def __init__(self, parent = None):
        super(help_text,self).__init__(parent)
        self.help_ui = Ui_Dialog()
        self.help_ui.setupUi(self)
        # widget1 = help_text()
        # widget1.setWindowFlags(QtCore.Qt.WindowContextHelpButtonHint)

# ------------------------main GUI---------------------------------
class Wykrywanie_rdzy(QMainWindow):
    def __init__(self):
        super(Wykrywanie_rdzy,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Rust detection program')
        self.interface()

# ------------------After 'Start' clicked-----------------------
    def start(self):
        self.ui.start_button.setEnabled(False)
        global rdza_tmp
        global mask_new
        rdza_tmp = None
        mask = None
        def okno(event,x,y,flags,param):#creating a window with zoomed plate
            if event == cv2.EVENT_LBUTTONDOWN:
                #calculating coordinates of the window
                zoom_p = 50
                x1=x-zoom_p
                x2=x+zoom_p
                y1=y-zoom_p
                y2=y+zoom_p
                if x1<0:
                    x1 = 0
                    x2 = zoom_p * 2
                if x2 > self.w:
                    x1 = self.w - zoom_p * 2
                    x2 = self.w
                
                if y1<0:
                    y1 = 0
                    y2 = zoom_p * 2
                if y2 > self.h:
                    y2 = self.h
                    y1=self.h - zoom_p * 2
                
                global zoomed_img
                zoomed_img=self.plytka[y1:y2,x1:x2]
                cv2.namedWindow('zoom     **Double click to add a corrosion area**',cv2.WINDOW_NORMAL)
                cv2.createTrackbar('ColorRange','zoom     **Double click to add a corrosion area**',5,10, self.nothing)
                cv2.resizeWindow('zoom     **Double click to add a corrosion area**', 600,600)
                cv2.setMouseCallback('zoom     **Double click to add a corrosion area**',kolor)
                cv2.imshow('zoom     **Double click to add a corrosion area**',zoomed_img)
                cv2.waitKey(20)
                
        def okno2(event,x,y,flags,param):#creating a window with zoomed corrosion
            if event == cv2.EVENT_LBUTTONDOWN: 
                #calculating coordinates of the window     
                zoom_p2 = 50
                x1=x-zoom_p2
                x2=x+zoom_p2
                y1=y-zoom_p2
                y2=y+zoom_p2
                if x1<0:
                    x1 = 0
                    x2 = zoom_p2 * 2
                if x2 > self.w:
                    x1 = self.w - zoom_p2 * 2
                    x2 = self.w
                
                if y1<0:
                    y1 = 0
                    y2 = zoom_p2 * 2
                if y2 > self.h:
                    y2 = self.h
                    y1=self.h - zoom_p2 * 2
                    
                global zoomed_img2
                zoomed_img2=self.rdza[y1:y2,x1:x2]
                cv2.namedWindow('zoom     **Double click to remove a corrosion area**',cv2.WINDOW_NORMAL)
                cv2.createTrackbar('ColorRange','zoom     **Double click to remove a corrosion area**',5,10, self.nothing)
                cv2.resizeWindow('zoom     **Double click to remove a corrosion area**', 600,600)
                cv2.setMouseCallback('zoom     **Double click to remove a corrosion area**',kolor2)
                cv2.imshow('zoom     **Double click to remove a corrosion area**',zoomed_img2)
                cv2.waitKey(20)
                
        def kolor(event,x,y,flags,param): #adding some rust
            if event == cv2.EVENT_LBUTTONDBLCLK:
                b_maski,g_maski,r_maski=(zoomed_img[y,x])
                #temporary rust mask
                zakres = cv2.getTrackbarPos('ColorRange','zoom     **Double click to add a corrosion area**')
                lower_mask = np.array([b_maski-zakres,g_maski-zakres,r_maski-zakres])
                upper_mask = np.array([b_maski+zakres,g_maski+zakres,r_maski+zakres])
                rdza_tmp = cv2.inRange(self.bgr_img, lower_mask, upper_mask)
                rdza_tmp = cv2.dilate(rdza_tmp,np.ones((3,3), np.uint8),iterations = 1)
                self.mask_new = cv2.bitwise_or(rdza_tmp,mask)
                
        def kolor2(event,x,y,flags,param): #subtracting rust
            if event == cv2.EVENT_LBUTTONDBLCLK:
                b_maski,g_maski,r_maski=(zoomed_img2[y,x])
                zakres2 = cv2.getTrackbarPos('ColorRange','zoom     **Double click to remove a corrosion area**')
                #temporary rust mask
                lower_mask = np.array([b_maski-zakres2,g_maski-zakres2,r_maski-zakres2])
                upper_mask = np.array([b_maski+zakres2,g_maski+zakres2,r_maski+zakres2])
                rdza_tmp2 = cv2.inRange(self.bgr_img, lower_mask, upper_mask)
                rdza_tmp2 = cv2.dilate(rdza_tmp2,np.ones((3,3), np.uint8),iterations = 1)
                self.mask_new = cv2.subtract(mask, rdza_tmp2)

                
#        -------------------------------- GUI PART--------------------------
        self.ui.status.setText("Busy")
        self.nazwa_pliku=self.ui.nazwa_pliku_obiekt.text()
        
#-------------------Reading Image----------------------------------------------
        self.bgr_img = cv2.imread(self.nazwa_pliku,1)
        try:
            self.h, self.w = self.bgr_img.shape[:2]#dimensions
        except AttributeError:
            msg = QtWidgets.QMessageBox().warning(self, "Warning", "Type File Path and Sample Name correctly!")
            self.ui.status.setText("...")
            self.ui.progressBar.setValue(0)
            self.ui.start_button.setEnabled(True)
            return 0
        self.ui.progressBar.setValue(5)
        if self.h < self.w :        #Rotate image when in landscape mode
            self.bgr_img = cv2.rotate(self.bgr_img, cv2.ROTATE_90_CLOCKWISE)
            self.h, self.w = self.bgr_img.shape[:2]
            
        self.bgr_img = cv2.resize(self.bgr_img, (1000,1400))
        self.hsv_img = cv2.cvtColor(self.bgr_img, cv2.COLOR_BGR2HSV)
        b,g,r = cv2.split(self.bgr_img)#color arrays
        self.mask_new = None
#-------------------------------LET THE LOoOP BEGIN!-----------------------------------
        while True:
            self.nazwa_probki=self.ui.nazwa_probki_obiekt.text()
            lower_red = np.array([0,80,30])
            upper_red = np.array([20,255,180])
#-----------------------Rust Range--------------------------
            if mask is None:
                mask = cv2.inRange(self.hsv_img, lower_red, upper_red)  
                mask = cv2.dilate(mask, np.ones((3,3), np.uint8), iterations = 1)
                mask = cv2.erode(mask, np.ones((4,4), np.uint8), iterations = 1)
                mask = cv2.dilate(mask, np.ones((4,4), np.uint8), iterations = 1)
            if self.mask_new is not None:
                mask = self.mask_new
#            mask = cv2.erode(mask, np.ones((2,2), np.uint8), iterations = 1)    #<----------Rust mask
#-----------------------background range--------------------------
            h = self.ui.spinBox_H.value()
            s = self.ui.spinBox_S.value()
            v = self.ui.spinBox_V.value()
            if h == -255:
                l_czysciwo = np.array([80,9,0])        #earlier version: [80,6,0]__________________________________________________________
                u_czysciwo = np.array([120,255,255])
                mask_rev = cv2.inRange(self.hsv_img, l_czysciwo, u_czysciwo)
            else:
                l_czysciwo = np.array([h-10,s-150,v-150])
                u_czysciwo = np.array([h+4,s+150,v+150])
                mask_rev = cv2.inRange(self.hsv_img, l_czysciwo, u_czysciwo)
            
            kernel1 = np.ones((70,70),np.uint8)
            cv2.morphologyEx(mask_rev, cv2.MORPH_CLOSE, kernel1, iterations = 2)
            mask_cz = cv2.medianBlur(mask_rev, 15)      #<---------background mask
            mask_pr = cv2.bitwise_not(mask_cz)          #<---------plate + rust mask
            mask_rcz = cv2.bitwise_or(mask, mask_cz)    #plate + background mask
            mask_p = cv2.bitwise_not(mask_rcz)          #<----------maska płytki(dobra) (bez rdzy)
            mask_pcz = cv2.bitwise_or(mask_p, mask_cz)
#-----------------------------COLOR OF THE BACKGROUND MASK-----------------------
            self.bgr_img_cz = self.bgr_img.copy()
            self.bgr_img_cz[mask_cz > 0] = [255, 0,160]
            
#            ----------------Transparency of the background mask-----------------------
            overlay = self.bgr_img_cz.copy()
            output = self.bgr_img.copy()
            alpha = 0.4                 #<-------------0 is fully transparent, while 1 is fully opaque
            cv2.addWeighted(overlay, alpha, output, 1- alpha,0, output)
            
            if self.ui.checkBox_bg_mask.isChecked():
                self.rdza = cv2.bitwise_and(output,output, mask = mask_rcz)
                self.plytka = cv2.bitwise_and(output,output, mask = mask_pcz)
            else:
                self.rdza = cv2.bitwise_and(self.bgr_img,self.bgr_img, mask = mask_rcz)
                self.plytka = cv2.bitwise_and(self.bgr_img,self.bgr_img, mask = mask_pcz)
            if rdza_tmp is not None:
                self.plytka = cv2.bitwise_and(self.plytka,self.plytka, mask = mask)
            cv2.namedWindow('Plytka     (press ESC to close)',cv2.WINDOW_NORMAL)
#            -----------------------bardzo prymitywny warunek skalowania(ale działa)------------
            if self.h > 3300:
                rescale = 5                 #   <-------------------Image scale 1:5------------
            else:
                rescale = 4
            cv2.resizeWindow('Plytka     (press ESC to close)', int(self.w/rescale),int(self.h/rescale))
            cv2.namedWindow('Rdza     (press ESC to close)',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Rdza     (press ESC to close)', int(self.w/rescale),int(self.h/rescale))
            cv2.imshow('Plytka     (press ESC to close)', self.plytka)
            cv2.imshow('Rdza     (press ESC to close)', self.rdza)
            cv2.setMouseCallback('Plytka     (press ESC to close)',okno)
            cv2.setMouseCallback('Rdza     (press ESC to close)',okno2)
            
#------------------------Calculating quantity of pixels----------------------------
            self.H, self.W = self.bgr_img.shape[:2]         #<------------pixel after image processing
            self.n_pix=self.H*self.W            #pixel qty.
            self.n_plytka = np.sum(mask_pr == 255)
            self.n_rdza_pix = np.sum(mask == 255)
            self.rdza_percent = str(round((self.n_rdza_pix/self.n_plytka)*100,2))
            self.n_czysciwo = np.sum(mask_cz == 255)
            self.bg_percent = str(round((self.n_czysciwo/self.n_pix)*100, 2))
            self.plate_percent = str(round(100 - (self.n_czysciwo/self.n_pix)*100, 2))
            self.ui.lcd_rust.display(self.rdza_percent)
            self.ui.lcd_plate.display(self.plate_percent)
            self.ui.lcd_bg.display(self.bg_percent)

#-----------------------Closing the loop----------------------
            key = cv2.waitKey(1)
            if key == 27:
                cv2.destroyWindow('Plytka     (press ESC to close)')
                cv2.destroyWindow('Rdza     (press ESC to close)')
                cv2.destroyWindow('zoom     **Double click to add a corrosion area**')
                cv2.destroyWindow('zoom     **Double click to remove a corrosion area**')
                self.ui.start_button.setEnabled(True)
                break

    def filename(self):
        self.filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", None, "Image Files (*.jpg *.png)")
        self.ui.nazwa_pliku_obiekt.setText(self.filepath)
#------------------------------------------ZAPIS WYNIKÓW-------------------------
    def save(self):
        ##RESULT SAVING
        #-------------------making a new directory if it's not made yet-----------------
        cwd = path.dirname(self.ui.nazwa_pliku_obiekt.text()) + '/Results/'
        if path.exists(cwd):
            if path.isdir(cwd):
                pass
            else:
                makedirs(cwd, mode=0o777, exist_ok=False)
        else:
            makedirs(cwd, mode=0o777, exist_ok=False)
        #---------------------------graphic results + Error handling---------------------
        try:
            plikG1 = cwd + self.nazwa_probki + '_grafical_results1.jpg'
            plikG2 = cwd + self.nazwa_probki + '_grafical_results2.jpg'
            plikG3 = cwd + self.nazwa_probki + '_original.jpg'
            cv2.imwrite(plikG1,self.plytka)
            cv2.imwrite(plikG2,self.rdza)
            cv2.imwrite(plikG3,self.bgr_img)
        except AttributeError:
            msg = QtWidgets.QMessageBox().warning(self, "Warning", "Type File Path and Sample Name correctly!")
            self.ui.status.setText("...")
            self.ui.progressBar.setValue(0)
            return 0
        
        self.ui.progressBar.setValue(90)

        plikTXT = cwd + self.nazwa_probki + '_percentage_result.txt'
        self.ui.progressBar.setValue(98)
        wynik_txt = "Rust[%]: " + self.rdza_percent + '\n' + 'Plate[%]: ' + self.plate_percent + '\n' + 'Background[%]: ' + self.bg_percent
        plikTXT = open(cwd + self.nazwa_probki + '_percentage_result.txt', 'w')
        plikTXT.write("___________Results for " + self.nazwa_probki + "___________\n\n" + wynik_txt)
        plikTXT.close()
        self.ui.progressBar.setValue(100)
        self.ui.status.setText("Saved")
        
    def getName(self):
        self.ui.nazwa_probki_obiekt.setText(path.basename(self.ui.nazwa_pliku_obiekt.text())[:-4])
    def nothing(self, x):
        pass
    def okno_bg_color(self): 
        self.ui.bg_color_btn.setEnabled(False)
        self.nazwa_probki=self.ui.nazwa_probki_obiekt.text()
        self.nazwa_pliku=self.ui.nazwa_pliku_obiekt.text()
        self.bgr_img = cv2.imread(self.nazwa_pliku,1)
        try:
            self.h, self.w = self.bgr_img.shape[:2]#dimensions
        except AttributeError:
            msg = QtWidgets.QMessageBox().warning(self, "Warning", "Type File Path and Sample Name correctly!")
            self.ui.status.setText("...")
            self.ui.progressBar.setValue(0)
            self.ui.bg_color_btn.setEnabled(True)
            return 0
        self.ui.progressBar.setValue(5)
        if self.h < self.w :        #Rotate image when in landscape mode
            self.bgr_img = cv2.rotate(self.bgr_img, cv2.ROTATE_90_CLOCKWISE)
            self.h, self.w = self.bgr_img.shape[:2]
            
        self.bgr_img = cv2.resize(self.bgr_img, (1000,1400))
        self.hsv_img = cv2.cvtColor(self.bgr_img, cv2.COLOR_BGR2HSV)
        self.zoomed_img3 = self.hsv_img
        while True:
            cv2.namedWindow('DoubleClick to set the Background Color',cv2.WINDOW_NORMAL)
            cv2.createTrackbar('DoubleClick','Click to set the Background Color',5,10, self.nothing)
            cv2.resizeWindow('DoubleClick to set the Background Color', 500,600 )
            cv2.setMouseCallback('DoubleClick to set the Background Color',self.bg_color_change)
            cv2.imshow('DoubleClick to set the Background Color',self.zoomed_img3)
            key = cv2.waitKey(100)
            if key == 27 or cv2.getWindowProperty('DoubleClick to set the Background Color', 0) < 0:
                cv2.destroyWindow('DoubleClick to set the Background Color')
                self.ui.bg_color_btn.setEnabled(True)
                break

    def bg_color_change(self,event,x,y,flags,param): #subtracting rust
        if event == cv2.EVENT_LBUTTONDBLCLK:
            H_bg,S_bg,V_bg=(self.zoomed_img3[y,x])
#            zakres2 = cv2.getTrackbarPos('ColorRange','DoubleClick to set the Background Color')
            #temporary rust mask
            self.ui.spinBox_H.setValue(H_bg)
            self.ui.spinBox_S.setValue(S_bg)
            self.ui.spinBox_V.setValue(V_bg)
            msg = QtWidgets.QMessageBox().about(self, "Done", "Color Set Successfully!")
            
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
        
app = QApplication(argv)
app.setStyle('Fusion')
widget = Wykrywanie_rdzy()
widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
widget.show()
exit(app.exec_())