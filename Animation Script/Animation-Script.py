import os
import sys

import pyperclip
import time
import json

if sys.platform == 'win32':
    from ctypes import windll, create_unicode_buffer
    import pydirectinput as pydi
    k_console = 'f1'
elif sys.platform == 'darwin':
    from AppKit import NSWorkspace
    import pyautogui as pydi #Use PyAutoGUI instead since pydirectinput is windows only
    k_console = 'f2'
else:
    raise OSError('Unsupported OS')

pydi.PAUSE = 0.01
atime = int(0)

def magicaIsForeground():
    if sys.platform == 'win32':
        hWnd = windll.user32.GetForegroundWindow()
        length = windll.user32.GetWindowTextLengthW(hWnd)
        buf = create_unicode_buffer(length + 1)
        windll.user32.GetWindowTextW(hWnd, buf, length + 1)
        if buf.value == 'MagicaVoxel | Ephtracy':              #If current active Window Magicavoxel then
            return True                                       #Continue script (not very performant) takes about 0.2 seconds to run and is has a noticable impact how fast something can go.
        else:
            return False
    elif sys.platform == 'darwin':
        if NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationName'] == 'MagicaVoxel':
            return True
        else:
            return False


def exitprog():
    input('Press Enter to continue...')
    sys.exit()


def beziersetup(firstkeyframe, lastkeyframe, data, ammountframes):

    #Setup + Error check
    params = []
    isdupicate = False
    for keyframe in range(firstkeyframe, lastkeyframe + 1):
        for param,value in data['keyframe'][keyframe]['param'].items():
            if param not in params:
                params.append(param)
            else:
                isdupicate = True

    if isdupicate == False:
        print('The animation has been stopped since there are no parameters to animate.\nFor an animation you need atleast 2 keyframes with the same parameter')
        print(f'Skipping Keyframes: {firstkeyframe} to {lastkeyframe}')
        return

    for frame in range(ammountframes):
        starttime = time.time()
        command = []
        commandstring = ' '
        if bool(data['global']['saverenders']) == True and frame != 0:
            commandstring ='snap scene | '

        for i in range(len(params)):
            key = params[i]
            lerparray = []
            for keyframe in range(firstkeyframe, lastkeyframe+1):
                if key in data['keyframe'][keyframe]['param']:
                    lerparray.append(data['keyframe'][keyframe]['param'][key])
            if key.find('ry') != -1:
                lerparray = beznormalise(lerparray,firstkeyframe,lastkeyframe,data)

            commandstring = commandstring + key + ' ' + str(round(bezier(lerparray, frame/ammountframes),4)) + ' | '
            if len(commandstring) > 400:
                command.append(commandstring)
                commandstring = ''
        commandstring = commandstring + ' ' + animationHandler(firstkeyframe,data)
        command.append(commandstring)

        try: print('#'*(os.get_terminal_size().columns))
        except (OSError, ValueError): pass
        print(f'\nLast command: {command}')
        print(f'Frame: {frame+1} of {ammountframes}')
        mvinput(command,float(data['keyframe'][firstkeyframe]['option']['secondsperrender']))

        #endtimer
        endtime = time.time()


        print(f'\nTime taken: {endtime - starttime:.2f} seconds')
        #estimate time left time x frames
        time_estimate = (endtime - starttime) * (ammountframes - frame)
        print(f'Estimated time left: {time_estimate:.2f} seconds')
        print(f'Estimated time left: {time_estimate/60:.2f} minutes')
        print(f'Estimated time left: {time_estimate/3600:.2f} hours')

def beznormalise(lerparray, firstkeyframe, lastkeyframe, data):
    '''
    Normalises angles, such that they will wrap around correctly around 360 degrees, and will rotate in the right direction.
    If the next angle is the same as the previous angle, it will assume a full rotation.
    '''
    newlerparray = [lerparray[0]]
    for i in range(firstkeyframe,lastkeyframe):
        p_yaw = newlerparray[-1]
        n_yaw = data['keyframe'][i+1]['param']['cam ry']

        if data['keyframe'][i+1]['option']['direction'] == 'Clockwise':
            while n_yaw <= p_yaw:
                n_yaw = n_yaw + 360
            newlerparray.append(n_yaw)
        elif data['keyframe'][i+1]['option']['direction'] == 'Counterclockwise':
            while n_yaw >= p_yaw:
                n_yaw = n_yaw - 360
            newlerparray.append(n_yaw)
        elif data['keyframe'][i+1]['option']['direction'] == 'Static':
            newlerparray.append(p_yaw)

    return newlerparray


def bezier(lerparray, perc):
    while len(lerparray) > 1:
        lerparray = [lerp(a, b, perc) for a, b in zip(lerparray, lerparray[1:])] #Only slice the second one, because the zip will slice the first one
    return lerparray[0]


def lerp(a, b, t):
    return float(a + (b - a) * t)


def readconfig():
    try:
        global data
        with open('config.json') as json_file:             #Load Json file
            data = json.load(json_file)                    #Write Json to var
        json_file.close()                                  #Close Json file
    except:                                                #If json not found error
        print('ERROR: No config.json in this folder.')
        exitprog()

    if data['version'] == '3':
        print('Your config file is outdated. Please generate a new one.')
        exitprog()

    print('Please open MagicaVoxel and make sure its in the foreground.')
    pause(True)                                            #Wait until window in Active to start script we dont want the script spamming your discord for
    interpolation = []

    for keyframe in data['keyframe']:
        try:
            if keyframe['option']['interpolation'] == 'linear':
                interpolation.append('linear')
            elif keyframe['option']['interpolation'] == 'bezier':
                interpolation.append('bezier')
            elif keyframe['option']['interpolation'] == 'bezier-sequence':
                interpolation.append('sequence')
        except:
            interpolation.append('1')

    for i in range(len(data['keyframe'])-1):
        if interpolation[i] == 'linear':
            liniar(i, data)
        elif interpolation[i] == 'bezier':
            ammountframes = int(data['keyframe'][i]['option']['frames'])
            for j in range(i+1,len(data['keyframe'])-1):
                if interpolation[j] == 'sequence':
                    ammountframes = int(data['keyframe'][j]['option']['frames'])+ammountframes
                else:
                    break
            beziersetup(i, j+1, data, ammountframes)





def animationHandler(currentkeyframe, data):
    global atime
    if True == data['keyframe'][currentkeyframe]['animation']['enable animation']:
        if atime == int(data['keyframe'][currentkeyframe]['animation']['endframe']):
            if data['keyframe'][currentkeyframe]['animation']['loop'] == True:
                atime = int(data['keyframe'][currentkeyframe]['animation']['startframe'])
        else:
            atime = atime + 1
    else:
        return ''
    return 'set a_time '+ str(int(atime)) + ' | '

def normalise(val):
    return (val % 360 + 360) % 360

def normaliseneg(val):
    return (val % -360 + -360) % -360

def liniar(currentkeyframe, data):
    try:
        totalframeCurKeyframe = int(data['keyframe'][currentkeyframe]['option']['frames'])
        global atime

        for i in range(0, totalframeCurKeyframe):
            #starttimer
            starttime = time.time()
            command = []
            commandValue = ''

            if bool(data['global']['saverenders']) and i != 0:
                commandValue ='snap scene | '

            for key, _ in data['keyframe'][currentkeyframe]['param'].items():
                try:
                    startPos = float(data['keyframe'][currentkeyframe]['param'][key])
                    goalPos = float(data['keyframe'][currentkeyframe+1]['param'][key])
                except KeyError:
                    print(f'\nERROR: Parameter {key} is missing in target keyframe. Parameter is being skipped.')
                    goalPos = startPos

                if key.find('ry') != -1: #There should be a function that does normalisation for all parameters that require it not just cam ry / yaw
                    currentDircetion = data['keyframe'][currentkeyframe]['option']['direction']
                    if currentDircetion == 'clockwise':
                        startPos = normalise(startPos)
                        goalPos = normalise(goalPos)
                    elif currentDircetion == 'counterclockwise':
                        startPos = normalise(startPos)
                        goalPos = normaliseneg(goalPos)

                commandValue = commandValue + key + ' ' + str(round(lerp(startPos, goalPos, i/totalframeCurKeyframe),4)) + ' | '
            if 'animation' in data['keyframe'][currentkeyframe]:
                commandValue = commandValue + ' ' + animationHandler(currentkeyframe,data)
            command.append(commandValue)

            secondPerRender = float(data['keyframe'][currentkeyframe]['option']['secondsperrender'])

            #endtimer

            print(f'Frame: {i} of {totalframeCurKeyframe-1}')


            mvinput(command,secondPerRender)

            endtime = time.time()

            print(f'\nTime taken: {endtime - starttime:.2f} seconds')
            time_estimate = (endtime - starttime) * (totalframeCurKeyframe - i)
            #estimate time left time x frames
            print(f'Estimated time left: {time_estimate:.2f} seconds')
            print(f'Estimated time left: {time_estimate/60:.2f} minutes')
            print(f'Estimated time left: {time_estimate/3600:.2f} hours\n')
            try: print('#'*(os.get_terminal_size().columns))
            except (OSError, ValueError): pass



    except ValueError:
        print('Error in config. Did you accidentally input a letter instead of a number?')
        exitprog()

    #print('Keyframe: ' + str(currentkeyframe+2) + ' of ' + str(len(data['keyframe'])))

def paste():
    '''
    Pastes the content of the clipboard to the selected text input field.
    '''
    if sys.platform == 'win32': #For windows, use individual keypresses, because pydirectinput does not support .hotkey()
        pydi.keyDown('ctrl')
        pydi.press('v')
        pydi.keyUp('ctrl')
    elif sys.platform == 'darwin': #For MacOS use .hotkey() since it is simpler, and more reliable
        pydi.hotkey('command', 'v')

def mvinput(command,secondPerRender):
    for cmd in command:
        #Wait until the magicaVoxel window is in the foreground again
        pause(False)
        #Once it is in the foreground, execute the commands
        pydi.press(k_console) #Open Magica console
        pyperclip.copy(cmd)
        paste()
        time.sleep(0.2)
        pydi.press('enter') #Confirm command
        if bool(data['global']['saverenders']) == True:
            time.sleep(0.2)
            pydi.press('enter') #Confirm the save render popup

        #Close the Magica console again to get back to have Magica be in its "starting state" again with no console selected.
        #On MacOS, this has to be done every time. On Windows, this has to be done only if no save popup was created, because here a save popup will deselect the console.
        if sys.platform == 'darwin' or not cmd.startswith('snap'):
            time.sleep(0.2)
            pydi.press(k_console)
    time.sleep(secondPerRender)


def pause(firsttime):
    '''
    Waits until MagicaVoxel is set to the foreground (again), to make sure no inputs are given if the user switches to a different program during execution.
    '''
    if firsttime:
        while not magicaIsForeground():   #Detect if magicavoxel is active to not spam mv commands into normal user programms like discord
            time.sleep(3)
    else:
        if not magicaIsForeground():
            print('Progress paused...')     #This message appears if magicavoxel is not active anymore to prevent damage or unwanted messages
            while not magicaIsForeground():
                time.sleep(5)
            print('WARNING: You exited magicavoxel while the render was in progress.')
            print('To avoid problems make sure the console is not selected and if it has any contenct delete it as this might lead to some issues.')
            input('Press enter to confirm')
            print('Select magicavoxel')

            while not magicaIsForeground():
                time.sleep(5)


def main():
    readconfig()
start_time = time.time()


try:
    main()
except KeyboardInterrupt:
    print('Interrupted')
    sys.exit(0)

#let console open till user closes it
print(f'Finished in --- {time.time() - start_time:.0f} seconds ---')
input()
