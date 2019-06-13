#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(12, GPIO.OUT)

class Led_subscribe(object):
	def __init__(self):
		self.sub_control = rospy.Subscriber("~led_test_control", Int32, self.sbControl, queue_size = 1)
	
	def sbControl(self, control_msg):
		p = GPIO.PWM(12, 50)  # 通道为 12 频率为 50Hz
		p.start(0)
		try:
			while 1:
				for dc in range(0, 101, 5):
					p.ChangeDutyCycle(dc)
					time.sleep(0.1)
				for dc in range(100, -1, -5):
					p.ChangeDutyCycle(dc)
					time.sleep(0.1)
		except KeyboardInterrupt:
			pass
		control_msg = control_msg
		print("[led_subscribe_node] Subscribe successfully!")
		print("your light level of led is %d" % control_msg.data)
		p = GPIO.PWM(12,1)
		p.ChangeDutyCycle(control_msg.data)
		raw_input("press any to break")
		p.stop()
		GPIO.cleanup()

if __name__ == "__main__":
	rospy.init_node("led_subscribe_node", anonymous=False)
	led_control_subscribe = Led_subscribe()
	rospy.spin()