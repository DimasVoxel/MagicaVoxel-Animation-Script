from sys import path_importer_cache
from time import thread_time_ns
from tkinter.constants import CURRENT, Y
from typing import Optional
from ctypes import wintypes, windll, create_unicode_buffer
import pyperclip
import pydirectinput as pydi
import time
import json
import sys
import os


def getForegroundWindowTitle() -> Optional[str]:            #Get current active Window
    hWnd = windll.user32.GetForegroundWindow()
    length = windll.user32.GetWindowTextLengthW(hWnd)
    buf = create_unicode_buffer(length + 1)
    windll.user32.GetWindowTextW(hWnd, buf, length + 1)
    
    if buf.value == "MagicaVoxel | Ephtracy":              #If current active Window Magicavoxel then
        return False                                        #Continue script (not very performant)
    else:
        return True
                                                             

def exitprog():
    input("Press Enter to continue...")
    sys.exit()

def writeToMv():                                                            
    try:
        with open('old-camara.json') as json_file:             #Load Json file
            data = json.load(json_file)                    #Write Json to var
        json_file.close()                                  #Close Json file
    except:                                                #If json not found error
        print("ERROR: You either dont have a camara.json in this folder or you made a mistake.")
        print("Common issues: you wrote true or false with an uppercaseletter or you got a typo somewhere")
        exitprog()

    print("Please open MagicaVoxel and make sure its in the foreground.")
    pause(True)                                            #Wait until window in Active to start script we dont want the script spamming your discord for example
    try:
        frames = float(data['frames'])                     #Get all values from json
        secondPerRender = float(data['SecondsPerRender'])

        pitch = float(data['start']['Pitch'])
        end_pitch = float(data['end']['Pitch'])
        yaw = float(data['start']['Yaw'])
        end_yaw = float(data['end']['Yaw'])
        if yaw < 0:                                            #Edge case since magicavoxel's yaw value goes from -180 to 180 instead of 0 to 360
            yaw = yaw - 360.000001                             #if you want to go in a circle numbers cant be same e.g -180 -> 180
            end_yaw = end_yaw - 360.000001
        if end_yaw < 0:
            end_yaw = end_yaw + 360.000001
            yaw = yaw + 360.000001  
        zoom = float(data['start']['Zoom'])
        end_zoom = float(data['end']['Zoom'])
        roll = float(data['start']['Roll'])
        end_roll = float(data['end']['Roll'])
        x_start = float(data['start']['X'])
        x_end = float(data['end']['X'])
        y_start = float(data['start']['Y'])
        y_end = float(data['end']['Y'])
        z_start = float(data['start']['Z'])
        z_end = float(data['end']['Z'])
    except ValueError:
        print("Error in config. Did you accidentally input a letter instead of a number?")
        exitprog()
 
 
    try:                                                  #Get slope to calculate linear path to next camara position
        m_pitch = float((pitch-end_pitch)/(0-frames))
    except ZeroDivisionError:                             #If start and end pos are the same it will throw an error we are catching it here
        m_pitch = 0

    try:    #catch by 0 div
        if yaw < end_yaw and data['direction'] == "left":    #Since the script cant know how exactly you want the camara to rotate 
            m_yaw = float(((yaw-end_yaw))/(0-frames))        #You can tell it to go left or right
        elif yaw < end_yaw and data['direction'] == "right": 
            m_yaw = float(((yaw-end_yaw)+360)/(0-frames))
        elif yaw > end_yaw and data['direction'] == "left": 
            m_yaw = float(((yaw-end_yaw)-360)/(0-frames))
        elif yaw > end_yaw and data['direction'] == "right": 
            m_yaw = float(((yaw-end_yaw))/(0-frames))
        else:
            m_yaw = 0

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
    
    t_frames = int(frames)              #Determin how often script is going to run
    for x in range(t_frames):
        pitch = pitch + m_pitch         #Very simple way to change values
        yaw = yaw + m_yaw
        zoom = zoom + m_zoom
        roll = roll + m_roll
        x_start = x_start + m_x
        y_start = y_start + m_y
        z_start = z_start + m_z

        command = "cam rx "+str(pitch)+" | cam ry "+str(yaw)+" | cam zoom "+str(zoom)+" | cam rz "+str(roll) 
        command2 = "cam x "+str(x_start)+ " | cam y "+str(y_start)+ " | cam z "+str(z_start)

        print("Currently on Frame "+str(x+1)+"/"+str(int(frames)))  #Progress

        pause(False)                                     #Find out if Magica is Active
        pydi.press('f1')                            #Open console
        pyperclip.copy(command)                     #Copy command paste command into mv
        
        pydi.keyDown("ctrl")
        pydi.press("v")
        pydi.keyUp("ctrl")
        pydi.press('enter')
        pyperclip.copy(command2)
        pause(False)
        pydi.keyDown("ctrl")
        pydi.press("v")
        pydi.keyUp("ctrl")
        pydi.press('enter')
        pydi.press('f1')
        time.sleep(secondPerRender)                 #Wait image to render

        

        if bool(data['saveRenders']):               #if saveRenders is true save image
            pause(False)              
            pydi.press("6")
            time.sleep(0.4)
            pydi.press('enter')
            time.sleep(0.4)
            


def pause(firsttime):
    if firsttime:
        while getForegroundWindowTitle():
            time.sleep(3)    
        pass
    else:   
        if getForegroundWindowTitle():
            print("Progress paused...")
            while getForegroundWindowTitle():
                time.sleep(5)                                   
            print("WARNING: You exited magicavoxel while the render was in progress.")
            print("To avoid problems make sure the console is not selected and if it has any contenct delete it as this might lead to some issues.")
            input("Press enter to confirm")
            print("Select magicavoxel")

            while getForegroundWindowTitle():
                time.sleep(5)              

def main():
    writeToMv()

try:
    main()
except KeyboardInterrupt:
    print('Interrupted')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

