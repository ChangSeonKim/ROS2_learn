import rclpy
from rclpy.node import Node

from std_msgs.msg import String

class BasicPublisher(Node):

    def __init__(self):
        super().__init__('basic_publisher')
        self.publisher_ = self.create_publisher(String, 'basic_pubsub', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = String()
        msg.data = 'Count: %d' % self.count
        self.publisher_.publish(msg)
        self.get_logger().info('Publishing: "%s"' % msg.data)
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    basic_publisher = BasicPublisher()
    rclpy.spin(basic_publisher)

    basic_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()