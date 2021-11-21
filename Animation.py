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
        with open('camara.json') as json_file:             #Load Json file
            global data
            data = json.load(json_file)                    #Write Json to var
        json_file.close()                                  #Close Json file
    except:                                                #If json not found error
        print("ERROR: You either dont have a camara.json in this folder or you made a mistake.")
        print("Common issues: you wrote true or false with an uppercaseletter or you got a typo somewhere")
        exitprog()

    print("Please open MagicaVoxel and make sure its in the foreground.")
    pause(True)                                            #Wait until window in Active to start script we dont want the script spamming your discord for 
    keyframenum = 0
  

    while keyframenum+1 < len(data['keyframe']):
        currentkeyframe = data['keyframe'][keyframenum]
        nextkeyframe = data['keyframe'][keyframenum + 1]
        keyframenum += 1

        try:
            frames =          float(currentkeyframe['Frames'])                     
            secondPerRender = float(currentkeyframe['SecondsPerRender'])
            c_dircetion =       currentkeyframe['Direction']
            c_pitch  =          float(currentkeyframe['Pitch'])
            c_yaw    =          float(currentkeyframe['Yaw'])
            c_zoom   =          float(currentkeyframe['Zoom'])
            c_roll   =          float(currentkeyframe['Roll'])
            c_x      =          float(currentkeyframe['X'])
            c_y      =          float(currentkeyframe['Y'])
            c_z      =          float(currentkeyframe['Z'])
           
            n_pitch  =          float(nextkeyframe['Pitch'])
            n_yaw    =          float(nextkeyframe['Yaw'])
            n_zoom   =          float(nextkeyframe['Zoom'])
            n_roll   =          float(nextkeyframe['Roll'])
            n_x      =          float(nextkeyframe['X'])
            n_y      =          float(nextkeyframe['Y'])
            n_z      =          float(nextkeyframe['Z'])

        except ValueError:
            print("Error in config. Did you accidentally input a letter instead of a number?")
            exitprog()

        try: m_zoom = float((c_zoom-n_zoom)/(0-frames))
        except ZeroDivisionError: m_zoom = 0  

        try: m_roll = float((c_roll-n_roll)/(0-frames))
        except ZeroDivisionError: m_roll = 0

        try: m_x = float((c_x-n_x)/(0-frames))
        except ZeroDivisionError: m_x = 0

        try: m_y = float((c_y-n_y)/(0-frames))
        except ZeroDivisionError: m_y = 0   

        try: m_z = float((c_z-n_z)/(0-frames))
        except ZeroDivisionError: m_z = 0   
                                 
        try: m_pitch = float((c_pitch-n_pitch)/(0-frames))
        except ZeroDivisionError: m_pitch = 0

        try:    
            if c_yaw < n_yaw and c_dircetion == "right":    
                m_yaw = float(((n_yaw-360)-c_yaw)/frames) #not normal right -90 -> 90 
            elif c_yaw > n_yaw and c_dircetion == "right":    
                m_yaw = float((n_yaw-c_yaw)/frames) #normal right 0 -> -90    
            elif c_yaw < n_yaw and c_dircetion == "left":    
                m_yaw = float((n_yaw-c_yaw)/frames) #normal left -90 -> 90 
            elif c_yaw > n_yaw and c_dircetion == "left":    
                m_yaw = float(((n_yaw+360)-c_yaw)/frames) #not normal left 90 -> -90    
            else:
               m_yaw = 0
        except ZeroDivisionError:
            m_yaw = 0

        t_frames = int(frames)              #Determin how often script is going to run
        for x in range(t_frames):
            c_pitch = c_pitch + m_pitch
            c_yaw = c_yaw + m_yaw
            c_zoom = c_zoom + m_zoom
            c_roll = c_roll + m_roll
            c_x = c_x + m_x
            c_y = c_y + m_y
            c_z = c_z + m_z

            command = "cam rx "+str(c_pitch)+" | cam ry "+str(c_yaw)+" | cam zoom "+str(c_zoom)+" | cam rz "+str(c_roll) 
            command2 = "cam x "+str(c_x)+ " | cam y "+str(c_y)+ " | cam z "+str(c_z)

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

            if bool(data['saveRenders']):
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
    sys.exit(0)


