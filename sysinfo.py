#!/usr/bin/env python3
"""
sysinfo.py – A professional, modular system information tool with CLI
"""
import argparse
import platform
import psutil
import socket
import time
import json
import os
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)


def get_system_info() -> dict:
    """
    Retrieve basic system information.

    Returns:
        dict: OS, node name, release, version, machine, and processor.
    """
    return {
        "system": platform.system(),
        "node_name": platform.node(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
    }


def get_cpu_info() -> dict:
    """
    Retrieve CPU details and usage statistics.

    Returns:
        dict: physical cores, total cores, usage per core, and total usage.
    """
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "total_cores": psutil.cpu_count(logical=True),
        "usage_per_core": psutil.cpu_percent(percpu=True),
        "total_usage": psutil.cpu_percent(),
    }


def get_memory_info() -> dict:
    """
    Retrieve virtual memory statistics.

    Returns:
        dict: total, available, used memory and percentage.
    """
    mem = psutil.virtual_memory()
    return {
        "total_gb": round(mem.total / (1024 ** 3), 2),
        "available_gb": round(mem.available / (1024 ** 3), 2),
        "used_gb": round(mem.used / (1024 ** 3), 2),
        "usage_percent": mem.percent,
    }


def get_disk_info() -> dict:
    """
    Retrieve disk partition usage details.

    Returns:
        dict: mapping of device to its usage stats (total, used, free, percent).
    """
    disks = {}
    for part in psutil.disk_partitions():
        try:
            usage = psutil.disk_usage(part.mountpoint)
            disks[part.device] = {
                "total_gb": round(usage.total / (1024 ** 3), 2),
                "used_gb": round(usage.used / (1024 ** 3), 2),
                "free_gb": round(usage.free / (1024 ** 3), 2),
                "usage_percent": usage.percent,
            }
        except PermissionError:
            continue  # skip partitions that cannot be accessed
    return disks


def get_network_info() -> dict:
    """
    Retrieve basic network information.

    Returns:
        dict: hostname and primary IP address.
    """
    hostname = socket.gethostname()
    try:
        ip = socket.gethostbyname(hostname)
    except socket.error:
        ip = "Unavailable"
    return {"hostname": hostname, "ip_address": ip}


def display_all() -> None:
    """
    Display all collected system information to the console.
    """
    sections = [
        ("SYSTEM INFORMATION", get_system_info()),
        ("CPU INFORMATION", get_cpu_info()),
        ("MEMORY INFORMATION", get_memory_info()),
        ("DISK INFORMATION", get_disk_info()),
        ("NETWORK INFORMATION", get_network_info()),
    ]
    for title, data in sections:
        print(Fore.CYAN + f"\n=== {title} ===")
        if isinstance(data, dict):
            for key, val in data.items():
                print(f"{key:<15}: {val}")
        else:
            print(data)


def export_to_file(path: str, fmt: str = "json") -> None:
    """
    Export collected information to a file.

    Args:
        path (str): Output file path.
        fmt (str): Format - 'json' or 'txt'.
    """
    info = {
        "system": get_system_info(),
        "cpu": get_cpu_info(),
        "memory": get_memory_info(),
        "disk": get_disk_info(),
        "network": get_network_info(),
    }
    if fmt == "json":
        with open(path, "w") as f:
            json.dump(info, f, indent=4)
    else:
        with open(path, "w") as f:
            for section, data in info.items():
                f.write(f"=== {section.upper()} ===\n")
                for key, val in data.items():
                    f.write(f"{key:<15}: {val}\n")
                f.write("\n")
    print(Fore.GREEN + f"Data successfully exported to {path}")


def live_monitor(interval: int = 2) -> None:
    """
    Live monitoring of CPU and memory usage.

    Args:
        interval (int): Seconds between updates.
    """
    try:
        while True:
            os.system("cls" if os.name == "nt" else "clear")
            cpu = psutil.cpu_percent()
            mem = psutil.virtual_memory().percent
            print(Fore.CYAN + "=== LIVE MONITORING ===")
            print(f"CPU Usage     : {cpu}%")
            print(f"Memory Usage  : {mem}%")
            time.sleep(interval)
    except KeyboardInterrupt:
        print(Fore.RED + "\nLive monitoring stopped by user.")


def parse_args() -> argparse.Namespace:
    """
    Parse command-line arguments.

    Returns:
        argparse.Namespace: Parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="System Info Tool: Display or export system metrics."
    )
    parser.add_argument(
        "-d", "--display", action="store_true",
        help="Display all system information"
    )
    parser.add_argument(
        "-e", "--export", metavar="FILE",
        help="Export information to specified file (supports .json or .txt)"
    )
    parser.add_argument(
        "-l", "--live", action="store_true",
        help="Start live CPU and memory monitoring"
    )
    parser.add_argument(
        "-i", "--interval", type=int, default=2,
        help="Interval in seconds for live monitoring (default: 2)"
    )
    return parser.parse_args()


def main() -> None:
    """
    Main entry point of the tool.
    """
    args = parse_args()

    if args.display:
        display_all()
    elif args.export:
        fmt = args.export.split('.')[-1]
        export_to_file(args.export, fmt)
    elif args.live:
        live_monitor(args.interval)
    else:
        # If no arguments, show help
        print(Style.BRIGHT + "No action specified. Use -h for help.")


if __name__ == "__main__":
    main()
