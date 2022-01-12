import rclpy
from rclpy.node import Node

from basic_interface.msg import MockSensor # 직접 만든 msg파일을 import!

class CustomMsgPublisher(Node):

    def __init__(self):
        super().__init__('custom_msg_publisher')
        self.publisher_ = self.create_publisher(MockSensor, 'mocksensor_topic', 10)
        timer_period = 1
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.count = 0

    def timer_callback(self):
        msg = MockSensor()
        msg.sensor_id = "RAPA_SENSOR_1"
        msg.data = self.count
        self.publisher_.publish(msg)
        self.get_logger().info('Sensor ID: "%s", Data: "%d"' % (msg.sensor_id, msg.data))
        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    custom_msg_publisher = CustomMsgPublisher()
    rclpy.spin(custom_msg_publisher)

    custom_msg_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()