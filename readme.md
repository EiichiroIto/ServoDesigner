ServoDesigner
====
[Readme in Japanese](https://github.com/EiichiroIto/ServoDesigner/blob/master/readme.ja.md "Readme in Japanese")

#Overview
ServoDesigner is a Scratch Mod for controlling multiple servo motors at the same time.

It can set and change PWM value up to 30 servos. Although ServoDesigner can not control servos directly, it controls indirectly using a program that controls servos via network communication.

#Description
ServoDesigner provides servo sprites and looks blocks. A servo sprite is added to project then it creates new 20 variables corresponding to servo channels.
 Multiple servo values are set up at the same time by editing a servo sprite's costume. Variables are changed and broadcast message 'servo changed' is sent whenever costume is changed.

ServoDesigner enables 'Mesh network' of Based on Scratch. If 'Host Mesh' or 'Join Mesh' is started, Based on Scratch sends every servo variable changes to network-connected programs. You need to make a program that receives variables and broadcast messages through 'Remote Sensor Protocol' and controls servo motors.

Two sample programs (controls servo using Arduino with firmata and using Raspberry-pi with servo controller via i2c protocol) are provided. You can modify freely these programs for your system.

##Block
ServoDesigner/Based on Scratch

--> Programs that controls servo motors (via Remote Sensor Protocol)

--> Servo Controller (GPIO, firmata, i2c etc)

Servo Motors (Maximum of 30 motors)

#Demo
![Creating a servo sprite and set up servo values](https://raw.githubusercontent.com/wiki/EiichiroIto/ServoDesigner/images/sd1.gif)
![Changing servo sprite by Looks block](https://raw.githubusercontent.com/wiki/EiichiroIto/ServoDesigner/images/sd2.gif)
![Using broadcast message](https://raw.githubusercontent.com/wiki/EiichiroIto/ServoDesigner/images/sd3.gif)

#Requirement
* Scratch 1.4
* Scratch Source Code 1.4 -- install from cs file

##Additional requirement
* Servo motors.
* Servo controller like Arduino or PCA9685.
* Python environment (Python 2.7) for sample programs.

#Usage
##Creating a servo sprite and set up servo value
1. Right click on stage, and select 'create new servo sprite'.
2. Select Costume tab, and click edit button of costume.
3. Servo Editor opens, then change variable watchers using slider.
4. Clicking on variable watcher Dialog box appears. Enter a servo value.
5. Clicking 'send servo changed' button, it sends 'servo changed' as broadcast message.
6. Selecting 'always send', automatically sends broadcast whenever variable watchers changes.
7. Clicking 'Set all to ' buttons, it sets up all variables to 0, 128, 255 or entered value.

##Using Looks block
1. Select Looks block category.
2. Put 'switch to costume servo in 2 secs' block to script pane.
3. You may change time and costume name.
4. Click the block.

#Install
##Install from image file
1. Install new Scratch 1.4 without using installer. (Extract compressed file)
2. Copy ServoDesigner.image and ServoDesigner.changes to the installed folder.
3. Drag ServoDesigner.image to Scratch application to start ServoDesigner.

##Install from cs file
1. Install new Scratch 1.4 without using installer. (Extract compressed file)
2. Extract ScratchSourceCode1.4 and copy files to installed folder.
3. Drag ServoDesigner.image to Scratch application to start Based on Scratch.
4. Close all windows. Select yes when 'Changes have not been saved...' dialog box appears.
5. Click desktop with pressing shift key to show 'find window' menu and select Scratch Frame.
6. Click close button on top left of Scratch window.
7. Click empty desktop and select 'open...' then 'file list' menu item.
8. Select 'ServoDesigner.cs' item on top right pane of File List window.
9. It will appear a scroll bar on the left side of top right pane. Click menu button above the scroll bar and select 'fileIn' menu item.
10. Click desktop and select 'open...' then 'Scratch' menu item.
11. After starting Based on Scratch, select 'File' menu with pressing shift-key and select 'Save Image in User Mode' menu item.
12. Select yes when 'Close non-Scratch windows...' dialog box appears.
13. Finished.

#License
The MIT License (MIT)

#Option
You can change the number of servos using setting file: 'Scratch.ini'.

`ServoChannels=28`

