# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 11:23:16 2021

@author: Krzysztof Dziarmaga
@mail: dziarmag@student.agh.edu.pl
"""
import numpy as np
import os, cv2

class Filter_Images:
    def __init__(self, GUI=None, path=None):
        """
        Initialize Filter_Images class.
        """
        if GUI:
            self.GUI = GUI
            self.path = path
        else:
            raise Exception("Brak obiektu nadrzędnego - GUI")

    def filtruj(self):
        image_folder=self.path
        file_list = os.listdir(image_folder)
        file_list = [os.path.join(image_folder, x) for x in file_list if x.endswith(('.PNG', '.png'))]
        first = True
        processed_img = 0

        image_stacks = np.zeros(shape=(len(file_list), 1200, 1600, 3), dtype=np.uint8)
        for i in range(image_stacks.shape[0]):
            processed_img += 1
            im=cv2.imread(file_list[i])
            image_stacks[i] = np.array(im)
            print("\r", 'Processing photos... {:2.1%}'.format(processed_img/len(file_list)), end='')


        image_median = np.median(image_stacks, axis=0).astype(np.uint8)
        # image_median = Image.fromarray(image_median)
        # comparison=np.hstack((image_stacks[0],image_median))
        # cv2.imwrite('Przed.PNG', image_stacks[0])
        cv2.imwrite(image_folder + 'Po_median.PNG', image_median)
        # hi_res=cv2.resize(image_median, (3200, 2400))

        # key=cv2.waitKey(0)
        # if key==ord('q'):
        #     cv2.destroyAllWindows()
        GUI.ui.nazwa_pliku_obiekt.setText(image_folder + 'Po_median.PNG')
        self.ui.nazwa_pliku_obiekt.setEnabled(False)





