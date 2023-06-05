#!/usr/bin/env python3
import turtlesim.msg
import tf
import rospy
import roslib
roslib.load_manifest('learning_tf')


def handle_turtle_pose(msg, turtlename):
    # The handler function for the turtle pose message broadcasts this turtle's translation and rotation, and publishes it
    # as a transform from frame "world" to frame "turtleX".

    if turtlename == "turtle1":
        print("%s x,y,z,theta: %.1f,%.1f,%.1f\n" %
              (turtlename, msg.x, msg.y, msg.theta))

    br = tf.TransformBroadcaster()
    br.sendTransform((msg.x, msg.y, 0),
                     tf.transformations.quaternion_from_euler(0, 0, msg.theta),
                     rospy.Time.now(),
                     turtlename,
                     "world")


if __name__ == '__main__':
    rospy.init_node('turtle_tf_broadcaster')

    # This node takes a single parameter "turtle", which specifies a turtle name, e.g. "turtle1" or "turtle2".
    # the param value is specified in the start_demo.launch file
    turtlename = rospy.get_param('~turtle')

    print("turtlename is %s\n" % turtlename)

    # The node subscribes to topic "turtleX/pose" and runs function handle_turtle_pose on every incoming message.
    rospy.Subscriber('/%s/pose' % turtlename,
                     turtlesim.msg.Pose,
                     handle_turtle_pose,
                     turtlename)
    rospy.spin()
