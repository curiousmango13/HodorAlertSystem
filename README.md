# HodorAlertSystem
Simple baby gates alert system using ESP32 and Reed Switch

1.	Overview of the project -- an exploitation of what your project does and how it works.  This can be as technical or as plain-language as you like -- whatever makes sense for you.
a basic prototype of a simple alarm system for monitoring state (open/close) of baby gates aka Hodor 1.0. 
Magnetic reed switch planted on both sides of the gates plugged into EPS32 
 In the event of doors left open, system will issue a message and  make a call through the broker account to parents’ 
Red LED is used as a visual alert 

2.	Demo of  project - Video  https://youtu.be/x7n-SPKERBI

Milestones:
•	Acquiring all necessary hardware
	ESP32
	Reed Switch
	Breadboard
	LED
	Wires
	Data cable
•	Setting up hardware 
	
•	Installing required software.
Driver for Windows10 to read data from ESP32, circuitPython, Thonny
•	Writing a working and functioning code to get an input.
•	Handling input 
https://ifttt.com/

•	Connecting to messaging service. 
https://mqtt.org/

•	Adding visual alert – light to the set


3.	Challenges and Wins – 
what went right:
•	wiring was fast

what went wrong: 
•	ESP32 did not show up as an external drive
•	New ESP32 was not soldiered


what went sideways: 
•	no reading – faulty LED
•	not a lot of resources for combination of my hardware/software

4.	Future directions and enhancements -- how would you enhance or modify this project going forward.
•	Case
•	Wire-free reed switch
•	Different alerts
•	Integration with video cam to be activated
