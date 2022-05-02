import json
import dearpygui.dearpygui as dpg

global config 
config = {}
config["keyframe"] = []
global setup
setup =False

global magicavoxel_parameters
magicavoxel_paramters = { 
    "camera":{
        "cam rx": {
            "desc":"Camera Pitch",
            "optionType":"float",
            "min":"-90",
            "max":"90"
        },
        "cam ry":{
            "desc":"Camera Yaw",
            "optionType":"float",
            "min":"-180",
            "max":"180"
        },
        "cam rz":{
            "desc":"Camera Roll", 
            "optionType":"float",
            "min":"-180",
            "max":"180"
        },
        "cam zoom":{
            "desc":"Camera Zoom",
            "optionType":"float",
            "min":"0",
            "max":"500000"
        },
        "set pt_fov":{
            "desc":"Camera FOV",
            "optionType":"float",
            "min":"0",
            "max":"360"
        },
        "cam x":{
            "desc":"Camera X",
            "optionType":"float",
            "min":"-10000",
            "max":"10000"
        },
        "cam y":{
            "desc":"Camera Y",
            "optionType":"float",
            "min":"-10000",
            "max":"10000"
        },
        "cam z":{
            "desc":"Camera Z",
            "optionType":"float",
            "min":"-10000",
            "max":"10000"
        },
        "set pt_fix_focus 1 | set pt_dof":{
            "desc":"Aperture",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_blade_rot":{
            "desc":"Blade Rotation",
            "optionType":"float",
            "min":"-180",
            "max":"180"
        },
        "set pt_expo":{
            "desc":"Exposure",
            "optionType":"float",
            "min":"0",
            "max":"16"
        },
        "set pt_bloom_mix":{
            "desc":"Bloom Mix",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_bloom_sca":{
            "desc":"Bloom Size",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_bloom_asp":{
            "desc":"Bloom Aspect Ratio",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_bloom_thr":{
            "desc":"Bloom Threshold",
            "optionType":"float",
            "min":"0",
            "max":"100"
        }
    },
    "light": {
        "set pt_sun_p":{
            "desc":"Sun pitch",
            "optionType":"float",
            "min":"-90",
            "max":"90"
    },
        "set pt_sun_y":{
            "desc":"Sun yaw",
            "optionType":"float",
            "min":"0",
            "max":"360"
        },
        "set pt_sun_area":{
            "desc":"Sun area",
            "optionType":"float",
            "min":"0",
            "max":"100"
        },
        "set pt_isun":{
            "desc":"Sun intensity",
            "optionType":"float",
            "min":"0",
            "max":"500"
        },
        "set pt_isky":{
            "desc":"Sky intensity - Uniform mode only",
            "optionType":"float",
            "min":"0",
            "max":"500"
        },
        "set pt_ray_d":{
            "desc":"Rayleight - Atmosphere only",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_mie_d":{
            "desc":"Mie - Atmosphere only",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_o3_d":{
            "desc":"Ozone - Atmosphere only",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_mie_g":{
            "desc":"Mie Scattering - Atmosphere only",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_ibl_i":{
            "desc":"IBL Intensity - IBL mode only",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_ibl_rot":{
            "desc":"IBL Rotation - IBL mode only",
            "optionType":"float",
            "min":"0",
            "max":"360"
        },
        "set pt_fog_et":{
            "desc":"Fog Density",
            "optionType":"float",
            "min":"0",
            "max":"5000"
        },
        "set pt_fog_eg":{
            "desc":"Fog Phase",
            "optionType":"float",
            "min":"-0.9",
            "max":"0.9"
        },
    },
    "param": {
        "cam rx": {
            "desc":"Camera Pitch",
            "optionType":"float",
            "min":"-90",
            "max":"90"
        },
        "cam ry":{
            "desc":"Camera Yaw",
            "optionType":"float",
            "min":"-180",
            "max":"180"
        },
        "cam rz":{
            "desc":"Camera Roll", 
            "optionType":"float",
            "min":"-180",
            "max":"180"
        },
        "cam zoom":{
            "desc":"Camera Zoom",
            "optionType":"float",
            "min":"0",
            "max":"500000"
        },
        "set pt_fov":{
            "desc":"Camera FOV",
            "optionType":"float",
            "min":"0",
            "max":"360"
        },
        "cam x":{
            "desc":"Camera X",
            "optionType":"float",
            "min":"-10000",
            "max":"10000"
        },
        "cam y":{
            "desc":"Camera Y",
            "optionType":"float",
            "min":"-10000",
            "max":"10000"
        },
        "cam z":{
            "desc":"Camera Z",
            "optionType":"float",
            "min":"-10000",
            "max":"10000"
        },
        "set pt_fix_focus 1 | set pt_dof":{
            "desc":"Aperture",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_blade_rot":{
            "desc":"Blade Rotation",
            "optionType":"float",
            "min":"-180",
            "max":"180"
        },
        "set pt_expo":{
            "desc":"Exposure",
            "optionType":"float",
            "min":"0",
            "max":"16"
        },
        "set pt_bloom_mix":{
            "desc":"Bloom Mix",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_bloom_sca":{
            "desc":"Bloom Size",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_bloom_asp":{
            "desc":"Bloom Aspect Ratio",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_bloom_thr":{
            "desc":"Bloom Threshold",
            "optionType":"float",
            "min":"0",
            "max":"100"
        },
        "set pt_sun_p":{
            "desc":"Sun pitch",
            "optionType":"float",
            "min":"-90",
            "max":"90"
    },
        "set pt_sun_y":{
            "desc":"Sun yaw",
            "optionType":"float",
            "min":"0",
            "max":"360"
        },
        "set pt_sun_area":{
            "desc":"Sun area",
            "optionType":"float",
            "min":"0",
            "max":"100"
        },
        "set pt_isun":{
            "desc":"Sun intensity",
            "optionType":"float",
            "min":"0",
            "max":"500"
        },
        "set pt_isky":{
            "desc":"Sky intensity - Uniform mode only",
            "optionType":"float",
            "min":"0",
            "max":"500"
        },
        "set pt_ray_d":{
            "desc":"Rayleight - Atmosphere only",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_mie_d":{
            "desc":"Mie - Atmosphere only",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_o3_d":{
            "desc":"Ozone - Atmosphere only",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_mie_g":{
            "desc":"Mie Scattering - Atmosphere only",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_ibl_i":{
            "desc":"IBL Intensity - IBL mode only",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_ibl_rot":{
            "desc":"IBL Rotation - IBL mode only",
            "optionType":"float",
            "min":"0",
            "max":"360"
        },
        "set pt_fog_et":{
            "desc":"Fog Density",
            "optionType":"float",
            "min":"0",
            "max":"5000"
        },
        "set pt_fog_eg":{
            "desc":"Fog Phase",
            "optionType":"float",
            "min":"-0.9",
            "max":"0.9"
        },
    },
    "option": {
        "frames":{
            "desc":"Frames Amount",
            "optionType":"int",
            "min":"1",
            "max":"100000",
            "default":100
        },
            "secondsperrender":{
            "optionType":"float",
            "desc":"Seconds per Frame",
            "min":"0",
            "max":"1000000",
            "default":10
        },
        "direction":{
            "desc":"Animation direction - Clockwise / Counterclockwise",
            "optionType":"booltext",
            "tooltip":"This only applies for camera yaw",
            "on":"clockwise",
            "off":"counterclockwise"
        },
        "interpolation": {
            "desc":"Interpolation for camera path - linear/bezier",
            "optionType":"booltext",
            "on":"bezier",
            "off":"linear"
        },
        "sequence":{
            "desc":"Add Keyframe to squence - Hover for more infos",
            "optionType":"bool",
            "default":False,
            "tooltip":"Enable this to add keyframe to sequence, enables you to create a longer camera path (works only with bezier).\nExample Without: a -> b b -> c c -> d \nExample With:    a -> b -> c -> d\nWatch the timeline below"
        },
    },
    "global": {
        "saverenders":{
            "desc":"Save rendered frames",
            "optionType":"bool",
            "default":True
            }
        },
    "animation": {
        "enable animation":{
            "desc":"Enable animation",
            "optionType":"bool"
            
        },
        "loop":{
            "desc":"Loop animation - Frames will always loop back to 0",
            "optionType":"bool",
        },
        "startframe":{
            "desc":"Starting Frame",
            "optionType":"int",
            "min":"0",
            "max":"120",
        },
        "endframe":{
            "desc":"Ending Frame - Starts looping from",
            "optionType":"int",
            "min":"0",
            "max":"120"
        }
       # "animationStep":{
       #    "optionType":"int",
       # }
    }
}


def writeJson():
    global config
    with open('config.json', 'w') as outfile:
        json.dump(config, outfile)


def readJson():
    global config
    try:
        with open('config.json') as json_file:
            config = json.load(json_file)
            #print("Config loaded")
    except: "File empty or not found"

########################################################################################################################
#Config functionality 
def deleteParamterButton(callback,data,userdata):
    delparam = userdata[0]
    callbackdata = userdata[1]
    keyframeNum = int(callbackdata[0])
    paramKey = callbackdata[1]
    paramValue = callbackdata[2]
    paramType = callbackdata[3]

    dpg.delete_item(delparam)
    #print(keyframeNum,paramKey,paramType)
    removeConfig(keyframeNum,paramKey,paramType)

def removeConfig(keyframe,param,attribute):
    global config
    if attribute == "keyframe":
        del config["keyframe"][keyframe]
    elif attribute == "param":
        del config["keyframe"][keyframe]["param"][param]
    updateTimeLine()

def fillConfig(keyframe,param,value,attribute):
    #keyframe = Number of keyframe
    #param = Parameter to be changed
    #value = Value to be changed to
    #attribute = "option" "animation" "param" "global"
    global config
    #print("Write to config")
    #print(keyframe,param,value,attribute)
    if attribute == "global":
        if "Global" not in config:
            config["global"] = {}
            config["global"]["saverenders"] = "true"
        config["global"][param] = value
    else: 
        keyframe = int(keyframe)
        try:
            if "param" not in config["keyframe"][keyframe] and keyframe != "":
                pass
        except: 
            config["keyframe"].append({})
            config["keyframe"][keyframe]["param"] = {}
            config["keyframe"][keyframe]["option"] = {}
            config["keyframe"][keyframe]["animation"] = {}
            config["global"] = {}
            config["global"]["saverenders"] = "true"

        if attribute == "param":
            config["keyframe"][keyframe]["param"][param] = value
        elif attribute == "option":
            config["keyframe"][keyframe]["option"][param] = value
        elif attribute == "animation":
            config["keyframe"][keyframe]["animation"][param] = value

    if param == "squence" or param == "frames" or param == "interpolation":
        updateTimeLine()
    if param == "secondsperrender":
        updateStats()


def writeToConfig(callback,data,userdata):
    #fillConfig(keyframe,param,value,attribute):
    keyframe = userdata[0]
    param = userdata[1]
    value = data #user input
    attribute = userdata[3]

    #print(userdata)
    #print("Write to config " + str(keyframe) + " " + str(param) + " " + str(value) + " " + str(attribute))
    fillConfig(keyframe,param,value,attribute)

########################################################################################################################
#Tab functionality 

def deleteTabButton(callback,data,userdata):
    global config
    keyframeTotalAmount = len(config["keyframe"])-1         #len starts counting from 1 instead of 0 
    deleteKeyframe = "keyframe:"+str(keyframeTotalAmount)  #keyframe + last keyframe number = keyframe:1 
    #print("Delete keyframe: " + deleteKeyframe)
    if dpg.does_alias_exist(deleteKeyframe) == True:
        dpg.delete_item(deleteKeyframe)
        removeConfig(keyframeTotalAmount,"","keyframe")

def addNewTabButton(callback,data):
    global config
    #print(len(config["keyframe"]))
    if len(config["keyframe"]) == 0:
        fillConfig(0,"","","keyframe")
        #print("Add new keyframe: " + "keyframe:0")
    else:
        fillConfig(len(config["keyframe"]),"","","keyframe")  

    for i in range(len(config["keyframe"])):
        nextkeyframe = str(i)
        if dpg.does_alias_exist("keyframe:"+nextkeyframe) == False:
            #print("Create new keyframe tab button")
            dpg.add_tab(label="keyframe: "+nextkeyframe,tag="keyframe:"+nextkeyframe,parent="keyframe_bar")
            with dpg.child_window(width=900, height=800,parent="keyframe:"+nextkeyframe,no_scrollbar=True):
                with dpg.group(horizontal=True, width=0):
                    with dpg.child_window(width=600, height=790):
                        with dpg.child_window(autosize_x=True,height=160):
                            dpg.add_text("Keyframe options")
                            dpg.add_separator()
                            for mvcommand,value in magicavoxel_paramters["option"].items():
                                mvcommand = str(mvcommand)
                                translateNewParam("","",(nextkeyframe,mvcommand,value,"option"))
                                #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                        with dpg.child_window(autosize_x=True,height=140):
                            dpg.add_text("Keyframe Animation options")
                            dpg.add_separator()
                            for mvcommand,value in magicavoxel_paramters["animation"].items():
                                mvcommand = str(mvcommand)
                                translateNewParam("","",(nextkeyframe,mvcommand,value,"animation"))
                                #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                        with dpg.child_window(autosize_x=True,height=700 ,tag="window:param:"+nextkeyframe):
                            dpg.add_text("Parameters")
                            dpg.add_separator()
                    with dpg.child_window(width=300, height=800,tag="window:infos:"+nextkeyframe):
                        #This is the top right window
                        with dpg.child_window(label="Parameters",tag="window:paramselection"+nextkeyframe,parent="window:infos:"+nextkeyframe,height=450):
                            with dpg.tab_bar(label="param_bar",tag="param_bar:"+nextkeyframe,parent="window:paramselection"+nextkeyframe):
                                dpg.add_tab(label="Camera",tag="camera_tab:"+nextkeyframe,parent="param_bar:"+nextkeyframe)
                                dpg.add_tab(label="Light",tag="light_tab:"+nextkeyframe,parent="param_bar:"+nextkeyframe)
                                for mvcommand,value in magicavoxel_paramters["light"].items():
                                    #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                                    mvcommand = str(mvcommand)
                                    dpg.add_button(label=value["desc"],tag="param_button:"+mvcommand+":"+nextkeyframe,parent="light_tab:"+nextkeyframe,callback=translateNewParam,user_data=(nextkeyframe,mvcommand,value,"param"))
                                for mvcommand,value in magicavoxel_paramters["camera"].items():
                                    #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                                    mvcommand = str(mvcommand)
                                    dpg.add_button(label=value["desc"],tag="light_button:"+mvcommand+":"+nextkeyframe,parent="camera_tab:"+nextkeyframe,callback=translateNewParam,user_data=(nextkeyframe,mvcommand,value,"param"))
                        with dpg.child_window(label="Statistics",tag="window:statistics"+nextkeyframe,parent="window:infos:"+nextkeyframe,height=350):
                            dpg.add_text("Statistics")
                            dpg.add_separator()
            
            if i != 0:
                sync(i)
    updateTimeLine()

def sync(keyframe):
    global config
    for attribute, mvcommands in config["keyframe"][keyframe-1].items():
        for param, value in config["keyframe"][keyframe-1][attribute].items():
            mvdictvalue = magicavoxel_paramters[attribute][param]
            #print("Attribute: " + attribute + " Param: " + param + " Value: " + str(value))
            translateNewParam("","",(keyframe,param,mvdictvalue,attribute,value))

def translateNewParam(callback,data,userdata):
    global setup
    global config 
    #Userdata 0 = keyframe num
    #Userdata 1 = param name/key 
    #Userdata 2 = param value
    #Userdata 3 = attribute



    keyframeNum = str(userdata[0])
    paramKey = str(userdata[1])
    paramValue = str(userdata[2])
    paramType = str(userdata[3])
    tagKey = "input:"+paramKey+":"+keyframeNum
    parentKey = "window:"+paramType+":"+keyframeNum
    labelName = magicavoxel_paramters[paramType][paramKey]["desc"]
    keyType = magicavoxel_paramters[paramType][paramKey]["optionType"]
    callbackData = (keyframeNum,paramKey,paramValue,paramType)
    if keyType == "float" or keyType ==  "int":
        maxValue = float(magicavoxel_paramters[paramType][paramKey]["max"])
        minValue = float(magicavoxel_paramters[paramType][paramKey]["min"])

    #if userdata[2]["default"] exists then use it
    if len(userdata) == 5:
        value = userdata[4]
    else:
        if "default" in userdata[2]:
            value = userdata[2]["default"]
        else:
            if keyType == "float" or keyType ==  "int":
                value = 0
            elif keyType == "bool":
                value = False
            else: 
                value = ""
    if keyType == "booltext":
        value = magicavoxel_paramters[paramType][paramKey]["off"]

    if callback == "init" or callback == "animation":
        if paramType in config["keyframe"][int(keyframeNum)]:
            value = config["keyframe"][int(keyframeNum)][paramType][paramKey]
    if callback == "globalinit" and "global" in config:
        if paramKey in config["global"]:
            value = config["global"][paramKey]


    if dpg.does_alias_exist(tagKey) != True:
        fillConfig(keyframeNum,paramKey,value,paramType)
        if paramKey == "sequence":
            with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                dpg.add_checkbox(tag=tagKey,label=labelName,parent="group:"+tagKey,default_value=value,callback=changeInterpol,user_data=callbackData)
                
        elif keyType == "float":
            with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                #dpg.add_image_button(texture_tag="trashImg",width=13,height=13,callback=deleteParamterButton,user_data=("group:"+tagKey,callbackData))
                dpg.add_input_float(tag=tagKey,label=labelName,max_value=maxValue,default_value=value,min_value=minValue,max_clamped=True,min_clamped=True,parent="group:"+tagKey,callback=writeToConfig,user_data=callbackData,width=200)
        elif keyType == "int":
            with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                #dpg.add_image_button(texture_tag="trashImg",width=13,height=13,callback=deleteParamterButton,user_data=("group:"+tagKey,callbackData))
                dpg.add_input_int(tag=tagKey,label=labelName,max_value=maxValue,default_value=value,min_value=minValue,max_clamped=True,min_clamped=True,parent="group:"+tagKey,callback=writeToConfig,user_data=callbackData,width=200)
        elif keyType == "bool":
            with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                #dpg.add_image_button(texture_tag="trashImg",width=13,height=13,callback=deleteParamterButton,user_data=("group:"+tagKey,callbackData))
                dpg.add_checkbox(tag=tagKey,label=labelName,parent="group:"+tagKey,default_value=bool(value),callback=writeToConfig,user_data=callbackData)
        elif keyType == "string":
            with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                #dpg.add_image_button(texture_tag="trashImg",width=13,height=13,callback=deleteParamterButton,user_data=("group:"+tagKey,callbackData))
                dpg.add_input_text(tag=tagKey,label=labelName,parent="group:"+tagKey,default_value=value,callback=writeToConfig,user_data=callbackData,width=200)
        elif keyType == "booltext":
            with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                #dpg.add_image_button(texture_tag="trashImg",width=13,height=13,callback=deleteParamterButton,user_data=("group:"+tagKey,callbackData))
                dpg.add_button(tag=tagKey,label=value,parent="group:"+tagKey,callback=changeText,user_data=callbackData)
                dpg.add_text(labelName,tag="infotext:"+tagKey,parent="group:"+tagKey)
        
        if paramType == "param":
            dpg.add_button(label="Del",width=35,height=19,callback=deleteParamterButton,user_data=("group:"+tagKey,callbackData),parent="group:"+tagKey,before=tagKey)

        if "tooltip" in userdata[2]:
            with dpg.tooltip(tag="tooltip:"+tagKey,parent=tagKey):
                dpg.add_text(userdata[2]["tooltip"],parent="tooltip:"+tagKey)
                
def changeInterpol(callback,data,userdata):
    global config
    keyframeNum = str(userdata[0])
    paramKey = str(userdata[1])
    paramValue = str(userdata[2])
    paramType = str(userdata[3])
    tagKey = "input:interpolation:"+keyframeNum

    #print(data)
    #print(keyframeNum)
    if data == True:
        fillConfig(keyframeNum,"interpolation","bezier","option")
        fillConfig(keyframeNum,paramKey,data,"option")
        dpg.disable_item(tagKey)
        dpg.set_item_label(tagKey,"bezier")
    if data == False:
        fillConfig(keyframeNum,"interpolation","linear","option")
        fillConfig(keyframeNum,paramKey,data,"option")
        dpg.enable_item(tagKey)
        dpg.set_item_label(tagKey,"linear")
    updateTimeLine()

def changeText(callback,data,userdata):
    global config
    keyframeNum = str(userdata[0])
    paramKey = str(userdata[1])
    paramValue = str(userdata[2])
    paramType = str(userdata[3])
    offValue = magicavoxel_paramters[paramType][paramKey]["off"]
    onValue = magicavoxel_paramters[paramType][paramKey]["on"]
    tagKey = "input:"+paramKey+":"+keyframeNum


    if dpg.get_item_label(tagKey) == offValue:
        value = onValue
        dpg.set_item_label(item=tagKey,label=value)
    else:
        value = offValue
        dpg.set_item_label(item=tagKey,label=value)

    #print(keyframeNum,paramKey,value,paramType)
    fillConfig(keyframeNum,paramKey,value,paramType)


########################################################################################################################
def initialize():
   
    #print("uga")
    for i in range(len(config["keyframe"])):
        nextkeyframe = str(i)
        if dpg.does_alias_exist("keyframe:"+nextkeyframe) == False:
            #print("Create new keyframe tab button")
            dpg.add_tab(label="keyframe: "+nextkeyframe,tag="keyframe:"+nextkeyframe,parent="keyframe_bar")
            with dpg.child_window(width=900, height=800,parent="keyframe:"+nextkeyframe,no_scrollbar=True):
                with dpg.group(horizontal=True, width=0):
                    with dpg.child_window(width=600, height=790):
                        with dpg.child_window(autosize_x=True,height=160):
                            dpg.add_text("Keyframe options")
                            dpg.add_separator()
                            for mvcommand,dictval in magicavoxel_paramters["option"].items():
                                mvcommand = str(mvcommand)
                                value = config["keyframe"][int(nextkeyframe)]["option"][mvcommand]
                                translateNewParam("init","",(nextkeyframe,mvcommand,dictval,"option",value))
                                #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
 
                        with dpg.child_window(autosize_x=True,height=140):
                            dpg.add_text("Keyframe Animation options")
                            dpg.add_separator()
                            for mvcommand,dictvalue in magicavoxel_paramters["animation"].items():
                                mvcommand = str(mvcommand)
                                value = config["keyframe"][int(nextkeyframe)]["animation"][mvcommand]
                                translateNewParam("init","",(nextkeyframe,mvcommand,dictvalue,"animation",value))
                                #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                        with dpg.child_window(autosize_x=True,height=700 ,tag="window:param:"+nextkeyframe):
                            dpg.add_text("Parameters")
                            dpg.add_separator()
                    with dpg.child_window(width=300, height=800,tag="window:infos:"+nextkeyframe):
                        #This is the top right window
                        with dpg.child_window(label="Parameters",tag="window:paramselection"+nextkeyframe,parent="window:infos:"+nextkeyframe,height=450):
                            with dpg.tab_bar(label="param_bar",tag="param_bar:"+nextkeyframe,parent="window:paramselection"+nextkeyframe):
                                dpg.add_tab(label="Camera",tag="camera_tab:"+nextkeyframe,parent="param_bar:"+nextkeyframe)
                                dpg.add_tab(label="Light",tag="light_tab:"+nextkeyframe,parent="param_bar:"+nextkeyframe)
                                for mvcommand,value in magicavoxel_paramters["light"].items():
                                    #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                                    mvcommand = str(mvcommand)
                                    dpg.add_button(label=value["desc"],tag="param_button:"+mvcommand+":"+nextkeyframe,parent="light_tab:"+nextkeyframe,callback=translateNewParam,user_data=(nextkeyframe,mvcommand,value,"param"))
                                for mvcommand,value in magicavoxel_paramters["camera"].items():
                                    #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                                    mvcommand = str(mvcommand)
                                    dpg.add_button(label=value["desc"],tag="light_button:"+mvcommand+":"+nextkeyframe,parent="camera_tab:"+nextkeyframe,callback=translateNewParam,user_data=(nextkeyframe,mvcommand,value,"param"))
                        with dpg.child_window(label="Statistics",tag="window:statistics"+nextkeyframe,parent="window:infos:"+nextkeyframe,height=350):
                            dpg.add_text("Statistics")
                            dpg.add_separator()
                            #print("what"+nextkeyframe)
    
    
        for mvcommand,value in config["keyframe"][i].items():
            #print("Create new param button")
            if mvcommand == "param":
                #print(value)
                for key,value in value.items():
                    translateNewParam("init",mvcommand,(nextkeyframe,key,"","param",value))
                        #Userdata 0 = keyframe num
                        #Userdata 1 = param name/key 
                        #Userdata 2 = param value
                        #Userdata 3 = attribute
    updateTimeLine()
########################################################################################################################
#TimeLine  

#Pretty clumsy but it works
def updateTimeLine():
    if dpg.does_alias_exist("timeline") == True:
        dpg.delete_item("timeline")
    offset = 20
    keyframenum = 0
    totalframes = 0
    issequence = False
    try:
        with dpg.group(parent="Third Window",horizontal=True,tag="timeline",show=False):
            with dpg.drawlist(width=3000, height=100,tag="drawlist"):  # or you could use dpg.add_drawlist and set parents manually
                while keyframenum < len(config["keyframe"])-1:
                    if "frames" in config["keyframe"][keyframenum]["option"] and "interpolation" in config["keyframe"][keyframenum]["option"] and "sequence" in config["keyframe"][keyframenum]["option"]:
                        if config["keyframe"][keyframenum]["option"]["interpolation"] == "linear" and not config["keyframe"][keyframenum]["option"]["sequence"] == True:
                            frameamount = config["keyframe"][keyframenum]["option"]["frames"]
                            issequence = False
                            textKey = keyframenum
                        elif config ["keyframe"][keyframenum]["option"]["interpolation"] == "bezier" and not config["keyframe"][keyframenum]["option"]["sequence"] == True:
                            frameamount = config["keyframe"][keyframenum]["option"]["frames"]
                            textKey = keyframenum
                            startKey = keyframenum 
                            if keyframenum+1 < len(config["keyframe"])-1:
                                if config["keyframe"][keyframenum+1]["option"]["sequence"] == True:
                                    while keyframenum <= len(config["keyframe"])-1 and config["keyframe"][keyframenum+1]["option"]["sequence"] == True:
                                        keyframenum += 1
                                        frameamount += config["keyframe"][keyframenum]["option"]["frames"]
                                        issequence = True
                                        textKey = str(startKey)+"-"+str(keyframenum)
                                        #print(keyframenum)
                                        if keyframenum+1 >= len(config["keyframe"])-1:
                                            break
                        else: 
                            frameamount = 0
                        for i in range(frameamount):
                            #print("keyframe:"+str(i))
                            if config["keyframe"][keyframenum]["option"]["interpolation"] == "linear" and issequence == False:
                                colour = (200,200,255,255)
                            elif config["keyframe"][keyframenum]["option"]["interpolation"] == "bezier" or issequence == True:
                                colour = (60,255,20,255)
                            else: 
                                colour = (255,0,0,255)
                            if i == 0:
                                colour = (255,255,0,255)
                            if i % 10 == 0:
                                if i == 0:
                                    dpg.draw_rectangle( pmin=(0+offset,30),     # top left corner 
                                                        pmax=(1+offset,75),     # bottom right corner
                                                        color=colour,thickness=1)
                                    dpg.add_text(str(i),pos=(offset+5,120),parent="timeline",)
                                    dpg.add_text("KeFr:"+str(textKey),pos=(offset+5,40),parent="timeline",)
                                elif i % 25 == 0:
                                        dpg.draw_rectangle( pmin=(0+offset,35),     # top left corner 
                                                            pmax=(1+offset,70),     # bottom right corner
                                                            color=colour,thickness=1)
                                        dpg.add_text(str(i),pos=(offset+5,120),parent="timeline",)
                                else:
                                    dpg.draw_rectangle( pmin=(0+offset,40),     # top left corner 
                                                        pmax=(1+offset,65),     # bottom right corner
                                                        color=colour,thickness=1,)
                                offset += 8
                        totalframes = frameamount + totalframes
                    

                        keyframenum = keyframenum + 1
            dpg.add_text(str("End Frame total: "+str(totalframes)),pos=(offset+10,78),parent="timeline",)
            dpg.show_item("timeline")
            #if offset under 950 width = 950 if offset larger than 950 width = offset
    except KeyError:
        pass
    if offset > 950:
        dpg.set_item_width("timeline",offset+200)
        dpg.set_item_width("drawlist",offset+200)
    else:
        dpg.set_item_width("timeline",950)
        dpg.set_item_width("drawlist",offset+200)
            #calculate bounding box
    updateStats()
                      
def updateStats():
    totaltime = 0
    try:
        for i in range(len(config["keyframe"])):
            if "secondsperrender" in config["keyframe"][i]["option"]:
                totaltime = round((config["keyframe"][i]["option"]["frames"]*(config["keyframe"][i]["option"]["secondsperrender"]+2))/60 + totaltime)
            else:
                return 
        for i in range(len(config["keyframe"])):
            #print("yes"+str(i))
            if dpg.does_alias_exist("statistics_group:"+str(i)) == True:
                dpg.delete_item("statistics_group:"+str(i))
            with dpg.group(tag="statistics_group:"+str(i),parent="window:statistics"+str(i)):
                dpg.add_text("Keyframe: "+str(i))
                dpg.add_text("Frames: "+str(config["keyframe"][i]["option"]["frames"]))
                dpg.add_text("Interpolation: "+str(config["keyframe"][i]["option"]["interpolation"]))
                dpg.add_text("In Sequence: "+str(config["keyframe"][i]["option"]["sequence"]))
                estimate = round((config["keyframe"][i]["option"]["frames"]*(config["keyframe"][i]["option"]["secondsperrender"]+2))/60)
                dpg.add_text("Keyframe rendertime: "+str(estimate) + " minutes")
                dpg.add_separator()
                dpg.add_text("Total animation time: "+str(totaltime)+" minutes")
                dpg.add_separator()
    except KeyError:
        pass
  #        params = []
  #        lenght = []
  #        for keyframe in range(len(config["keyframe"])):
  #            params = []
  #            for param,value in config["keyframe"][keyframe]["param"].items():
  #                if param not in params:
  #                    params.append(param)
  #                    lenght.append(len(param))
  #        if 
  #        dpg.add_text("Parameters:"+str(lenght[i]))
  #        print(params)

########################################################################################################################
#help
def gethelp(callback,data):
    with dpg.window(label="Help",tag="help",width=200,height=400):
        dpg.add_text("How does this work?")


########################################################################################################################
dpg.create_context()

#look for trash.png in the same directory as this script and in ui folder
#dpg.load_image("trash.png")
#  try: 
#      path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui', 'trash.png'))
#
#      width, height, channels, data = dpg.load_image(path)
#      with dpg.texture_registry(show=False):
#          dpg.add_static_texture(width, height, data, tag="trashImg")
#  except TypeError:
#      print("script was looking for in:"+path)
#      print("Ui not found, make sure the ui folder is in the same directory as this script")
#      exit()
readJson()

with dpg.viewport_menu_bar():
    with dpg.menu(label="SAVE"):
        dpg.add_menu_item(label="Save",callback=writeJson)
    #with dpg.menu(label="HELP"):
    #    dpg.add_menu_item(label="What am I doing?",callback=gethelp)




with dpg.window(tag="Primary Window",label="Config Generator",menubar=True):
    with dpg.child_window(label="Global Settings",tag="window:global",height=70):
        #global settings
        dpg.add_text("Global Settings")
        dpg.add_separator()
        for mvcommand,value in magicavoxel_paramters["global"].items():
            mvcommand = str(mvcommand)
            translateNewParam("globalinit","",("",mvcommand,value,"global"))
    with dpg.child_window(tag="Second Window",parent="Primary Window",height=750,no_scrollbar=True):
        with dpg.tab_bar(label="keyframe_bar",tag="keyframe_bar"):    
            dpg.add_tab_button(label="+",tag="add",trailing=True,callback=addNewTabButton)
            dpg.add_tab_button(label="-",tag="remove",trailing=True,callback=deleteTabButton)
    with dpg.child_window(tag="Third Window",height=150,parent="Primary Window",width=950):
        dpg.add_text("Timeline")
        dpg.add_separator()
    
if config["keyframe"] != []:
    initialize()


#dpg.show_documentation()
dpg.set_primary_window("Primary Window", True)
dpg.create_viewport(width=950, height=1100 ,title="Config Generator  |  Dima's Voxel")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

