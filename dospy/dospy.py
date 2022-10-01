import socket
from threading import Thread


class DosPy(object):
    def __init__(self) -> None:
        self._threads_num = 100
        self._default_protocol = socket.SOCK_DGRAM
