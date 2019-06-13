#!/usr/bin/env python
import rospy
from std_msgs.msg import int32
import RPi.GPIO as GPIO

GPIO.setmode(GPIO)
GPIO.setup(12, GPIO.OUT)

class Led_subscribe(self):
	def __init__(self):
		self.sub_control = rospy.Subscriber("~led_test_control", int32, self.sbControl, queue_size = 1)
	
	def sbControl(self, control_msg):
		control_msg = control_msg
		print("[led_subscribe_node] Subscribe successfully!")
		print("your light level of led is %d" % control_msg.data)
		p = GPIO.PWM(12, 0.5)
		p.ChangeDutyCycle(control_msg.data)

if __name__ = "__main__":
	rospy.init_node("led_subscribe_node", anonymous=False)
	led_subscribe = Led_subscribe()
	rospy.spin()