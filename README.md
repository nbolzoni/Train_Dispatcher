# Train_Dispatcher

A train dispatcher's primary job is to ensure that trains are properly routed for their respective destinations. He or she must choose routings that are safe and that allow the train to reach its destination in a prompt manner to satisfy tight schedules.

This project attempts to simulate what a railroad dispatcher may see on a Centralized Traffic Control (CTC) display panel. A GUI is used to show tracks, interlockings, signals, and track occupancy. The user is allowed to change routings and signal indications to allow trains to proceed to the correct destination without any collisions.

Tkinter was used in this project to create the GUI. In its current state, the train_dispatcher program takes three inputs - a list of defined trains, track segments, and signals with relevant attributes such as direction, position, and identification. Track segments and signals must be linked together to form a logical route for the train to follow . Once these inputs are defined, the user is presented with an iterface that shows all three elements in "live" time. Track segments are normally shown as white rectangles while segments occupied by trains are shown in red. Signals govern entry to "blocks" of these track segments and will prevent trains from colliding with each other.

There are two types of signals utlized in this simulation:
1. Automatic Block Signals (ABS) - signals automatically grant permission to enter a block if the track segments ahead are clear
2. Controlled Signals - signals must be manually set to be cleared so that switches can be set in the proper position before allowing trains to proceed.

The user is allowed to change the position of each switch by clicking on the switch track segment. The user can also grant clearance at controlled signals to allow trains to pass them (controlled signals only guard switches in this case). ABS signals cannot be set by the user as they are automatically controlled.

The simulation ends when all trains have left the route at a boundary track segment.

A test route is provided in this directory to demostrate a simple scenario with two trains heading in opposite directions on a small area of controlled tracks.

Inspiration for this project:
http://morscher.com/atcs/display_cleveland_multi.jpg
