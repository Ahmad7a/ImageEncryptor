# tkinter module allows simplistic GUI interface
import argparse
import tkinter as tk
from tkinter import filedialog

import cv2  # --> assists with image manipulation based on OpenCV,
# numpy and PIL are imported for array and image manipulation respectively,
import numpy as np
from PIL import Image
from numpy import random  # --> random is used for generating semi-random numbers or values.


class xor():

    def open_file(self):
        root = tk.Tk()
        root.withdraw()  # hide window
        root.focus_force()
        filepath = filedialog.askopenfilename(title="Select image")  # show dialog and retrieve full file path
        return filepath

    def gen_key(self, r, c, t):  # --> Create random key
        key_name = filedialog.asksaveasfilename(title='Please select where to save the key:')
        key = random.randint(256, size=(r, c, t))
        random.randint(2, size=(r, c, t))

        cv2.imwrite(key_name, key)
        return key_name

    # Main
    def main(self):

        try:
            exitBool = True
            while (exitBool == True):
                menu = 'choose one of the following:\n 1.encryption\n 2.decryption  \n [ press 0 for exit ] \n'
                choice = input(menu)
                if choice == '1':
                    org = cv2.imread(self.open_file())  # --> Load original image
                    r, c, t = org.shape  # --> returns a tuple containing the number of rows, columns, and channels in the image.
                    # r: number of rows, c: number of columns, t: number of color channels.

                    key_name = self.gen_key(r, c, t)
                    key = np.asarray(Image.open(key_name).convert('RGB'))

                    # Encryption
                    enc = org ^ key
                    enc_name = filedialog.asksaveasfilename(title='Please choose where to save the encrypted image:')
                    cv2.imwrite(enc_name, enc)


                elif choice == '2':
                    enc = cv2.imread(self.open_file())  # --> reads in an image file and stores it as a variable in
                    # the OpenCV (Computer Vision) format.
                    r, c, t = enc.shape

                    key_name = filedialog.askopenfilename(title="Select the key file: ")
                    key = np.asarray(Image.open(key_name).convert('RGB'))

                    # decryption
                    dec = enc ^ key
                    dec_name = filedialog.asksaveasfilename(title='Please select where to save the decrypted image:')
                    cv2.imwrite(dec_name, dec)

                elif choice == '0':
                    print("Exiting the program...")
                    exitBool = False

        except BaseException:
            print("**** an Exception is occurred ****")
            print("Exception type: " + str(BaseException))

        finally:
            print("< Thank you for using XOR Image encryptor (: >")

x = xor()
x.main()