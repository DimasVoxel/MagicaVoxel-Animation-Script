from sys import path_importer_cache
from time import thread_time_ns
from tkinter.constants import CURRENT
from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer
import pyperclip
import pydirectinput as pydi
import time
import json
import sys


def getForegroundWindowTitle() -> Optional[str]:
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    
    if buf.value == "MagicaVoxel | Ephtracy":               
        return True
    else:
        time.sleep(5)
        getForegroundWindowTitle()


def writeToMv():
    try:
        with open('camara.json') as json_file:
            data = json.load(json_file)
        json_file.close()
    except:
        print("You dont have a camara.json in this folder. Please download it from the place you got this script from.")
        input("Press Enter to continue...")
        sys.exit()

    print("Please open MagicaVoxel and make sure its in the foreground.")
    getForegroundWindowTitle() 
    
    frames = float(data['frames'])
    secondPerRender = float(data['SecondsPerRender'])
    pitch = float(data['Pitch'])
    end_pitch = float(data['End_Pitch'])
    yaw = float(data['Yaw'])
    end_yaw = float(data['End_Yaw'])
    zoom = float(data['Zoom'])
    end_zoom = float(data['End_Zoom'])
    roll = float(data['Roll'])
    end_roll = float(data['End_Roll'])
    x_start = float(data['Start_X'])
    x_end = float(data['End_X'])
    y_start = float(data['Start_Y'])
    y_end = float(data['End_Y'])
    z_start = float(data['Start_Z'])
    z_end = float(data['End_Z'])

#catch by 0 div

    try:
        m_pitch = float((pitch-end_pitch)/(0-frames))
    except ZeroDivisionError:
        m_pitch = 0

    try:
        m_yaw = float((yaw-end_yaw)/(0-frames))
    except ZeroDivisionError:
        m_yaw = 0    

    try:
        m_zoom = float((zoom-end_zoom)/(0-frames))
    except ZeroDivisionError:
        m_zoom = 0  

    try:
        m_roll = float((roll-end_roll)/(0-frames))
    except ZeroDivisionError:
        m_roll = 0

    try:
        m_x = float((x_start-x_end)/(0-frames))
    except ZeroDivisionError:
        m_x = 0

    try:
        m_y = float((y_start-y_end)/(0-frames))
    except ZeroDivisionError:
        m_y = 0   

    try:
        m_z = float((z_start-z_end)/(0-frames))
    except ZeroDivisionError:
        m_z = 0   

    print(m_z)
    
    t_frames = int(frames)
    for x in range(t_frames):
        pitch = pitch + m_pitch
        yaw = yaw + m_yaw
        zoom = zoom + m_zoom
        roll = roll + m_roll
        x_start = x_start + m_x
        y_start = y_start + m_y
        z_start = z_start + m_z

        command = "cam rx "+str(pitch)+" | cam ry "+str(yaw)+" | cam zoom "+str(zoom)+" | cam rz "+str(roll)
        command2 = "cam x "+str(x_start)+ " | cam y "+str(y_start)+ " | cam z "+str(z_start)

        print("Currently on Frame "+str(x)+"/"+str(frames))
        print("Time remaining " + str(round((t_frames-x)*secondPerRender+((t_frames-x)*0.8),2)))

        getForegroundWindowTitle()
        pydi.press('f1')
        pyperclip.copy(command)
        
        pydi.keyDown("ctrl")
        pydi.press("v")
        pydi.keyUp("ctrl")
        pydi.press('enter')
        pyperclip.copy(command2)
        getForegroundWindowTitle()
        pydi.keyDown("ctrl")
        pydi.press("v")
        pydi.keyUp("ctrl")
        pydi.press('enter')
        pydi.press('f1')
        time.sleep(secondPerRender)

        if bool(data['saveRenders']):
            getForegroundWindowTitle()
            pydi.press("6")
            time.sleep(0.4)
            pydi.press('enter')
            time.sleep(0.4)
def main():

    writeToMv()

main()
