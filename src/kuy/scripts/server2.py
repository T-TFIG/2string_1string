#!/usr/bin/python3
from kuy.srv import Sentms

import rclpy
from rclpy.node import Node

class StringService(Node):

    def __init__(self):
        super().__init__('String_Node')
        self.srv = self.create_service(Sentms, 'str_service', self.make_string_callback)
        self.get_logger().info('say Hi')

    def make_string_callback(self, request, response):
        print("send_request")
        response.c = str(request.a) + str(request.b)

        return response


def main():
    rclpy.init()

    server_node = StringService()

    print("In progress")
    
    try:
        rclpy.spin(server_node)
    except KeyboardInterrupt:
        server_node.destroy_node()
        rclpy.shutdown()



if __name__ == '__main__':
    main()
