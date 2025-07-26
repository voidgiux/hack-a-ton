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


def fake_terminal_loop(commands, outputs):
    print("> > > Starting hacking procedure < < <")
    print("Stay a while and listen..\n")
    time.sleep(1)

    iteration = 0
    try:
        while True:
            iteration += 1

            if random.random() < 0.10:
                print(random_line())
                time.sleep(random.uniform(0.3, 0.7))
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
        ("[*] System initiated.", 0.5),
        ("[+] Loading modules...", 0.5),
        ("[!] Done!", 0.5),
        ("[*] Loading dependencies...", 0.5),
        ("[*] Done!", 0.5),
        ("[!] Charging the faith capacitors...", 1.5),
        ("[*] Done!", 0.5),
        ("\nAll systems ready!\n", 1.0),
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