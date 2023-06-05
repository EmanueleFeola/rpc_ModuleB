#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def callback(data):
    # callback che viene richiamata quando arriva qualcosa
    # sul topic
    rospy.loginfo(rospy.get_caller_id() + 'I heard %s', data.data)

def listener():
    rospy.init_node('listener', anonymous=True)
    # specifico a quale topic mi voglio registrare e il tipo di dato
    # che mi aspetto
    rospy.Subscriber('chatter', String, callback)

    # keep python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
