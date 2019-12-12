# joy_ws

## __It's recommended to install these:__

* sudo apt-get install ros-distribution-husky-simulator
* sudo apt-get install ros-distribution-husky-desktop
* sudo apt-get install ros-distribution-husky-navigation

## __Code created with the purpose of simulate a robot (Husky) from Clearpath Robotics.__

How to use a xbox controller to move the robot:

(Terminal 1) $ roscore

(Terminal 2) $ rosrun joy_test joy_test.py

(Terminal 3) $ rosrun joy joy_node

(Terminal 4) $ roslaunch husky_gazebo husky_playpen.launch

* It's recommended to follow the terminal order.
* The Husky is controlled by the Left Analog Stick.
* It has a deadman on the left bumper button (LB).

### Code based on these references:

Writing a Teleoperation Node for a Linux-Supported Joystick:

http://wiki.ros.org/joy/Tutorials/WritingTeleopNode

Using an Xbox Controller on Ubuntu and ROS:

https://andrewdai.co/xbox-controller-ros.html#rosjoy

</br>
</br>


## __Code created with the purpose to read and X and Y input for the terminal to navigate the Husky.__

How to use the 2D navigation script:

(Terminal 1) $ roslaunch husky_gazebo husky_playpen.launch

(Terminal 2) $ roslaunch husky_viz view_robot.launch

(Terminal 3) $ roslaunch husky_navigation gmapping_demo.launch

(Terminal 4) $ rosrun joy_test joy_move.py

* It's recommended to follow the terminal order.
* When prompted, input the X goal.
* When prompted, input the Y goal.
* To exit, press "CTRL + C" then "Enter".

### Code based on these references:

How to define goal in RVIZ through python script:

https://answers.ros.org/question/283633/how-to-define-goal-in-rviz-through-python-script/
