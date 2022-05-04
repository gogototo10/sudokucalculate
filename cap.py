
import copy
import time
import sys
import PyQt5
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PIL import ImageGrab
from PIL import Image
import cv2
import keyboard
import mouse
import numpy as np
import pyscreenshot
import pytesseract
import sudocu_calculator
pytesseract.pytesseract.tesseract_cmd = r'tesseract.exe의 주소를 입력'

cacap_UI = 'cacap.ui'




class MainDialog(QDialog):


    def __init__(self):
        self.sudocu_mat_main = [

            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],

            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        QDialog.__init__(self, None)

        uic.loadUi(cacap_UI, self)
        #self.text_file_rw()
        self.setMouseTracking(True)

        self.capture_button.clicked.connect(self.capture_button_Clicked)
        self.calculator_Button.clicked.connect(self.calculator_Button_Clicked)

    def calculator_Button_Clicked(self):
        print("start calculate")
        temp_mat = sudocu_calculator.sudocu_calculation_final(self.sudocu_mat_main)
        self.textEdit_sdocu_write(temp_mat)

    def text_file_rw(self):
        try :
            f = open("text.txt", 'r')
            f_line=f.readlines()
            for f_line_i in f_line:
                for f_line_i_split_i in f_line_i.split(" "):
                    self.sudocu_mat_main[f_line.index(f_line_i)][f_line_i.split(" ").index(f_line_i_split_i)] = int(f_line_i_split_i)
            f.close()
            self.textEdit_sdocu_write(self.sudocu_mat_main)


        except:
            f = open("text.txt", 'w')
            f.write("0 0 0 0 0 0 0 0 0\n")
            f.write("0 0 0 0 0 0 0 0 0\n")
            f.write("0 0 0 0 0 0 0 0 0\n")
            f.write("0 0 0 0 0 0 0 0 0\n")
            f.write("0 0 0 0 0 0 0 0 0\n")
            f.write("0 0 0 0 0 0 0 0 0\n")
            f.write("0 0 0 0 0 0 0 0 0\n")
            f.write("0 0 0 0 0 0 0 0 0\n")
            f.write("0 0 0 0 0 0 0 0 0\n")
            f.close()
            self.textEdit_sdocu_write(self.sudocu_mat_main)

    def textEdit_sdocu_write(self,mat):
        temp_line = ""
        for i in range(0, 9):
            for j in range(0, 9):
                temp_line = temp_line + str(mat[i][j]) + " "
            temp_line = temp_line+"\n"

        self.textEdit.setText(temp_line)


    def capture_button_Clicked(self,buttons):

        

        global x1, y1, x2, y2
        while_flag=True
        while while_flag:
            if mouse.is_pressed() == True:
                x1, y1 = mouse.get_position()
                while_flag=False
                print(x1, y1)
        while_flag = True
        while while_flag:
            if mouse.is_pressed() == False:
                while_flag = False
                x2, y2 = mouse.get_position()
                print(x2, y2)
        if x1>x2:
            temp=x1
            x1=x2
            x2=temp
        if y1 > y2:
            temp = y1
            y1 = y2
            y2 = temp
        print("Your ROI : {0}, {1}, {2}, {3}".format(x1, y1, x2, y2))
        
        im = pyscreenshot.grab(bbox=(x1, y1, x2, y2))
        saveas = 'part_screenshot.png'
        im.save(saveas)
        print("ergergerg")

        im = cv2.imread('part_screenshot.png', cv2.IMREAD_COLOR)
        with_i = int(im.shape[0] / 9)
        height_j = int(im.shape[1] / 9)

        list_of_mat = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
        mat = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]


        for i in range(0,9):
            for j in range(0,9):
                list_of_mat[i][j]=im.copy()

        offset_var=5
        for i in range(0,9):
            for j in range(0,9):
                list_of_mat[i][j]=im[i*with_i+offset_var : (i+1)*with_i-offset_var , j*height_j+offset_var: (j+1)*height_j-offset_var]

        for i in range(0, 9):
            for j in range(0, 9):
                if (pytesseract.image_to_string(list_of_mat[i][j], config='--psm 6')).split('\n')[0] in ["1","2","3","4","5","6","7","8","9"]:
                    mat[i][j]=int(pytesseract.image_to_string(list_of_mat[i][j], config='--psm 6').split('\n')[0])

                elif (pytesseract.image_to_string(list_of_mat[i][j], config='--psm 6')).split('\n')[0] == "A":
                    mat[i][j]=4
                print(mat[i][j])


        for i in range(0,9):
            print(mat[i])
        print("debug1")
        self.textEdit_sdocu_write(mat)
        self.sudocu_mat_main = copy.deepcopy(mat)



app = QApplication(sys.argv)
main_dialog = MainDialog()
main_dialog.show()

app.exec_()