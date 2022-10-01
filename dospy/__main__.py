import os

from .dospy import DosPy


def main():
    os.system('clear')

    print('\033[1;32mDoSPy (Denial of Service Python)\033[m')
    print('\033[3;33mWARNING: It is your responsibility to use this tool against third-party servers.\033[m\n')

    host = input('dospy > Host to attack = ').strip()
    port = input('dospy > Host port      = ').strip()
