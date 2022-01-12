import rclpy
from rclpy.node import Node

from basic_interface.msg import MockSensor


class CustomMsgSubscriber(Node):

    def __init__(self):
        super().__init__('custom_msg_subscriber')
        self.subscription = self.create_subscription(
            MockSensor,
            'mocksensor_topic',
            self.listener_callback,
            10)
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info('Received(by "%s"): %d' % (msg.sensor_id, msg.data))


def main(args=None):
    rclpy.init(args=args)
    custom_msg_subscriber = CustomMsgSubscriber()
    rclpy.spin(custom_msg_subscriber)

    custom_msg_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()