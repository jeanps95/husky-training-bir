# joy_ws

Code created with the purpose of simulate a robot (Husky) from Clearpath Robotics.

How to use:

(Terminal 1) $ roscore

(Terminal 2) $ rosrun joy_test joy_test.py

(Terminal 3) $ rosrun joy joy_node

(Terminal 4) $ roslaunch husky_gazebo husky_playpen.launch

* It's recommended to follow the terminal order.
* The Husky is controlled by the Left Analog Stick.
* It has a deadman on the left bumper button (LB).

Code based on these references:


Writing a Teleoperation Node for a Linux-Supported Joystick:

http://wiki.ros.org/joy/Tutorials/WritingTeleopNode

Using an Xbox Controller on Ubuntu and ROS:

https://andrewdai.co/xbox-controller-ros.html#rosjoy
