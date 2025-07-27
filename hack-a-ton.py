"""
Github: ........ https://github.com/voidgiux/hack-a-ton
Title: ......... hack-a-ton
Description: ... A fake terminal "hacking" simulation that fills your screen with random commands and nonsense.
 ............... To use as an idle animation, to look busy, or just for fun.
Author ......... voidgiux
Date: .......... 26 Jul 2025
"""

import time
import random
import os
import argparse


def load_lines_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    return lines


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def process_command(cmd: str) -> str:
    if '{}' in cmd:
        cmd = cmd.format(random.randint(0, 255), random.randint(0, 255))

    if "CVE-2023-XXXX" in cmd:
        year = random.randint(2018, 2025)
        cve_id = random.randint(1000, 99999)
        cmd = cmd.replace("CVE-2023-XXXX", f"CVE-{year}-{cve_id}")

    return cmd


def random_line():
    choice = random.choice(['hash', 'nonsense', 'symbols'])

    if choice == 'hash':
        length = random.choice([32, 40, 48, 64])
        return ''.join(random.choices('0123456789abcdef', k=length))

    elif choice == 'nonsense':
        words = ['flarb', 'snark', 'blip', 'zarg', 'wibble', 'foo', 'bar', 'baz', 'qux', 'foobar', 'narf']
        count = random.randint(3,7)
        return ' '.join(random.choices(words, k=count))

    else:
        symbols = '!@#$%^&*()-_=+[]{};:<>,.?/\\|~`'
        length = random.randint(20, 50)
        return ''.join(random.choices(symbols, k=length))


def simulate_console_sequence():
    sequence = [
        "[*] Starting Metasploit Framework...",
        "msf6 > use exploit/windows/smb/ms17_010_eternalblue",
        "msf6 exploit(ms17_010_eternalblue) > set RHOST 192.168.56.10",
        "RHOST => 192.168.56.10",
        "msf6 exploit(ms17_010_eternalblue) > set LPORT 4444",
        "LPORT => 4444",
        "msf6 exploit(ms17_010_eternalblue) > run",
        "[*] Exploit sent successfully!",
        "[+] Meterpreter session 1 opened!",
        "meterpreter > getuid",
        "Server username: NT AUTHORITY\\SYSTEM",
        "meterpreter > hashdump",
        "[*] Dumping password hashes...",
        "Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::",
    ]

    for line in sequence:
        print(line)
        time.sleep(random.uniform(0.3, 0.7))
    print()


def simulate_hashcat_sequence():
    sequence = [
        "hashcat -m 0 -a 0 -o cracked.txt hashes.txt rockyou.txt",
        "Hashcat v6.2.5 starting...",
        "Started: Tue Jul 27 14:00:00 2025",
        "Speed.#1.........:  1000 H/s (10.0ms) @ Accel:32 Loops:1024 Thr:256 Vec:8",
        "Recovered........: 2/5 (40.00%) Digests",
        "Progress.........: 120000/500000 (24.00%)",
        "Rejected.........: 0/120000 (0.00%)",
        "Restore.Point....: 100000/500000 (20.00%)",
        "Restore.Sub.#1...: Salt:0 Amplifier:0",
        "",
        "Session.Name.....: hashcat_session",
        "Status...........: Running",
        "Guess.Base.......: File: rockyou.txt",
        "Guess.Queue......: 1/1 (100.00%)",
        "",
        "example1:password123",
        "example2:qwertyuiop",
        "example3:letmein",
        "",
        "Press 'q' to quit, 's' to suspend, 'r' to restore.",
    ]

    for line in sequence:
        print(line)
        time.sleep(random.uniform(0.2, 0.6))
    print()


def simulate_nmap_sequence():
    sequence = [
        "Starting Nmap 7.80 ( https://nmap.org ) at 2025-07-27 14:10 UTC",
        "Nmap scan report for target.host (192.168.1.100)",
        "Host is up (0.0012s latency).",
        "Not shown: 997 filtered ports",
        "PORT     STATE  SERVICE",
        "22/tcp   open   ssh",
        "80/tcp   open   http",
        "443/tcp  open   https",
        "8080/tcp closed http-proxy",
        "",
        "Nmap done: 1 IP address (1 host up) scanned in 6.45 seconds"
    ]

    for line in sequence:
        print(line)
        time.sleep(random.uniform(0.15, 0.5))
    print()


def simulate_hydra_sequence():
    sequence = [
        "Hydra v9.1 (c) 2025 by van Hauser/THC & David Maciejak - Please do not use in military or secret service organizations, or for illegal purposes.",
        "Hydra (http://www.thc.org/thc-hydra) starting at 2025-07-27 14:15:00",
        "[DATA] max 16 tasks per 1 server, overall 16 tasks, 1434437 login tries (l:1000/p:1434), ~89652 tries per task",
        "[STATUS]  123.00 tries/min, 16 tasks, 0 done, 5 active",
        "[22][ssh] host: 192.168.1.100   login: admin   password: 123456",
        "[STATUS]  234.00 tries/min, 16 tasks, 1 done, 5 active",
        "[22][ssh] host: 192.168.1.100   login: root    password: toor",
        "[STATUS]  345.00 tries/min, 16 tasks, 2 done, 5 active",
        "[22][ssh] host: 192.168.1.100   login: user    password: password123",
        "[STATUS]  456.00 tries/min, 16 tasks, 3 done, 5 active",
        "1 of 1 target successfully completed, 3 valid passwords found",
        "Hydra finished"
    ]

    for line in sequence:
        print(line)
        time.sleep(random.uniform(0.15, 0.5))
    print()


def fake_terminal_loop(commands, outputs):
    print("> > > Starting hacking procedure < < <")
    print("> > > Stay a while and listen... < < <\n")
    time.sleep(1)

    iteration = 0
    try:
        while True:
            iteration += 1

            rand_val = random.random()

            if rand_val < 0.05:
                print(random_line())
                time.sleep(random.uniform(0.3, 0.7))
                continue

            elif rand_val < 0.10:
                simulate_console_sequence()
                continue

            elif rand_val < 0.15:
                simulate_hashcat_sequence()
                continue

            elif rand_val < 0.20:
                simulate_nmap_sequence()
                continue

            elif rand_val < 0.25:
                simulate_hydra_sequence()
                continue

            raw_command = random.choice(commands)
            cmd = process_command(raw_command)
            print(f"$ {cmd}")
            time.sleep(random.uniform(0.2, 0.6))

            n_outputs = random.randint(1, 5)
            for _ in range(n_outputs):
                print(f"  {random.choice(outputs)}")
                time.sleep(random.uniform(0.15, 0.4))

            print()
            time.sleep(random.uniform(0.3, 0.8))

    except KeyboardInterrupt:
        print_quit_message()


def print_initial_sequence():
    steps = [
        ("[*] Boot sequence initialized...", random.uniform(0.2, 1)),
        ("[*] Establishing uplink...", random.uniform(0.2, 1)),
        ("[+] Network node handshake successful.", random.uniform(0.2, 1)),
        ("[*] Loading core modules...", random.uniform(0.2, 1)),
        ("[!] Charging the faith capacitors...", random.uniform(1, 2)),
        ("[*] Realigning subspace sarcasm modulators...", random.uniform(0.2, 1)),
        ("\n>>> All systems green. Ready for operation.\n", 1.0),
    ]

    for message, delay in steps:
        print(message)
        time.sleep(delay)


def print_title():
    ascii_title="""
 |   |               |             \        __ __|            
 |   |   _` |   __|  |  /         _ \          |   _ \   __ \ 
 ___ |  (   |  (       < _____|  ___ \ _____|  |  (   |  |   |
_|  _| \__,_| \___| _|\_\      _/    _\       _| \___/  _|  _|                                                 
    """

    print(ascii_title)


def print_quit_message():
    print("\n[!] Aborted! The cake is a lie...\n")

def main():
    parser = argparse.ArgumentParser(description="Fake terminal hacker 'screensaver'. Example: autohaxaton --target=mytarget.lol")
    parser.add_argument('--target', type=str, help='Target hostname or IP', default=None)
    args = parser.parse_args()

    commands = load_lines_from_file("data/commands.txt")
    outputs = load_lines_from_file("data/outputs.txt")

    if not commands:
        print("Error: file 'commands.txt' is empty or missing.")
        exit(1)

    if not outputs:
        print("Error: file 'outputs.txt' is empty or missing.")
        exit(1)

    clear()
    print_title()
    print_initial_sequence()
    if args.target:
        print(f"Target acquired: {args.target}")
    else:
        args.target = "a random target!"
        print("No target specified.")
    print(f"Initiating automatic hacking procedure on {args.target}\n")
    time.sleep(2)

    fake_terminal_loop(commands, outputs)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_quit_message()