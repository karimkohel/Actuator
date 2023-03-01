# HTI-actuator
a module that controls basic computer functions that can be integrated into any central controlling module, targeted to be used in HTI

This module will simulate a bunch of keyboard shortcuts and system commands to achieve control


## Basic actuators
Used to move the mouse to a region of the screen, control the system volume, copy past or control keyboard arrows


```python
from Actuator.actuator import Actuator

# Class dependant methods 
motor = Actuator(numOfRegions=4) # will divide the screen to 4 regions
motor.pointToRegion(3) # will move the mouse to the 3rd region center (left down)

# static methods will be marked static and can be used without constructing
Actuator.paste() # will paste any text copied to clipboard
Actuator.setVolume(40) # will set system volume to a given number

```







##### Done
 - regional mouse movement
 - volume control
 - copy/past 
 - arrow control



##### In Progress
 - regional focus
 - regional click


