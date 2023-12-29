import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def main():
    rclpy.init()
    node = Node("listener")
    client = node.create_client(Query, 'query') #service client make
    while not client.wait_for_service(timeout_sec=1.0): #service wait
        node.get_logger().info('待機中')

    req = Query.Request()
    req.name = "アシド"
    future = client.call_async(req)　#asynchronuos service call

    while rclpy.ok():
        rclpy.spin_once(node) #call once and end
        if future.done(): #if over
            try:
                response = future.result()
            except:
                node.get_logger().info('呼び出し失敗')
            else: #else for not except time
                node.get_logger().info("age: {}".format(response.age))

            break

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
