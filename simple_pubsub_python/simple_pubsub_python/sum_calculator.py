import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64


class SumCalculator(Node):

    def __init__(self):
        super().__init__('sum_calculator')
        self.subscription = self.create_subscription(
            Int64,
            'natural_number_signal',
            self.listener_callback,
            10)
        self.subscription
        self.datalist = []

    def listener_callback(self, msg):
        self.datalist.append(msg.data)
        self.get_logger().info('Received: "%d" | Sum: "%d"' % (msg.data, sum(self.datalist)))


def main(args=None):
    rclpy.init(args=args)
    sum_calculator = SumCalculator()
    rclpy.spin(sum_calculator)

    sum_calculator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()