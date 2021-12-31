import ctypes
import serial
from pynput.mouse import Button, Controller

from serial import Serial 
import threading
import pydirectinput

from queue import Queue

import keyboard as k

user32 = ctypes.windll.user32
width = user32.GetSystemMetrics(0)
height=user32.GetSystemMetrics(1)



ser=serial.Serial('COM3',9600)


mouse = Controller()


def PressKeys(in_q):
    while True:
        arr=in_q.get().split(' ')
        #mouseButtonLeft   
        if arr[0]=='0':
            mouse.click(Button.left, 1)
        if arr[1]=='0':
            k.press('s')
        else:
            k.release('s')
        if arr[2]=='0':
            k.press('space')
        else:
            k.release('space')           
        if arr[3]=='0':
            k.press('a')
        else:
            k.release('a')
        if arr[4]=='0':
            k.press('e')
        else:
            k.release('e')
        if arr[5]=='0':
            k.press('w')
        else:
            k.release('w')
        if arr[6]=='0':
            mouse.click(Button.middle, 1)
        if arr[7]=='0':
            k.press('r')
        else:
            k.release('r')
        if arr[8]=='0':
            k.press('d')
        else:
            k.release('d')

def moveRpos(arr):
    if arr[1]=='0':
        #down
        pydirectinput.moveTo(int(width/2),-height)
        mouse.click(Button.left, 1)       
    if arr[3]=='0':
        #left
        pydirectinput.moveTo(-width,int(height/2))
        mouse.click(Button.left, 1)
    if arr[5]=='0':
        #up
        pydirectinput.moveTo(int(width/2),height)
        mouse.click(Button.left, 1)
    if arr[8]=='0':
        #right
        pydirectinput.moveTo(width,int(height/2))
        mouse.click(Button.left, 1)
                                                            



def Readdata():
        data=ser.readline(1000)
        data=str(data).replace("'",'').replace("b",'').replace("\\r\\n",'')
        print(data)
        return data

def ReadData(out_q):
    while True:
        data=ser.readline(1000)
        data=str(data).replace("'",'').replace("b",'').replace("\\r\\n",'')
        out_q.put(data)
        print(data)


def main():
    q = Queue()
    
    t1=threading.Thread(target=ReadData, args =(q, ))
    t2=threading.Thread(target=PressKeys, args =(q, ))

    t1.start()
    t2.start()

if __name__ == '__main__':
    main()