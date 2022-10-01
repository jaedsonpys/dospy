import os
import sys

from .dospy import DosPy


def main():
    os.system('clear')

    print('\033[1;32mDoSPy (Denial of Service Python)\033[m')
    print('\033[3;33mWARNING: It is your responsibility to use this tool against third-party servers.\033[m\n')

    host = input('dospy > Host to attack = ').strip()
    port = int(input('dospy > Host port      = ').strip())

    dospy = DosPy(host, port)

    print('\nChecking host availability...', end=' ')
    result = dospy.is_ready_to_connect()

    if result:
        response_time = dospy.check_connection_ms()
        print('\033[32mOK\033[m')
        print(f'Response time is {response_time:.4f}ms')
    else:
        print('\033[31mERROR: Could not connect to specified host and port.\033[m')
        sys.exit(1)
