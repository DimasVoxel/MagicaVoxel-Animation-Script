
import json
import pprint
import os
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
        "set pt_dof":{
            "desc":"Aperture",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_fix_focus":{
            "desc":"Focus",
            "optionType":"float",
            "min":"0",
            "max":"9999"
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
        "set pt_dof":{
            "desc":"Aperture",
            "optionType":"float",
            "min":"0",
            "max":"1"
        },
        "set pt_fix_focus":{
            "desc":"Focus",
            "optionType":"float",
            "min":"0",
            "max":"9999"
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
            "desc":"Animation direction - Clockwise / Anticlockwise",
            "optionType":"string",
            "default":"Clockwise"
        },
        "interpolation": {
            "desc":"Interpolation for camera path - linear/bezier",
            "optionType":"string",
            "default":"linear"
        }
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
            "max":"120"
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

def main():
    global config

    fillConfig(0,"cam ry","65.9","param")
    fillConfig(0,"frames",100,"option")
    fillConfig(0,"direction","left","option")
    fillConfig(0,"secondsperrender",2,"option")
    fillConfig(0,"interpolation","linear","option")
    fillConfig(0,"loop","true","animation")
    fillConfig(0,"startframe","0","animation")
    fillConfig(0,"endframe","100","animation")
    fillConfig(1,"cam ry","65.9","param")
    fillConfig(1,"cam rx","65.9","param")
    fillConfig(1,"bla","123","param")
    fillConfig(1,"frames",100,"option")
    fillConfig(1,"direction","left","option")
    fillConfig(1,"secondsperrender",2,"option")
    fillConfig(1,"interpolation","linear","option")
    fillConfig(1,"loop","true","animation")
    fillConfig(1,"startframe","0","animation")
    fillConfig(1,"endframe","100","animation")
    fillConfig("","saverender","true","global")

    writeJson()

def readJson():
    global config
    try:
        with open('config.json') as json_file:
            config = json.load(json_file)
            #print("Config loaded")
    except: "File empty or not found"





#readJson()

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
    #updateTimeLine()

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
            with dpg.child_window(autosize_x=True, height=800,parent="keyframe:"+nextkeyframe,no_scrollbar=True):
                with dpg.group(horizontal=True, width=0):
                    with dpg.child_window(width=600, height=790):
                        with dpg.child_window(autosize_x=True,height=140):
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
                    with dpg.child_window(width=300, height=450):
                        #This is the top right window
                        with dpg.child_window(label="Parameters",tag="window:paramselection"+nextkeyframe):
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
            if i != 0:
                sync(i)

def sync(keyframe):
    global config
    for attribute, mvcommands in config["keyframe"][keyframe-1].items():
        for param, value in config["keyframe"][keyframe-1][attribute].items():
            mvdictvalue = magicavoxel_paramters[attribute][param]
            #print("Attribute: " + attribute + " Param: " + param + " Value: " + str(value))
            translateNewParam("","",(keyframe,param,mvdictvalue,attribute,value))

def translateNewParam(callback,data,userdata):
    global setup
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

    if dpg.does_alias_exist(tagKey) != True:
        if paramType == "param":
            #print("Fill with new param: "+keyframeNum+" "+paramKey+" "+paramValue+" "+paramType)
            fillConfig(keyframeNum,paramKey,value,paramType)
            if keyType == "float":
                with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                    dpg.add_image_button(texture_tag="trashImg",width=13,height=13,callback=deleteParamterButton,user_data=("group:"+tagKey,callbackData))
                    dpg.add_input_float(tag=tagKey,label=labelName,max_value=maxValue,default_value=value,min_value=minValue,max_clamped=True,min_clamped=True,parent="group:"+tagKey,callback=writeToConfig,user_data=callbackData,width=200)
            if keyType == "int":
                with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                    dpg.add_image_button(texture_tag="trashImg",width=13,height=13)
                    dpg.add_input_int(tag=tagKey,label=labelName,max_value=maxValue,default_value=value,min_value=minValue,max_clamped=True,min_clamped=True,parent="group:"+tagKey,callback=writeToConfig,user_data=callbackData,width=200)
            if keyType == "bool":
                with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                    dpg.add_image_button(texture_tag="trashImg",width=13,height=13)
                    dpg.add_checkbox(tag=tagKey,label=labelName,parent="group:"+tagKey,default_value=value,callback=writeToConfig,user_data=callbackData)
            if keyType == "string":
                with dpg.group(parent=parentKey,horizontal=True,tag="group:"+tagKey):
                    dpg.add_image_button(texture_tag="trashImg",width=13,height=13)
                    dpg.add_input_text(tag=tagKey,label=labelName,parent="group:"+tagKey,default_value=value,callback=writeToConfig,user_data=callbackData,width=200)
        else: 
            #print("Fill with new param: "+keyframeNum+" "+paramKey+" "+paramValue+" "+paramType)
            fillConfig(keyframeNum,paramKey,value,paramType)
            if keyType == "float":
                dpg.add_input_float(tag=tagKey,label=labelName,max_value=maxValue,default_value=value,min_value=minValue,max_clamped=True,min_clamped=True,parent=parentKey,callback=writeToConfig,user_data=callbackData,width=200)
            if keyType == "int":
                dpg.add_input_int(tag=tagKey,label=labelName,max_value=maxValue,default_value=value,min_value=minValue,max_clamped=True,min_clamped=True,parent=parentKey,callback=writeToConfig,user_data=callbackData,width=200)
            if keyType == "bool":
                dpg.add_checkbox(tag=tagKey,label=labelName,parent=parentKey,default_value=value,callback=writeToConfig,user_data=callbackData)
            if keyType == "string":
                dpg.add_input_text(tag=tagKey,label=labelName,parent=parentKey,default_value=value,callback=writeToConfig,user_data=callbackData,width=200)

########################################################################################################################
def initialize():
    readJson()
    #print("uga")
    for i in range(len(config["keyframe"])):
        nextkeyframe = str(i)
        if dpg.does_alias_exist("keyframe:"+nextkeyframe) == False:
            #print("Create new keyframe tab button")
            dpg.add_tab(label="keyframe: "+nextkeyframe,tag="keyframe:"+nextkeyframe,parent="keyframe_bar")
            with dpg.child_window(width=900, height=800,parent="keyframe:"+nextkeyframe,no_scrollbar=True):
                with dpg.group(horizontal=True, width=0):
                    with dpg.child_window(width=600, height=790):
                        with dpg.child_window(autosize_x=True,height=140):
                            dpg.add_text("Keyframe options")
                            dpg.add_separator()
                            for mvcommand,value in magicavoxel_paramters["option"].items():
                                mvcommand = str(mvcommand)
                                translateNewParam("init","",(nextkeyframe,mvcommand,value,"option"))
                                #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                        with dpg.child_window(autosize_x=True,height=140):
                            dpg.add_text("Keyframe Animation options")
                            dpg.add_separator()
                            for mvcommand,value in magicavoxel_paramters["animation"].items():
                                mvcommand = str(mvcommand)
                                translateNewParam("init","",(nextkeyframe,mvcommand,value,"animation"))
                                #Tag = keyframe:set pt_fix_focus:0 e.g Keyframe + key + num Keyframe
                        with dpg.child_window(autosize_x=True,height=700 ,tag="window:param:"+nextkeyframe):
                            dpg.add_text("Parameters")
                            dpg.add_separator()
                    with dpg.child_window(width=300, height=450):
                        #This is the top right window
                        with dpg.child_window(label="Parameters",tag="window:paramselection"+nextkeyframe):
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

########################################################################################################################
#TimeLine

def updateTimeLine2():
    if dpg.does_alias_exist("timeline") == True:
        dpg.delete_item("timeline")
    with dpg.group(parent="Third Window",horizontal=True,tag="timeline"):
        for keyframe in config["keyframe"]:
            #print(keyframe["option"]["interpolation"])
            with dpg.child_window(width=100,height=40):
                dpg.add_text(str(keyframe["option"]["interpolation"]))

            ##print("TIMELINE")
        
def updateTimeLine():
    if dpg.does_alias_exist("timeline") == True:
        dpg.delete_item("timeline")
    offset = 20
    with dpg.group(parent="Third Window",horizontal=True,tag="timeline"):
        with dpg.drawlist(width=950, height=100):  # or you could use dpg.add_drawlist and set parents manually
            for keyframe in config["keyframe"]:
                if "frames" in keyframe["option"] and "interpolation" in keyframe["option"]:
                    for i in range(keyframe["option"]["frames"]):
                        print("keyframe:"+str(i))
                        if keyframe["option"]["interpolation"] == "linear":
                            colour = (200,200,255,255)
                        else:
                            if keyframe["option"]["interpolation"] == "bezier":
                                colour = (60,255,20,255)
                            else: 
                                colour = (100,105,20,255)
                        if i % 5 == 0:
                            if i % 25 == 0:
                                dpg.draw_rectangle( pmin=(0+offset,30),     # top left corner 
                                                    pmax=(1+offset,75),   # bottom right corner
                                                    color=colour,thickness=1)
                                dpg.add_text(str(i),pos=(offset+5,120),parent="timeline",)
                            else:
                                dpg.draw_rectangle( pmin=(0+offset,40),     # top left corner 
                                                    pmax=(1+offset,65),   # bottom right corner
                                                    color=colour,thickness=1,)
                            offset += 8

            sequence = []

            for keyframe in config["keyframe"]:
                if "interpolation" in keyframe["option"]:
                    sequence.append(keyframe["option"]["interpolation"])

            
            #calculate bounding box
            

########################################################################################################################

dpg.create_context()

#look for trash.png in the same directory as this script and in ui folder
#dpg.load_image("trash.png")
try: 
    path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'ui', 'trash.png'))

    width, height, channels, data = dpg.load_image(path)
    with dpg.texture_registry(show=False):
        dpg.add_static_texture(width, height, data, tag="trashImg")
except TypeError:
    print("Ui not found, make sure the ui folder is in the same directory as this script")
    exit()

with dpg.viewport_menu_bar():
    with dpg.menu(label="File"):
        dpg.add_menu_item(label="Save",callback=writeJson)


with dpg.window(tag="Primary Window",label="Config Generator",menubar=True):
    with dpg.child_window(label="Global Settings",tag="window:global",height=70):
        #global settings
        dpg.add_text("Global Settings")
        dpg.add_separator()
        for mvcommand,value in magicavoxel_paramters["global"].items():
            mvcommand = str(mvcommand)
            translateNewParam("","",("",mvcommand,value,"global"))
    with dpg.child_window(tag="Second Window",parent="Primary Window",height=750,no_scrollbar=True):
        with dpg.tab_bar(label="keyframe_bar",tag="keyframe_bar"):    
            dpg.add_tab_button(label="+",tag="add",trailing=True,callback=addNewTabButton)
            dpg.add_tab_button(label="-",tag="remove",trailing=True,callback=deleteTabButton)
    with dpg.child_window(tag="Third Window",parent="Primary Window"):
        dpg.add_text("Timeline")
        dpg.add_separator()
    

initialize()



#dpg.show_documentation()
dpg.set_primary_window("Primary Window", True)
dpg.create_viewport(width=950, height=1100 ,title="Config Generator  |  Dima's Voxel")
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

