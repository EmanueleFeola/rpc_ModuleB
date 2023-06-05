#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

def talker():
    # specifico il topic (chatter) e il tipo di dato 
    # da pubblicare (String)
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    while not rospy.is_shutdown():
        # stringa da mandare
        hello_str = "hello world from VR474837"
        # printa su schermo la stringa pubblicata
        rospy.loginfo(hello_str)
        # pubblica la stringa sul topic
        pub.publish(hello_str)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
