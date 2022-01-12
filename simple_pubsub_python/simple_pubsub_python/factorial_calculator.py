import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64


class FactorialCalculator(Node):

    def __init__(self):
        super().__init__('factorial_calculator')
        self.subscription = self.create_subscription(
            Int64,
            'natural_number_signal',
            self.listener_callback,
            10)
        self.subscription
        self.datalist = []
        self.resultData = 1

    def listener_callback(self, msg):
        self.datalist.append(msg.data)
        self.resultData *= msg.data
        self.get_logger().info('Received: "%d" | Factorial: "%d"' % (msg.data, self.resultData))


def main(args=None):
    rclpy.init(args=args)
    factorial_calculator = FactorialCalculator()
    rclpy.spin(factorial_calculator)

    factorial_calculator.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()