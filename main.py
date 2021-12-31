import pydirectinput
import serial
from serial import Serial 
import threading

import ctypes
from queue import Queue

import keyboard as k

from pynput.mouse import Controller,Button

mouse=Controller()

ser=serial.Serial('COM3',9600)

def MouseClick():
    ctypes.windll.user32.mouse_event(2, 0, 0, 0,0) # left down
    ctypes.windll.user32.mouse_event(4, 0, 0, 0,0) # left up

def PressKeys(in_q):
    while True:
        arr=in_q.get().split(' ')
        #mouseButtonLeft   
        if arr[0]=='0':
            k.press('l')
        else:
            k.release('l')
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
            k.press('q')
        else:
            k.release('q')
        if arr[7]=='0':
            k.press('r')
        else:
            k.release('r')
        if arr[8]=='0':
            k.press('d')
        else:
            k.release('d')
                                                                

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