# MagicaVoxel-Animation-Script
This little script was created to animate MagicaVoxels camera for more interesting and dynamic renders and animations.

WINDOWS ONLY  
Supported MV version: 99.6.4


Download executable from here: https://dimasvoxel.gumroad.com/l/KrSWL

How to install source code:

**Install** the latest version of Python: https://www.python.org/

Once installed **open Powershell** using **windows key + r** and input powershell into the newly opened textbox

Navigate to the folder you saved this script at and exectue:

**pip install -r requirements.txt**

You're now ready to execute the script. 

**python.exe .\animation.py**

How to use: https://youtu.be/9lkYa2ao8XM


Explanation of camara.json:

{
"frames":    "100",       #How many frames do you want to render  
"SecondsPerRender":"15",  #How long do you want the script to wait for the render to complete - In seconds  
"saveRenders": true,      #Toggle if renders should be saved | Either: true or false  
"direction": "right",     #In which direction should the camera rotate Example: https://imgur.com/a/b8TBVBQ  

"start":   
    {   
    "X":   "123",  
    "Y":   "0",  
    "Z":   "0",  
    "Zoom":      "200",  
    "Pitch":     "-90",  
    "Yaw":       "0",  
    "Roll":      "0"  
    },

"end":   
    {   
    "X":     "0",  
    "Y":     "0",   
    "Z":     "0",  
    "Zoom":  "0",  
    "Pitch": "0",  
    "Yaw":   "0",  
    "Roll":  "0"  
    }  
}  
