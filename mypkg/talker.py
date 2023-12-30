import rclpy
from rclpy.node import Node 
from std_msgs.msg import Int16, String

rclpy.init()
node = Node("talker")
pub = node.create_publisher(Int16, "countup", 10)
pub = node.create_publisher(String, "message", 10)
n = 0

def cb():
    global n
    age = Int16()
    age.data = n
    pub.publish(age)

    name = String()
    name.data = "ashid" 
    pub.publish(name)

    n = 10

node.create_timer(0.5, cb)
rclpy.spin(node)
