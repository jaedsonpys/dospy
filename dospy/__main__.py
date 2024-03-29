import os
import sys

from .dospy import DosPy


def prompt(message: str):
    return input(f'\033[1;32mDoSPy\033[m > {message}')


def main():
    os.system('clear')

    print('\033[1;32mDoSPy (Denial of Service Python)\033[m')
    print('\033[3;33mWARNING: It is your responsibility to use this tool against third-party servers.\033[m\n')

    host = prompt('Host to attack = ').strip()
    port = int(prompt('Host port      = ').strip())

    dospy = DosPy(host, port)

    threads_num = prompt('Number of threads (default is 100) = ').strip()
    bytes_num = prompt('Number of bytes (default is 1000)  = ').strip()

    if not threads_num:
        threads_num =  100
    
    if not bytes_num:
        bytes_num = 1000

    dospy.set_config(int(threads_num), int(bytes_num))

    print(f'\n- \033[33mConfigured to create {threads_num} threads, sending {bytes_num} bytes.\033[m\n')
    result = prompt('start attack? [y/n] = ').strip().lower()

    if result in ('y', 's'):
        try:
            print('\n- \033[32mStarting attack...\033[m')
            dospy.attack()
            print('- \033[32mDoSPy is running...\033[m')

            while True:
                pass
        except KeyboardInterrupt:
            print('\n- \033[31mAttack canceled by user\033[m')
            dospy.stop_attack()
    else:
        print('\n\033[31mCanceled by user!\033[m')
        sys.exit(0)
