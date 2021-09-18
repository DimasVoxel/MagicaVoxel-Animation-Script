# MagicaVoxel-Animation-Script
This little script was created to animate MagicaVoxels camara for more interesting and dynamic renders and animations.

How to install:

**Install** the latest version of Python: https://www.python.org/

Once installed **open Powershell** using **windows key + r** and input powershell into the newly opened textbox

Navigate to the folder you this script at and exectue:

**pip install -r requirements.txt**

You're now ready to execute the script. 

**python.exe .\animation.py**

How to use:


Explanation of camara.json:

{
"frames":    "100",       #How many frames do you want to render  
"SecondsPerRender":"15",  #How long do you want the script to wait for the render to complete - In seconds  
"saveRenders": true,      #Toggle if renders should be saved | Either: true or false  
"direction": "right",     #In which direction should the camara rotate Example: https://imgur.com/a/b8TBVBQ  

"Start_X":   "0",         #The following options represent the ones out of MagicaVoxel  
"Start_Y":   "0",  
"Start_Z":   "0",  
"Zoom":      "0",  
"Pitch":     "0",  
"Yaw":       "0",  
"Roll":      "0",  

"End_X":     "0",  
"End_Y":     "0",  
"End_Z":     "0",  
"End_Zoom":  "0",  
"End_Pitch": "0",  
"End_Yaw":   "0",   
"End_Roll":  "0"  
}  
