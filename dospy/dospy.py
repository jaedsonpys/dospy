import socket
import time
from threading import Thread


class DosPy(object):
    def __init__(self, host: str, port: int, threads_num: int = 100) -> None:
        self._host = host
        self._port = port
        self._threads_num = threads_num

        self._default_protocol = socket.SOCK_DGRAM

    def check_connection_ms(self) -> float:
        conn_check = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        start = time.time()
        conn_check.connect((self._host, self._port))
        end = time.time()

        conn_check.close()
        return end - start

    def is_ready_to_connect(self) -> bool:
        conn_check = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
            conn_check.connect((self._host, self._port))
        except OSError:
            return False
        else:
            conn_check.close()
            return True
