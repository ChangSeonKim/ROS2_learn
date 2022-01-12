import rclpy
from rclpy.node import Node

from basic_interface.srv import MockSensorControl


class CustomServiceServer(Node):

    def __init__(self):
        super().__init__('custom_service_server')
        self.srv = self.create_service(MockSensorControl, 'mock_sensor_control', self.service_callback)

    def service_callback(self, request, response):
        if request.command == 1:
            self.get_logger().info('Control "%s": %d' % (request.sensor_id, request.command))
            response.is_success = True
        else:
            self.get_logger().info('ERROR: unknown command!')
            response.is_success = False
            
        return response


def main(args=None):
    rclpy.init(args=args)

    custom_service_server = CustomServiceServer()

    rclpy.spin(custom_service_server)

    rclpy.shutdown()


if __name__ == '__main__':
    main()