#!/usr/bin/env python  
import roslib
roslib.load_manifest('joy_test')
import rospy
import math
import tf
from geometry_msgs.msg import Twist
from sensor_msgs.msg import Joy

class turtlebot():

    def __init__(self):
        #Creating our node,publisher and subscriber
        rospy.init_node('turtlebot_controller', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist, queue_size=10)


    def get_distance(self, goal_x, goal_y):
        distance = sqrt(pow((goal_x - self.pose.x), 2) + pow((goal_y - self.pose.y), 2))
        return distance

    def move2goal(self):
        goalx = 5
        goaly = 5
        distance_tolerance = 0.1
        vel_msg = Twist()
        listener = tf.TransformListener()

        (trans,rot) = listener.lookupTransform('map', 'base_link', rospy.Time(0))
        while sqrt(pow((goalx - trans[0]), 2) + pow((goaly - trans[1]), 2)) >= distance_tolerance:
            (trans,rot) = listener.lookupTransform('map', 'base_link', rospy.Time(0))
            #Porportional Controller
            #linear velocity in the x-axis:
            vel_msg.linear.x = 1.5 * sqrt(pow((goalx - trans[0]), 2) + pow((goaly - trans[1]), 2))
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            #angular velocity in the z-axis:
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = 4 * (atan2(goaly - trans[1], goalx - trans[0]) - rot[3])

            #Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)
            self.rate.sleep()
        #Stopping our robot after the movement is over
        vel_msg.linear.x = 0
        vel_msg.angular.z =0
        self.velocity_publisher.publish(vel_msg)

        rospy.spin()

if __name__ == '__main__':
    try:
        #Testing our function
        x = turtlebot()
        x.move2goal()

    except rospy.ROSInterruptException: pass


# if __name__ == '__main__':
#     rospy.init_node('turtle_tf_listener')

#     listener = tf.TransformListener()

#     turtle_vel = rospy.Publisher('/husky_velocity_controller/cmd_vel', Twist ,queue_size=10)

#     rate = rospy.Rate(10.0)
#     while not rospy.is_shutdown():
#         try:
#             (trans,rot) = listener.lookupTransform('map', 'base_link', rospy.Time(0))
#         except (tf.LookupException, tf.ConnectivityException, tf.ExtrapolationException):
#             continue

#         angular = 4 * math.atan2(trans[1], trans[0])
#         linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
#         cmd = Twist()
#         cmd.linear.x = linear
#         cmd.angular.z = angular
#         turtle_vel.publish(cmd)

#         rate.sleep()