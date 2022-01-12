import rclpy
from rclpy.node import Node

from std_msgs.msg import String


class BasicSubscriber(Node):

    def __init__(self):
        super().__init__('basic_subscriber')
        self.subscription = self.create_subscription(
            String,
            'basic_pubsub',
            self.listener_callback,
            10)
        self.subscription  

    def listener_callback(self, msg):
        self.get_logger().info('Received: "%s"' % msg.data)


def main(args=None):
    rclpy.init(args=args)
    basic_subcriber = BasicSubscriber()
    rclpy.spin(basic_subcriber)

    basic_subcriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()