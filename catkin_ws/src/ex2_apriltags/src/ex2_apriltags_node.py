#!/usr/bin/env python
import rospy
from duckietown_msgs.msg import AprilTagsWithInfos

class ex2_apriltags_node(object):
    def __init__(self):
        self.pub_led_brightness = rospy.Publisher("~led_brightness_controller", Int32, queue_size=1)
        self.sub_tag_id = rospy.Subscriber("apriltags_postprocessing_node/apriltags_out", AprilTagsWithInfos, self.get_Apriltag, queue_size=1)
        
    def get_Apriltag(self, Tag):
        try:
            tag_id = Tag.infos[0].id
            rospy.loginfo("-------TAG = %d---------" %(tag_id))
            led_right = Int32()
            led_right.data = 3
            self.pub_led_brightness.publish(led_right)
            print("led brightness have update !")
            
        except:
            print("NO TAG")

if __name__ == "__main__":
    rospy.init_node("ex2_apriltags_node", anonymous=True)
    ex2_apriltags = ex2_apriltags_node()
    rospy.spin()
