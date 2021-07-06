#!/usr/bin/env python3

try:
    import rospy
except:
    import rospy2 as rospy

from std_msgs.msg import String

def main():
    rospy.init_node("example_node")
    pub = rospy.Publisher("/hello", String, queue_size = 1)

    rate = rospy.Rate(5)
    seq = 0

    while not rospy.is_shutdown():
        rate.sleep()
        seq += 1
        pub.publish("hello %d" % seq)

if __name__ == "__main__":
    main()
