Animation Script - Version 06.05.2022 1

#########

What is this?

This is a small tool set to animate the camera and other parameters in magicavoxel to make more interesting renders.

########

Which os and magicavoxel are supported?

Magicavoxel: 0.99.7
OS : Windows 10 

#########

How do I use it?

First, create a configuration in the Config Generator. After you're done save the config, this will result in a config.json to be generated.
This config.json will be later used by the animation script itself to animate the parameters inside magicavoxel.

#########

How do I use the config generator?

1. Open the config generator.exe and create at least 2 key frames by clicking on the +
2. Choose what parameters you would like to animate. Select them from the camera and light tab on the right side.
2.1. Make sure to add the parameter you want to animate in both key frames. You always need a starting point and an end point, a → b
3. Finally, configure options that are provided (number of frames, seconds for each frame, rotation of camera)
4. Save file (top-left corner)

########

What does Animation direction mean?

Animation direction is for you to decide in which direction you want your camera to rotate. This only applies for camera yaw.

Clockwise camera rotation:
   --->
/ \	|
 |     \ /
   ←--


#######

What are the different interpolation types.

There are 2.5 Interpolation types that are available in the animation script(so far).

Linear: Values change from a → b in a linear fashion Example: https://twitter.com/Dimasvoxel/status/1438620478042746880(Animation is choppy because of low frame rate)

Bezier: For a bezier animation, you require more than 2 key frames in a sequence. All values will be animated in a seamless and combined way, a -> b -> c 
Examples: https://twitter.com/Dimasvoxel/status/1471534537591173127
Examples: https://twitter.com/Dimasvoxel/status/1521809419771785216

Bezier-sequence: To create a bezier animation, you need to tell the animation script which key frames you want to combine. 
		 Your first key frame should be set to bezier and all subsequent key frames need to be set to bezier-sequence. (Take a look at the Timeline in the bottom to see how it is affected)
		
######

Key frame Animation options, what are those?

Magicavoxel 99.7 supports key frame animations 
Example: https://twitter.com/Dimasvoxel/status/1470832109954768897

Animation script supports to both animate the camera and the key frame animation at the same time.
To achieve that effect, “Enable animation” and choose a starting and end frame of your magicavoxel key frame animation.

Example: https://twitter.com/Dimasvoxel/status/1471534537591173127
Example: https://twitter.com/Dimasvoxel/status/1519379761063153664