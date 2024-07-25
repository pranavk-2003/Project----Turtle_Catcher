#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
import math
from my_robot_interfaces.msg import Turtle
from my_robot_interfaces.msg import TurtleArray
class TurtleController(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("TurtleController") # MODIFY NAME
        self.turtle_to_catch_=None
        self.pose_=None
        self.pose_publisher=self.create_publisher(
            Twist,"turtle1/cmd_vel",10)
        self.pose_subscriber=self.create_subscription(
            Pose,"turtle1/pose",self.callback_turtle_pose_,10)    
        self.alive_turtles_subscriber_=self.create_subscription(
            "alive_turtles",self.callback_alive_turtles,10)
        self.controller_timer=self.create_timer(0.01,self.controller)   
    def callback_turtle_pose_(self,msg):
        self.pose_=msg
    def callback_alive_turtles():
        if len(msg.turtles)>0:
            self.turtule_to_catch_=msg.turtles[0]
    def controller(self):
        if self.pose_==None or self.turtule_to_catch_==None:
            return
        dist_x=self.turtle_to_catch_.x-self.pose_.x
        dist_y=self.turtle_to_catch_.y-self.pose_.y
        dist=math.sqrt(dist_x*dist_x+dist_y*dist_y)
        msg=Twist()
        if dist>0.5:
            msg.linear.x=dist
            goal_theta=math.atan2(dist_y,dist_x)
            diff=goal_theta - self.pose_.theta
            if diff>math.pi :
                diff-=2*math.pi
            elif diff<-math.pi:
                diff+=2*math.pi
            msg.angular.z=6*diff
        else:
            msg.linear.x=0.0
            msg.angular.z=0.0

        self.pose_publisher.publish(msg)
def main(args=None):
    rclpy.init(args=args)
    node = TurtleController() # MODIFY NAME
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
