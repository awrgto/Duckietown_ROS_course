#!/usr/bin/env python
import rospy
from duckietown_msgs.msg import AprilTagsWithInfos
from std_msgs.msg import Int16

class apriltags_control_node(object):
    def __init__(self):
        self.sub_tag_id = rospy.Subscriber("apriltags_postprocessing_node/apriltags_out", AprilTagsWithInfos, self.get_Apriltag, queue_size=1)
        
    def get_Apriltag(self, Tag):
        try:
            tag_id = Tag.infos[0].id
            rospy.loginfo("-------TAG = %d---------" %(tag_id))
            
        except:
            print("NO TAG")

if __name__ == "__main__":
    rospy.init_node("apriltags_control_node", anonymous=True)
    apriltags_control = apriltags_control_node()
    rospy.spin() 
