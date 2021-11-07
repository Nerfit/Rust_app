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
# Converting files commands
# pyuic5 -x -o rustgui2.py rustgui2.ui
# pyrcc5 -o Zasoby_rc.py Zasoby.qrc
# ------------------second GUI with instructions-------------------
class help_text(QDialog):
    def __init__(self, parent = None):
        """
        Function used to display Help Dialog
        """
        super(help_text,self).__init__(parent)
        self.help_ui = Ui_Dialog()
        self.help_ui.setupUi(self)

# ------------------------main GUI---------------------------------
class Wykrywanie_rdzy(QWidget):
    def __init__(self):
        super(Wykrywanie_rdzy,self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle('System wizyjny do analizy korozjina płytkach referencyjnych')
        self.interface()

    def get_images(self):
        """
        Function calling collector and then filter objects
        """
        if not self.ui.nazwa_probki_obiekt.text():
            msg = QtWidgets.QMessageBox().warning(self, "Warning", "Wpisz nazwę próbki!")
        else:
            self.ui.start_button.setEnabled(False)
            collector.start_collecting()
            self.ui.status.setText('Obrazy przechwycone. Zaczynam filtrację ...')
            images_path = filtr.filtruj()
            self.ui.nazwa_pliku_obiekt.setText(images_path)
            self.ui.nazwa_pliku_obiekt.setEnabled(False)
            self.ui.start_button.setEnabled(True)

    def start(self):
        """
        Function that is being executed after the start button is pressed.
        """
        global rdza_tmp
        global mask_new
        rdza_tmp = None
        mask_k = None
        def okno(event,x,y, flags, param):
            """
            Creating a window with zoomed plate
            :param event: Event triggered e.g. mouse click
            :param x: x coordinate
            :param y: y coordinate
            :param flags:
            :param param:
            :return:
            """
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
                cv2.namedWindow('zoom     **Podwojny przycisk myszy dodaje korozje**',cv2.WINDOW_NORMAL)
                cv2.createTrackbar('ColorRange','zoom     **Podwojny przycisk myszy dodaje korozje**',5,10, self.nothing)
                cv2.resizeWindow('zoom     **Podwojny przycisk myszy dodaje korozje**', 600,600)
                cv2.setMouseCallback('zoom     **Podwojny przycisk myszy dodaje korozje**',kolor)
                cv2.imshow('zoom     **Podwojny przycisk myszy dodaje korozje**',zoomed_img)
                cv2.waitKey(20)

        def okno2(event,x,y, flags, param):
            """
            Creating a window with zoomed corrosion area
            :param event: Event triggered e.g. mouse click
            :param x: x coordinate
            :param y: y coordinate
            :param flags:
            :param param:
            :return:
            """
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
                cv2.namedWindow('zoom     **Podwojny przycisk myszy odejmuje korozje**',cv2.WINDOW_NORMAL)
                cv2.createTrackbar('ColorRange','zoom     **Podwojny przycisk myszy odejmuje korozje**',5,10, self.nothing)
                cv2.resizeWindow('zoom     **Podwojny przycisk myszy odejmuje korozje**', 600,600)
                cv2.setMouseCallback('zoom     **Podwojny przycisk myszy odejmuje korozje**',kolor2)
                cv2.imshow('zoom     **Podwojny przycisk myszy odejmuje korozje**',zoomed_img2)
                cv2.waitKey(20)

        def kolor(event,x,y, flags, param):
            """
            Function responsible for adding some rust
            :param event: Event triggered e.g. mouse click
            :param x: x coordinate
            :param y: y coordinate
            """
            if event == cv2.EVENT_LBUTTONDBLCLK:
                b_maski,g_maski,r_maski=(zoomed_img[y,x])
                #temporary rust mask
                zakres = cv2.getTrackbarPos('ColorRange','zoom     **Podwojny przycisk myszy dodaje korozje**')
                lower_mask = array([b_maski-zakres,g_maski-zakres,r_maski-zakres])
                upper_mask = array([b_maski+zakres,g_maski+zakres,r_maski+zakres])
                rdza_tmp = cv2.inRange(self.bgr_img, lower_mask, upper_mask)
                rdza_tmp = cv2.dilate(rdza_tmp,ones((3,3), uint8),iterations = 1)
                self.mask_new = cv2.bitwise_or(rdza_tmp,mask_k)

        def kolor2(event,x,y, flags, param):
            """
            Function responsible for subtracting rust
            :param event: Event triggered e.g. mouse click
            :param x: x coordinate
            :param y: y coordinate
            :return:
            """
            if event == cv2.EVENT_LBUTTONDBLCLK:
                b_maski,g_maski,r_maski=(zoomed_img2[y,x])
                zakres2 = cv2.getTrackbarPos('ColorRange','zoom     **Podwojny przycisk myszy odejmuje korozje**')
                #temporary rust mask
                lower_mask = array([b_maski-zakres2,g_maski-zakres2,r_maski-zakres2])
                upper_mask = array([b_maski+zakres2,g_maski+zakres2,r_maski+zakres2])
                rdza_tmp2 = cv2.inRange(self.bgr_img, lower_mask, upper_mask)
                rdza_tmp2 = cv2.dilate(rdza_tmp2,ones((3,3), uint8),iterations = 1)
                self.mask_new = cv2.subtract(mask_k, rdza_tmp2)

        # GUI
        self.ui.status.setText("Busy")
        self.nazwa_pliku=self.ui.nazwa_pliku_obiekt.text()

        # Reading Image
        self.bgr_img = cv2.imread(self.nazwa_pliku,1)
        try:
            self.h, self.w = self.bgr_img.shape[:2] #image dimensions
        except AttributeError:
            msg = QtWidgets.QMessageBox().warning(self, "Warning", "Nejpierw pobierz obraz z serwera!")
            self.ui.status.setText("...")
            self.ui.progressBar.setValue(0)
            self.ui.start_button.setEnabled(True)
            return 0
        self.ui.progressBar.setValue(5)
        if self.h < self.w :        #Rotate image when in landscape mode
            self.bgr_img = cv2.rotate(self.bgr_img, cv2.ROTATE_90_CLOCKWISE)
            self.h, self.w = self.bgr_img.shape[:2]

        self.bgr_img = cv2.resize(self.bgr_img, (1200,1600))
        self.hsv_img = cv2.cvtColor(self.bgr_img, cv2.COLOR_BGR2HSV)
        b,g,r = cv2.split(self.bgr_img)#color arrays
        self.mask_new = None
        # Here the main loop starts where calculations are being done
        while True:
            self.nazwa_probki=self.ui.nazwa_probki_obiekt.text()
            lower_red = array([0,80,30])
            upper_red = array([40,255,180])
            # upper_red = array([20,255,180])
            # Rust Range
            if mask_k is None:
                mask_k = cv2.inRange(self.hsv_img, lower_red, upper_red)
                mask_k = cv2.dilate(mask_k, ones((3,3), uint8), iterations = 1)
                mask_k = cv2.erode(mask_k, ones((4,4), uint8), iterations = 1)
                mask_k = cv2.dilate(mask_k, ones((4,4), uint8), iterations = 1)
            if self.mask_new is not None:
                mask_k = self.mask_new
            # Background range
            h = self.ui.spinBox_H.value()
            s = self.ui.spinBox_S.value()
            v = self.ui.spinBox_V.value()
            if h == -255:
                # l_czysciwo = array([80, 9, 0])  # previous variant: [80,6,0]
                # u_czysciwo = array([120, 255, 255])
                l_czysciwo = array([107, 147, 0])  # previous variant: [80,6,0]
                u_czysciwo = array([137, 255, 255])
                mask_rev = cv2.inRange(self.hsv_img, l_czysciwo, u_czysciwo)
            else:
                # Setting the background range basing on selected HSV color
                l_czysciwo = array([h-15,s-50,v-150])
                u_czysciwo = array([h+15,s+100,v+150])
                # l_czysciwo = array([h-20,s-100,v-150])
                # u_czysciwo = array([h+20,s+100,v+150])
                mask_rev = cv2.inRange(self.hsv_img, l_czysciwo, u_czysciwo)    # Black plate only
            kernel1 = ones((70,70),uint8)
            # cv2.namedWindow('TEST',cv2.WINDOW_NORMAL)
            cv2.morphologyEx(mask_rev, cv2.MORPH_CLOSE, kernel1, iterations = 2)
            mask_t = cv2.medianBlur(mask_rev, 15)      #<---------background (white)
            mask_pr = cv2.bitwise_not(mask_t)          #<---------plate, rust (white)
            mask_rcz = cv2.bitwise_or(mask_k, mask_t)    #rust + background mask (white), plate black
            mask_p = cv2.bitwise_not(mask_rcz)          #<----------maska: płytka(biała) (bez rdzy i tła: czarne)
            mask_pcz = cv2.bitwise_or(mask_p, mask_t)  #<----------tylko rdza czarna
            # cv2.imshow('TEST', mask_k)

            # COLOR OF THE BACKGROUND MASK
            self.bgr_img_cz = self.bgr_img.copy()
            self.bgr_img_cz[mask_t > 0] = [216, 20, 255]

#            ----------------Transparency of the background mask-----------------------
            overlay = self.bgr_img_cz.copy()
            output = self.bgr_img.copy()
            alpha = 0.25                 #<-------------0 is fully transparent, while 1 is fully opaque
            cv2.addWeighted(overlay, alpha, output, 1 - alpha,0, output)

            if self.ui.checkBox_bg_mask.isChecked():
                self.rdza = cv2.bitwise_and(output,output, mask = mask_rcz)
                self.plytka = cv2.bitwise_and(output,output, mask = mask_pcz)
            else:
                self.rdza = cv2.bitwise_and(self.bgr_img,self.bgr_img, mask = mask_rcz)
                self.plytka = cv2.bitwise_and(self.bgr_img,self.bgr_img, mask = mask_pcz)
            if rdza_tmp is not None:
                self.plytka = cv2.bitwise_and(self.plytka,self.plytka, mask = mask_k)
            cv2.namedWindow('Plytka     (Wcisnij ESC zeby zamknac)',cv2.WINDOW_NORMAL)
            # skalowanie okna
            if self.h > 3300:
                rescale = 5         # Frame scale 1:5
            else:
                rescale = 2         # Frame scale 1:2
            cv2.resizeWindow('Plytka     (Wcisnij ESC zeby zamknac)', int(self.w/rescale),int(self.h/rescale))
            cv2.namedWindow('Korozja     (Wcisnij ESC zeby zamknac)',cv2.WINDOW_NORMAL)
            cv2.resizeWindow('Korozja     (Wcisnij ESC zeby zamknac)', int(self.w/rescale),int(self.h/rescale))
            cv2.imshow('Plytka     (Wcisnij ESC zeby zamknac)', self.plytka)
            cv2.imshow('Korozja     (Wcisnij ESC zeby zamknac)', self.rdza)
            cv2.setMouseCallback('Plytka     (Wcisnij ESC zeby zamknac)',okno)
            cv2.setMouseCallback('Korozja     (Wcisnij ESC zeby zamknac)',okno2)

            # Calculating quantity of pixels
            self.H, self.W = self.bgr_img.shape[:2]         # Pixel after image processing
            self.n_pix=self.H*self.W        # Liczba pikseli obrazu
            self.n_t = sum(mask_t == 255)  # Liczba pikseli tła
            self.n_p = self.n_pix-self.n_t  # Liczba pikseli płytki
            self.n_k = sum(mask_k == 255)     # Liczba pikseli korozji
            self.t = (self.n_t / self.n_pix) * 100
            self.p = 100 - self.t
            self.k = (self.n_k / self.n_p) * 100

            self.t = str(round(self.t, 2))
            self.p = str(round(self.p, 2))
            self.k = str(round(self.k, 2))


            self.ui.lcd_rust.display(self.k)
            self.ui.lcd_plate.display(self.p)
            self.ui.lcd_bg.display(self.t)

            # Closing the loop
            key = cv2.waitKey(1)
            if key == 27:
                cv2.destroyAllWindows()
                self.ui.start_button.setEnabled(True)
                break

    def filename(self):
        """
        Display Dialog window to select image for analysis
        :return:
        """
        self.filepath, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Open file", None, "Image Files (*.jpg *.png)")
        self.ui.nazwa_pliku_obiekt.setText(self.filepath)
    def save(self):
        """
        Function responsible for saving the analysis results
        """
        # making a new directory if it's not made yet
        cwd = os.path.abspath(os.getcwd()) + '\\Results\\'
        print(cwd)
        if path.exists(cwd):
            if path.isdir(cwd):
                pass
            else:
                makedirs(cwd, mode=0o777, exist_ok=False)
        else:
            makedirs(cwd, mode=0o777, exist_ok=False)
        # Graphical results + Error handling
        try:
            self.nazwa_probki = self.ui.nazwa_probki_obiekt.text()
            plikG1 = cwd + self.nazwa_probki + '_grafical_results1.png'
            plikG2 = cwd + self.nazwa_probki + '_grafical_results2.png'
            plikG3 = cwd + self.nazwa_probki + '_original.png'
            print(plikG1)
            cv2.imwrite(plikG1,self.plytka)
            cv2.imwrite(plikG2,self.rdza)
            cv2.imwrite(plikG3,self.bgr_img)
        except AttributeError:
            msg = QtWidgets.QMessageBox().warning(self, "Warning", "Wpisz poprawną ścieżkę i nazwę próbki!")
            self.ui.status.setText("...")
            self.ui.progressBar.setValue(0)
            return 0

        self.ui.progressBar.setValue(90)
        plikTXT = cwd + self.nazwa_probki + '_result.txt'
        self.ui.progressBar.setValue(98)
        wynik_txt = "Korozja [%]: " + self.k + '\n' + 'Płytka [%]: ' + self.p + '\n' + 'Tło [%]: ' + self.t
        plikTXT = open(cwd + self.nazwa_probki + '_result.txt', 'w')
        plikTXT.write("Wyniki dla próbki:\t" + self.nazwa_probki + "\n" + wynik_txt)
        plikTXT.close()
        self.ui.progressBar.setValue(100)
        self.ui.status.setText("Saved")

    def getName(self):
        """
        Get the sample name from path
        :return:
        """
        self.ui.nazwa_probki_obiekt.setText(path.basename(self.ui.nazwa_pliku_obiekt.text())[:-4])

    def nothing(self, x):
        """
        Empty function (sometimes used with trackbar callback)
        :param x:
        :return:
        """
        pass

    def okno_bg_color(self):
        """
        Prepare a window for setting the background color
        :return:
        """
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

        self.bgr_img = cv2.resize(self.bgr_img, (1200,1600))
        self.hsv_img = cv2.cvtColor(self.bgr_img, cv2.COLOR_BGR2HSV)
        self.zoomed_img3 = self.hsv_img
        cv2.namedWindow('2xLPM zeby ustawic kolor tla', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('2xLPM zeby ustawic kolor tla', 500, 600)
        cv2.setMouseCallback('2xLPM zeby ustawic kolor tla', self.bg_color_change)
        cv2.imshow('2xLPM zeby ustawic kolor tla', self.zoomed_img3)
        while cv2.getWindowProperty('2xLPM zeby ustawic kolor tla', cv2.WND_PROP_VISIBLE) > 0: # if window is not closed by "x"
            key = cv2.waitKey(100)
            if key == 27:
                cv2.destroyWindow('2xLPM zeby ustawic kolor tla')
                break
        self.ui.bg_color_btn.setEnabled(True)

    def bg_color_change(self,event,x,y,flags,param):
        """
        Function used to set the spinbox values according to selected background color
        :param event: Event triggered
        :param x: x coord
        :param y: y coord
        :param flags: Not required here
        :param param: Not required here
        :return:
        """
        if event == cv2.EVENT_LBUTTONDBLCLK:
            H_bg,S_bg,V_bg=(self.zoomed_img3[y,x])
            #temporary rust mask
            self.ui.spinBox_H.setValue(H_bg)
            self.ui.spinBox_S.setValue(S_bg)
            self.ui.spinBox_V.setValue(V_bg)
            msg = QtWidgets.QMessageBox().about(self, "Done", "Color Set Successfully!")
            
    def help_txt(self):
        """
        Function used to call Help class containing Help dialog
        :return:
        """
        help_text(self).show()
    # Connecting buttons from GUI with corresponding functions
    def interface(self):
        """
        Function which connects user's interactions in GUI with proper functions
        :return:
        """
        self.ui.start_button.clicked.connect(self.start)
        self.ui.save_button.clicked.connect(self.save)
        # self.ui.collect_button.clicked.connect(self.get_images)       # downlowad images from ESP32-CAM   (uncomment one option)
        self.ui.collect_button.clicked.connect(self.filename)           # load image from PC    (uncomment one option)
        self.ui.Button_getName.clicked.connect(self.getName)
        self.ui.bg_color_btn.clicked.connect(self.okno_bg_color)
        self.ui.pushButton_info.clicked.connect(self.help_txt)
        self.ui.pushButton_analyze_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_analyze))
        self.ui.pushButton_set_col_page.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_set_col))

if __name__ == "__main__":
    app = QApplication(argv)
    widget = Wykrywanie_rdzy()
    widget.setWindowFlags(QtCore.Qt.WindowCloseButtonHint)
    images_path = os.path.abspath(os.getcwd()) + '\Zdj\\'
    collector = Collect_Images(GUI=widget, path=images_path)
    filtr = Filter_Images(GUI=widget, path=images_path)
    widget.show()
    exit(app.exec_())