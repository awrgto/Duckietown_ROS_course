#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

class Led_publish(object):
	def __init__(self):
		self.pub_control = rospy.Publisher("~led_test_control", Int32, queue_size=1)
		self.controlBox()
	
	def controlBox(self):
		p = GPIO.PWM(12,0.5)
		p.start(1)		
		key = input("light level: ")
		override_msg = Int32()
		override_msg.data = key
		self.pub_control.publish(override_msg)
		print("[led_publish_node] Publish successfully!")
			
if __name__ == "__main__":
	rospy.init_node("led_publish_node", anonymous=False)
	led_control_publish = Led_publish()
	rospy.spin()