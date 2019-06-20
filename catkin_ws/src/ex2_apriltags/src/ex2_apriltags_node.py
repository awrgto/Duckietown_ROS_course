#!/usr/bin/env python
import rospy
from duckietown_msgs.msg import WheelsCmdStamped, AprilTagsWithInfos

class ex2_apriltags_node(object):
    def __init__(self):

        self.sub_tag_id = rospy.Subscriber("apriltags_postprocessing_node/apriltags_out", AprilTagsWithInfos, self.get_Apriltag, queue_size=1)
        self.sub_WCR = rospy.Subscriber("~wheels_cmd", WheelsCmdStamped, self.cbWheelsCmdRec, queue_size=1)

        self.cwr = 0


    def  cbWheelsCmdRec(self, wC):
        self.cwr += wC.header.stamp.nsecs *( 10^-9 )* 20 * (wC.vel_left / 0.582576274872)

    def get_Apriltag(self, Tag):
        try:
            dist = 0
            tag_id = Tag.infos[0].id
            rospy.loginfo("-------TAG = %d---------" %(tag_id))
            if tag_id == 302 :
                self.cwr = 0
            elif tag_id == 21 :
                rospy.loginfo("distance from other tag is %d cm" % (self.cwr))

        except:
            print("NO TAG")

if __name__ == "__main__":
    rospy.init_node("ex2_apriltags_node", anonymous=False)
    ex2_apriltags = ex2_apriltags_node()
    rospy.spin()
