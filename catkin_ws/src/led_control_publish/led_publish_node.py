
import rospy
from std_msgs.msg import int32

class Led_publish(object):
	def __init__(self):
		self.pub_control = rospy.Publisher("~led_test_control", int32, queue_size=1)
		self.controlBox()
	
	def controlBox(self):
		while(true):
			key = input("light level: ")
			override_msg = int32()
			override_msg.data = key
			self.pub_control.publish(override_msg)
			print("[led_publish_node] Publish successfully!")
			
if __name__ == "__main__":
	rospy.init_node("led_publish_node", anonymous=False)
	led_publish_node = Led_publish()
	rospy.spin()