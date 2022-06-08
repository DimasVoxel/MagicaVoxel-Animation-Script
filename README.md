<h3 align="center">Animation Script for Magicavoxel</h3>

---

<p align="center">
    <br>
</p>

## 📝 Table of Contents
- [Download](#download)
- [What is it?](#problem_statement)
- [Requirements](#Requirements)
- [How to use](#how_to_use)
- [How to run](#how_to_run)
- [Limitations](#limitations)

## Download <a name = "download"/>

Download an .exe from Gumroad: https://dimasvoxel.gumroad.com/l/KrSWL

## 🧐 What is this? <a name = "What is it"/>

This small script was created to create more dynamic renders and animations.

This is a script that interacts with magicavoxel via the built-in magicavoxel console to enable animation of various parameters that cannot normally be animated, such as sun position, camera movement, and more.

## 💡 Requirements <a name = "Requirements"/>

- Magicavoxel 0.99.7
- Windows 10 (7/8 Not tested), MacOS (Limited functionality)

## 🎈 How to use <a name = "how_to_use"/>

The script uses a config.json file to know which parameters to animate.
To create a usable config, use the Config Generator that also comes with this project.
Save the config from the generator and put it in the same folder as the animation script. Open magicavoxel, then run the animation script as explained below. Now, bring magicavoxel to the foreground, and let the program run.

The renders are saved in the magicavoxel export folder.

## How to run <a name = "how to run"/>
### Using .exe file (Windows only)
1. Download the executable(s) using the link above.
2. Place the config in the same folder as the executable.
3. Run the executable like you would with any other .exe file (by double clicking).

### Using Python (MacOS + Windows)
1. Download / Install Python (3.7.x or newer).
2. Download the animation script code from GitHub.
3. Install the following packages / dependencies (this can be done using pip install).
   - PyAutoGUI (MacOS) / PyDirectInput (Windows)
   - Pyperclip
   - DearPyGUI (for config generator)
4. Run the animation script / config generator in Python through the method of your choice (e.g. by selecting Python as the default program for .py files and then opening it, or by opening the script in IDLE and pressing F5 to run, or ...).
