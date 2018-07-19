#!/usr/bin/env python
import rospy
import pygame
from duckietown_msgs.msg import  Twist2DStamped, BoolStamped, StopLineReading
from std_msgs.msg import String, Int32, Int16
from sensor_msgs.msg import Joy
from Adafruit_PWM_Servo_Driver import PWM
from Adafruit_MotorHAT import Adafruit_MotorHAT
import time
from __builtin__ import True
class porter_car_servo_node(object):
    print "porter_car_servo_node start"
    def __init__(self):
        print "qqqqqqqqqq"
        self.node_name = rospy.get_name()
        self.pwm=PWM(address=0x40,debug=False)
        self.pwm.setPWMFreq(60)
        self.pwm.setPWM(3,0,650)
        self.sub_joy_ = rospy.Subscriber("joy", Joy, self.cbJoy, queue_size=1)
    def cbJoy(self, joy_msg):
            if(joy_msg.buttons[5]==1):
                 self.pwm.setPWM(3,0,400)
                 time.sleep(0.2)
            elif(joy_msg.buttons[4]==1):
                 self.pwm.setPWM(3,0,650)#450
                 time.sleep(0.2)
if __name__=="__main__":
    rospy.init_node("porter_car",anonymous=False)
    porter_car_servo = porter_car_servo_node()
    rospy.spin()
