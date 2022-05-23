import socket
import sys


# Font setting
class Text:
    pink = '\033[95m'
    blue = '\033[94m'
    cyan = '\033[96m'
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'
    default = '\033[0m'
    bold = '\033[1m'
    underline = '\033[4m'


# Welcome screen
def logo ():
    # http://patorjk.com/   (ANSI shadow)
    print(f''' {Text.green}
        ██╗  ██╗███╗   ██╗ ██████╗ ██╗  ██╗    ██████╗ ███████╗
        ██║ ██╔╝████╗  ██║██╔═══██╗╚██╗██╔╝    ██╔══██╗██╔════╝
        █████╔╝ ██╔██╗ ██║██║   ██║ ╚███╔╝     ██████╔╝███████╗
        ██╔═██╗ ██║╚██╗██║██║   ██║ ██╔██╗     ██╔═══╝ ╚════██║
        ██║  ██╗██║ ╚████║╚██████╔╝██╔╝ ██╗    ██║     ███████║
        ╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═╝    ╚═╝     ╚══════╝ {Text.cyan}
        version: 0.01   |   author: Mr Knox   |   Port Scanner {Text.default}
        \n
    ''')


def get_ip(target):
    try:
        target = socket.gethostbyname(target) 
        print(f"\n{Text.cyan} [+] Target IP : {target} {Text.default} \n")
        return target

    except:
        print(f"{Text.red} [-] Unable to find target. {Text.default} \n")
        main()


def scan(target, port_1, port_2, timeout):
    ip = get_ip(target)
    print(" Press ctrl+z to exit.")

    for port in range(port_1, port_2+1):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(timeout)
            sock.connect((ip, port))
            service = sock.recv(1024).decode()
            sys.stdout.write(f'\r{Text.green} [+] Port {port} is open {Text.default}')
            sys.stdout.flush()
            print(f'\n {service} ')

        except:
            sys.stdout.write(f'\r{Text.yellow} [*] Scanning port {port}{Text.default}  ')
            sys.stdout.flush()

    sys.stdout.write(f'\r{Text.blue} (>‿◠) Scan complete {Text.default} \n')
    sys.stdout.flush()


def main(recall=None):
    global target, port_1, port_2, timeout

    target = input(" [*] Enter target to scan: ")
    port_1 = input(" [*] Enter first Port no.: ")
    port_2 = input(" [*] Enter last Port no.: ")
    timeout = input(" [*] Set Timeout in seconds: ")

    try:
        port_1 = int(port_1)
        port_2 = int(port_2)

    except:
        print(f'\n{Text.red} [-] Port number should be Integer. {Text.default}')
        port_1 = input(" [*] Enter first Port no.: ")
        port_2 = input(" [*] Enter last Port no.: ")

    try:
        timeout = float(timeout)

    except:
        print(f'\n{Text.red} [-] Timeout should be a float or integer. {Text.default}')
        timeout = input(" [*] Set Timeout in seconds: ")

    scan(target, port_1, port_2, timeout)


if __name__ == "__main__":
    logo()
    main()
