import sys

from example_interfaces.srv import AddTwoInts
import rclpy
from rclpy.node import Node


class BasicServiceClient(Node):

    def __init__(self):
        super().__init__('basic_service_client')
        self.client = self.create_client(AddTwoInts, 'add_two_ints') # Client builder 패턴
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service server...')
        self.req = AddTwoInts.Request()

    def send_request(self):
        self.req.a = int(sys.argv[1])
        self.req.b = int(sys.argv[2])
        self.future = self.client.call_async(self.req)


def main(args=None):
    rclpy.init(args=args)

    basic_service_client = BasicServiceClient()
    basic_service_client.send_request()

    while rclpy.ok():
        rclpy.spin_once(basic_service_client)
        # future가 done 상태가 되면 다음 if문을 실행합니다
        if basic_service_client.future.done():
            try:
                response = basic_service_client.future.result()
            except Exception as e:
                basic_service_client.get_logger().info(
                    'Service call failed: %r' % (e,))
            else:
                basic_service_client.get_logger().info(
                    'Result: %d + %d = %d' %
                    (basic_service_client.req.a, basic_service_client.req.b, response.sum))
            break

    basic_service_client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()