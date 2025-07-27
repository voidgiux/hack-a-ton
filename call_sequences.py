import time
import random


def simulate_console_sequence():
    play_sequence_from_file("data/msf_sequence.txt")


def simulate_hashcat_sequence():
    play_sequence_from_file("data/hashcat_sequence.txt")


def simulate_nmap_sequence():
    play_sequence_from_file("data/nmap_sequence.txt")


def simulate_hydra_sequence():
    play_sequence_from_file("data/hydra_sequence.txt")


def play_sequence_from_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        for line in lines:
            print(line)
            time.sleep(random.uniform(0.3, 0.7))
    except FileNotFoundError:
        print(f"[!] Sequence file {filepath} not found.")