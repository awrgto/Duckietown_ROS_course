#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

class Led_subscribe(object):
	def __init__(self):
		self.sub_control = rospy.Subscriber("~led_test_control", Int32, self.sbControl, queue_size = 1)
	
	def sbControl(self, control_msg):
		p = GPIO.PWM(12, 100)
		p.start(0)
		try:
			print("[led_subscribe_node] Subscribe successfully!")
			print("your light level of led is %d" % control_msg.data)
			p.ChangeDutyCycle(control_msg.data)
			time.sleep(10)
			raw_input("press any to break")
		except KeyboardInterrupt:
			pass
#		control_msg = control_msg
		p.stop()
		GPIO.cleanup()

if __name__ == "__main__":
	rospy.init_node("led_subscribe_node", anonymous=False)
	led_control_subscribe = Led_subscribe()
	rospy.spin()