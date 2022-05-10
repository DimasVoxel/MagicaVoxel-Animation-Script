from copy import deepcopy
import json
import dearpygui.dearpygui as dpg

global config 
config = {}
config["keyframe"] = []
global setup
setup =False
global tabpos
tabpos = {}
configVersion = 3

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
        "set pt_fix_focus 1 | set pt_focus":{
            "desc":"Focus",
            "optionType":"float",
            "min":"0",
            "max":"9999.9"
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
            "set pt_fix_focus 1 | set pt_focus":{
            "desc":"Focus",
            "optionType":"float",
            "min":"0",
            "max":"9999.9"
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
        "interpolation": {
            "desc":"Interpolation for camera path - linear/bezier",
            "optionType":"select",
            "options":["linear","bezier","bezier-sequence"],
            "default":"linear"
        },
        "direction":{
            "desc":"Animation direction - Clockwise / Counterclockwise",
            "optionType":"select",
            "tooltip":"This only applies for camera yaw",
            "options":["Clockwise","Counterclockwise"],
            "default":"Clockwise"
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

    tabpos = {}
    count = 0
    info = dpg.get_item_info("keyframe_bar")
    for child in info["children"][1]:
        if "keyframe" in dpg.get_item_alias(child):
            pos = dpg.get_item_rect_max(child)
            tag = dpg.get_item_alias(child)
            tag = tag.replace("keyframe:","")
            tabpos[pos[0]] = int(tag)

    tabpos = sorted(tabpos.items())
    configbak = deepcopy(config)
    for i in range(len(tabpos)):
        #reorder keyframes in config
        if tabpos[i][1] != i:
            config["keyframe"][i],config["keyframe"][tabpos[i][1]] = configbak["keyframe"][tabpos[i][1]],configbak["keyframe"][i]


    config["version"] = {}
    config["version"] = configVersion

    with open('config.json', 'w') as outfile:
        json.dump(config, outfile)

    if dpg.does_item_exist("keyframe_bar") == True:
        dpg.delete_item("keyframe_bar")

    config = {}
    config["keyframe"] = []
    readJson()
    rebuild()


def readJson():
    global config
    try:
        with open('config.json') as json_file:
            config = json.load(json_file)
            #print("Config loaded")
    except: "File empty or not found"

def readMagicaCam():

    with dpg.file_dialog(directory_selector=False, show=True, id="file_dialog_id",height=600):
       
        dpg.add_file_extension("", color=(150, 255, 150, 255))
        dpg.add_file_extension(".txt", color=(255, 0, 255, 255), custom_text="[header]")
        dpg.add_file_extension(".*")



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

def tabOrder():
    if dpg.does_item_exist("keyframe_bar") == True:
        global config
        global tabpos
        tabpos = {}
        count = 0
        info = dpg.get_item_info("keyframe_bar")
        for child in info["children"][1]:
            if "keyframe" in dpg.get_item_alias(child):
                pos = dpg.get_item_rect_max(child)
                tag = dpg.get_item_alias(child)
                tag = tag.replace("keyframe:","")
                tabpos[pos[0]] = int(tag)

        tabpos = sorted(tabpos.items())


def deleteTabButton(callback,data,userdata):
    global config
    try:
        KeyFrameNum = len(config["keyframe"])-1         #len starts counting from 1 instead of 0 
        deleteKeyframe = "keyframe:"+str(KeyFrameNum)  #keyframe + last keyframe number = keyframe:1 
    except TypeError:
        pass
    #else:
     #   deleteKeyframe = userdata[0]
     #   KeyFrameNum = userdata[1]
    
    #print("Delete keyframe: " + deleteKeyframe)
    if dpg.does_alias_exist(deleteKeyframe) == True:
        dpg.delete_item(deleteKeyframe)
        removeConfig(KeyFrameNum,"","keyframe")

def addNewTabButton(callback,data):
    global config
    #print(len(config["keyframe"]))
    if len(config["keyframe"]) == 0:
        fillConfig(0,"","","keyframe")
        #print("Add new keyframe: " + "keyframe:0")
    else:
        fillConfig(len(config["keyframe"]),"","","keyframe")  

    rebuild()
    newtab = "keyframe:"+str(len(config["keyframe"])-1)
    dpg.set_value("keyframe_bar",newtab)
    
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

    if keyType == "select":
        selval = magicavoxel_paramters[paramType][paramKey]["options"]
    
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
                
        if keyType == "float":
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
        elif keyType == "select":
            with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                dpg.add_combo(items=selval,tag=tagKey,label=labelName,parent="group:"+tagKey,default_value=value,callback=writeToConfig,user_data=callbackData,width=200)
        
        if paramType == "param":
            dpg.add_button(label="Del",width=35,height=19,callback=deleteParamterButton,user_data=("group:"+tagKey,callbackData),parent="group:"+tagKey,before=tagKey)

        if "tooltip" in userdata[2]:
            with dpg.tooltip(tag="tooltip:"+tagKey,parent=tagKey):
                dpg.add_text(userdata[2]["tooltip"],parent="tooltip:"+tagKey)
                



########################################################################################################################
#main
def rebuild():
    global config
    global tabpos
    currenttab = ""

    if dpg.does_item_exist("keyframe_bar") == True:
        tabOrder()
        currenttab = dpg.get_value("keyframe_bar")
        dpg.delete_item("keyframe_bar")
   
    
    with dpg.tab_bar(label="keyframe_bar",tag="keyframe_bar",parent="Second Window",reorderable=True,track_offset=True):
        dpg.add_tab_button(label="+",tag="add",trailing=True,callback=addNewTabButton)
        dpg.add_tab_button(label="-",tag="remove",trailing=True,callback=deleteTabButton)
    
    for i in range(len(config["keyframe"])):
        if len(tabpos) > i and len(tabpos) != 0:
            intnextkeyframe = tabpos[i][1]
            strnextkeyframe = str(tabpos[i][1])
        else:
            intnextkeyframe = i
            strnextkeyframe = str(i)
       # print(strnextkeyframe+"thiaosda")
       # print(tabpos)

        if dpg.does_alias_exist("keyframe:"+strnextkeyframe) == False:
            #print("Create new keyframe tab button")
            dpg.add_tab(label=strnextkeyframe+" Keyframe",tag="keyframe:"+strnextkeyframe,parent="keyframe_bar",track_offset=True,tracked=True)
            #with dpg.popup(tag="tooltip:"+"keyframe:"+strnextkeyframe,parent="keyframe:"+strnextkeyframe,modal=True):
            #    dpg.add_text("Options")
            #    dpg.add_separator()
            #    dpg.add_button(label="Delete",callback=deleteTabButton,user_data="keyframe:"+strnextkeyframe)
            #   # dpg.add_button("Copy",callback=copyKeyframeButton,user_data=("keyframe:"+strnextkeyframe))
            with dpg.child_window(width=900, height=800,parent="keyframe:"+strnextkeyframe,no_scrollbar=True):
                with dpg.group(horizontal=True, width=0):
                    with dpg.child_window(width=600, height=790):
                        with dpg.child_window(autosize_x=True,height=160):
                            dpg.add_text("Keyframe options")
                            dpg.add_separator()
                            for mvcommand,dictval in magicavoxel_paramters["option"].items():
                                mvcommand = str(mvcommand)
                                if mvcommand in config["keyframe"][intnextkeyframe]["option"]:
                                    value = config["keyframe"][intnextkeyframe]["option"][mvcommand]
                                    translateNewParam("init","",(intnextkeyframe,mvcommand,dictval,"option",value))
                                else:
                                    translateNewParam("","",(intnextkeyframe,mvcommand,dictval,"option"))
                                #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                        with dpg.child_window(autosize_x=True,height=140):
                            dpg.add_text("Keyframe Animation options")
                            dpg.add_separator()
                            for mvcommand,dictvalue in magicavoxel_paramters["animation"].items():
                                mvcommand = str(mvcommand)
                                if mvcommand in config["keyframe"][intnextkeyframe]["animation"]:
                                    value = config["keyframe"][intnextkeyframe]["animation"][mvcommand]
                                    translateNewParam("init","",(intnextkeyframe,mvcommand,dictvalue,"animation",value))
                                else:
                                    translateNewParam("","",(intnextkeyframe,mvcommand,dictvalue,"animation"))
                                #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                        with dpg.child_window(autosize_x=True,height=700 ,tag="window:param:"+strnextkeyframe):
                            dpg.add_text("Parameters")
                            dpg.add_separator()
                    with dpg.child_window(width=300, height=800,tag="window:infos:"+strnextkeyframe):
                        #This is the top right window
                        with dpg.child_window(label="Parameters",tag="window:paramselection"+strnextkeyframe,parent="window:infos:"+strnextkeyframe,height=450):
                            with dpg.tab_bar(label="param_bar",tag="param_bar:"+strnextkeyframe,parent="window:paramselection"+strnextkeyframe):
                                dpg.add_tab(label="Camera",tag="camera_tab:"+strnextkeyframe,parent="param_bar:"+strnextkeyframe)
                                dpg.add_tab(label="Light",tag="light_tab:"+strnextkeyframe,parent="param_bar:"+strnextkeyframe)
                                for mvcommand,value in magicavoxel_paramters["light"].items():
                                    #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                                    mvcommand = str(mvcommand)
                                    dpg.add_button(label=value["desc"],tag="param_button:"+mvcommand+":"+strnextkeyframe,parent="light_tab:"+strnextkeyframe,callback=translateNewParam,user_data=(intnextkeyframe,mvcommand,value,"param"))
                                for mvcommand,value in magicavoxel_paramters["camera"].items():
                                    #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                                    mvcommand = str(mvcommand)
                                    dpg.add_button(label=value["desc"],tag="light_button:"+mvcommand+":"+strnextkeyframe,parent="camera_tab:"+strnextkeyframe,callback=translateNewParam,user_data=(intnextkeyframe,mvcommand,value,"param"))
                        with dpg.child_window(label="Statistics",tag="window:statistics:"+strnextkeyframe,parent="window:infos:"+strnextkeyframe,height=350):
                            dpg.add_text("Statistics")
                            dpg.add_separator()
                            #print("what"+nextkeyframe)
    
    
        for mvcommand,value in config["keyframe"][intnextkeyframe].items():
            #print("Create new param button")
            if mvcommand == "param":
                #print(value)
                for key,value in value.items():
                    translateNewParam("init",mvcommand,(intnextkeyframe,key,"","param",value))
                        #Userdata 0 = keyframe num
                        #Userdata 1 = param name/key 
                        #Userdata 2 = param value
                        #Userdata 3 = attribute
    
        if intnextkeyframe != 0:
            sync(intnextkeyframe)
    #print(currenttab)
    if dpg.does_item_exist(currenttab) == True:
        #print("Set current tab to: "+currenttab)
        dpg.set_value("keyframe_bar",currenttab)

    updateStats()

########################################################################################################################
#TimeLine  

#Pretty clumsy but it works
def updateTimeLine():
    global tabpos

    if dpg.does_alias_exist("timeline") == True:
        dpg.delete_item("timeline")
    offset = 20
    totalframes = 0

    try:
        with dpg.group(parent="Third Window",horizontal=True,tag="timeline",show=False):
            with dpg.drawlist(width=3000, height=100,tag="drawlist"):  # or you could use dpg.add_drawlist and set parents manually
                for j in range(len(config["keyframe"])-1):
                    if len(tabpos) > j and len(tabpos) != 0:
                        keyframenum = tabpos[j][1]
                    else:
                        keyframenum = j
                    if "frames" in config["keyframe"][keyframenum]["option"] and "interpolation" in config["keyframe"][keyframenum]["option"]:
                        if config["keyframe"][keyframenum]["option"]["interpolation"] == "linear":
                            frameamount = config["keyframe"][keyframenum]["option"]["frames"]
                            textKey = keyframenum
                        elif config ["keyframe"][keyframenum]["option"]["interpolation"] == "bezier":#
                            frameamount = 0
                            textKey = keyframenum
                            startKey = keyframenum 
                            if keyframenum < len(config["keyframe"])-1:
                                frameamount = config["keyframe"][keyframenum]["option"]["frames"]
                                if config["keyframe"][keyframenum+1]["option"]["interpolation"] == "bezier-sequence":
                                    keyframenum += 1
                                    textKey = str(startKey)+"-"+str(keyframenum)
                                    while keyframenum < len(config["keyframe"])-1 and config["keyframe"][keyframenum+1]["option"]["interpolation"] == "bezier-sequence":
                                        keyframenum += 1
                                        j += 1
                                        frameamount += config["keyframe"][keyframenum]["option"]["frames"]
                                        textKey = str(startKey)+"-"+str(keyframenum)
                                        #print(keyframenum)
                                        if j+1 >= len(config["keyframe"])-1:
                                            break
                        else: 
                            frameamount = 0
                        for i in range(frameamount):
                            #print("keyframe:"+str(i))
                            if config["keyframe"][keyframenum]["option"]["interpolation"] == "linear":
                                colour = (200,200,255,255)
                            elif config["keyframe"][keyframenum]["option"]["interpolation"] == "bezier" or config["keyframe"][keyframenum]["option"]["interpolation"] == "bezier-sequence":
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
                
                dpg.draw_rectangle( pmin=(0+offset,30),     # top left corner 
                    pmax=(1+offset,75),     # bottom right corner
                    color=(255,255,0,255),thickness=1)
                dpg.add_text("KeFr:"+str(len(config["keyframe"])-1),pos=(offset+5,40),parent="timeline",)
                offset += 8

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
        for j in range(len(config["keyframe"])-1):
            if len(tabpos) > j and len(tabpos) != 0:
                keyframenum = tabpos[j][1]
            else:
                keyframenum = j

            if "secondsperrender" in config["keyframe"][keyframenum]["option"]:
                totaltime = round((config["keyframe"][keyframenum]["option"]["frames"]*(config["keyframe"][keyframenum]["option"]["secondsperrender"]+2))/60 + totaltime)
            else:
                return 



        for i in range(len(config["keyframe"])):

            if len(tabpos) > i and len(tabpos) != 0:
                keyframenum = tabpos[i][1]
            else:
                keyframenum = i
            #print("yes"+str(i))
            if config["keyframe"][i]["option"]["interpolation"] == "bezier-sequence":
                issequence = "True"
            else:
                issequence = "False"

            print("window:statistics:"+str(keyframenum)+"  "+str(dpg.does_item_exist("window:statistics:"+str(keyframenum))))
            if dpg.does_item_exist("window:statistics:"+str(keyframenum)) == False:
                break

            if dpg.does_alias_exist("statistics_group:"+str(keyframenum)) == True:
                dpg.delete_item("statistics_group:"+str(keyframenum))
                
            #print(str(keyframenum))


            with dpg.group(tag="statistics_group:"+str(keyframenum),parent="window:statistics:"+str(keyframenum)):
                dpg.add_text("Keyframe: "+str(keyframenum),parent="statistics_group:"+str(keyframenum))
                dpg.add_text("Frames: "+str(config["keyframe"][keyframenum]["option"]["frames"]),parent="statistics_group:"+str(keyframenum))
                if config["keyframe"][keyframenum]["option"]["interpolation"] == "bezier-sequence":
                    issequence = "True"
                else:
                    dpg.add_text("Interpolation: "+str(config["keyframe"][keyframenum]["option"]["interpolation"]),parent="statistics_group:"+str(keyframenum))
                    issequence = "False"
                
                dpg.add_text("In Sequence: "+ issequence,parent="statistics_group:"+str(keyframenum))
                estimate = round((config["keyframe"][keyframenum]["option"]["frames"]*(config["keyframe"][keyframenum]["option"]["secondsperrender"]+2))/60)
                dpg.add_text("Keyframe rendertime: "+str(estimate) + " minutes",parent="statistics_group:"+str(keyframenum))
                dpg.add_separator(parent="statistics_group:"+str(keyframenum))
                dpg.add_text("Total animation time: "+str(totaltime)+" minutes",parent="statistics_group:"+str(keyframenum))
                dpg.add_separator(parent="statistics_group:"+str(keyframenum))


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
    with dpg.window(label="Help",tag="help",width=500,height=600):
        dpg.add_text("How does this work?")
        dpg.add_separator()
        dpg.add_text("Each animation is made out of multimple keyframes \nand each keyframe holds information how certain values should look like.")



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
if config["version"] != configVersion:
    config = {}
    config["keyframe"] = []


with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Save",callback=writeJson)
       # with dpg.menu(label="Open"):
        #    dpg.add_menu_item(label="Import Magicavoxel Camera export",callback=readMagicaCam,tag="importMagicaCam")
  #  with dpg.menu(label="HELP"):
   #     dpg.add_menu_item(label="What am I doing?",callback=gethelp)




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
        with dpg.group(tag="timeline_group",horizontal=True):
            dpg.add_text("Timeline")
            dpg.add_button(label="Refresh timeline",tag="refresh",callback=updateTimeLine)
        dpg.add_separator()
    
if config["keyframe"] != []:
    rebuild()
    updateTimeLine()


#dpg.show_documentation()
dpg.set_primary_window("Primary Window", True)
dpg.create_viewport(width=950, height=1100 ,title="Config Generator  |  Dima's Voxel")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

