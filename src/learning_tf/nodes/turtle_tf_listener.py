#!/usr/bin/env python3
import turtlesim.srv
import geometry_msgs.msg
import tf
import math
import rospy
import roslib

roslib.load_manifest("learning_tf")

if __name__ == "__main__":
    rospy.init_node("turtle_tf_listener")

    listener = tf.TransformListener()

    rospy.wait_for_service("spawn")
    spawner = rospy.ServiceProxy("spawn", turtlesim.srv.Spawn)
    spawner(4, 2, 0, "turtle2")

    # we will move turtle2 based on the pose of turtle1
    turtle_vel = rospy.Publisher(
        "turtle2/cmd_vel", geometry_msgs.msg.Twist, queue_size=1
    )

    rate = rospy.Rate(10.0)
    while not rospy.is_shutdown():
        try:
            # we query the listener for a specific transformation by lookupTransform
            # We want the transform from the '/turtle1' frame  to the '/turtle2' frame
            # rospy.Time(0) will just get us the latest available transform
            # trans is the (x, y, z) linear transformation of the child frame relative to the parent,
            # rot is the (x, y, z, w) quaternion required to rotate from the parent orientation to the child orientation
            (trans, rot) = listener.lookupTransform(
                "/turtle2", "/turtle1", rospy.Time(0)
            )
        except (
            tf.LookupException,
            tf.ConnectivityException,
            tf.ExtrapolationException,
        ):
            continue

        print(
            "relative transformation between two turtles:\ntranslation: %.1f, %.1f, %.1f\nrotation: %.1f, %.1f, %.1f, %.1f\n"
            % (trans[0], trans[1], trans[2], rot[0], rot[1], rot[2], rot[3])
        )

        delta = 2

        if trans[0] ** 2 + trans[1] ** 2 > delta:
            angular = 4 * math.atan2(trans[1], trans[0])
            linear = 0.5 * math.sqrt(trans[0] ** 2 + trans[1] ** 2)
            cmd = geometry_msgs.msg.Twist()
            cmd.linear.x = linear
            cmd.angular.z = angular
            turtle_vel.publish(cmd)

        rate.sleep()
