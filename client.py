from tkinter import *
import sys
import numpy as np
sys.path.append('/usr/local/lib/python2.7/site-packages')
import cv2

root = Tk() 
root.geometry('400x400')

def binaryOfFraction(fraction): 
    binary = str() 

    while (fraction): 
        fraction *= 2
        if (fraction >= 1): 
            int_part = 1
            fraction -= 1
        else: 
            int_part = 0

        binary += str(int_part) 
    return binary 
  
def floatingPoint(real_no): 
    sign_bit = 0
    if(real_no < 0): 
        sign_bit = 1
    real_no = abs(real_no) 
  
    int_str = bin(int(real_no))[2 : ] 
    fraction_str = binaryOfFraction(real_no - int(real_no)) 
    ind = int_str.index('1') 
    exp_str = bin((len(int_str) - ind - 1) + 127)[2 : ] 
    mant_str = int_str[ind + 1 : ] + fraction_str 
    mant_str = mant_str + ('0' * (23 - len(mant_str))) 

    return sign_bit, exp_str, mant_str 


def convertToInt(mantissa_str): 
    power_count = -1
    mantissa_int = 0

    for i in mantissa_str:  
        mantissa_int += (int(i) * pow(2, power_count)) 
        power_count -= 1

    return (mantissa_int + 1) 

def ispisiMantisu():
    sign_bit, exp_str, mant_str = floatingPoint(value1.get())
    ieee_32 = str(sign_bit) + '-' + exp_str + '-' + mant_str 
    value2.set(ieee_32)

def ispisiBroj():
    ieee_32 = value2.get()
    sign_bit = int(ieee_32[0]) 
    exponent_bias = int(ieee_32[2 : 10], 2) 
    exponent_unbias = exponent_bias - 127 
    mantissa_str = ieee_32[11 : ] 
    mantissa_int = convertToInt(mantissa_str) 
    real_no = pow(-1, sign_bit) * mantissa_int * pow(2, exponent_unbias) 
    value1.set(real_no)

# Input 1
value1 = DoubleVar()
a = Label(root, text ="Float broj") 
a.pack()
unosBroja = Entry(root, width=20, textvariable=value1)
unosBroja.pack()
button1 = Button(root, text="Ispisi mantisu", command=ispisiMantisu)
button1.pack()

# Input 2
value2 = StringVar()
a = Label(root, text ="IEEE754") 
a.pack()
unosMantise = Entry(root, width=100, textvariable=value2)
unosMantise.pack()
button2 = Button(root, text="Ispisi broj", command=ispisiBroj)
button2.pack()

def gammaTransform():
    image1 = cv2.imread('math.jpg', 1)
    image2 = (int(spin.get()) - image1)
    cv2.imshow('Gamma transformation', image2)

spin = Spinbox(root, from_= 0, to = 255, command=gammaTransform)
spin.pack()

root.mainloop()