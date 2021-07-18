# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 12:50:26 2020

@author: Krzysztof Dziarmaga
@mail: dziarmag@student.agh.edu.pl
"""
import cv2,time, os, shutil
import requests
import numpy as np

class Collect_Images:
    def __init__(self, GUI=None, path=None):
        """
        Initialize Collect_Images class.
        """
        if GUI:
            self.GUI = GUI
            self.path = path
        else:
            raise Exception("Brak obiektu nadrzędnego - GUI")

    def start_collecting(self):
        """
        Function used to collect images from ESP32-CAM webserver
        :return:
        """
        path = self.path
        url='http://192.168.31.201/cam-hi.jpg'
        cv2.namedWindow('ESP32_CAM',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('ESP32_CAM', 800,600)

        if  os.path.exists('Zdj'):
            shutil.rmtree('Zdj')
        if not os.path.exists('Zdj'):
            os.makedirs('Zdj')

        i=0
        while i < 15:
            i += 1
            try:
                imgResponse2 = requests.get(url)
                time.sleep(0.1)
                # imgnp=np.array(bytearray(imgResponse.read()),dtype=np.uint8)
                imgnp=np.array(bytearray(imgResponse2.content),dtype=np.uint8)
                time.sleep(0.1)
                img=cv2.imdecode(imgnp,-1)

                self.GUI.ui.status.setText('Pobieram i zapisuję obrazy z kamery ...')
                cv2.imshow('ESP32_CAM',img)
                cv2.imwrite(os.path.join(path , str(i)+'.PNG'), img)
                key=cv2.waitKey(5)
                if key==ord('q'):
                    break;
            except KeyboardInterrupt:
                cv2.destroyAllWindows()
                print('Przerwano działanie programu')
                break
        cv2.destroyAllWindows()