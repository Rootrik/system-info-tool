import platform
import psutil
import socket
import datetime
from colorama import Fore, Style, init

# Inicializace colorama
init(autoreset=True)

def get_ip_address():
    try:
        # Vytvoříme socket a zjistíme IP adresu z vnější sítě
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except Exception:
        ip = "Nelze zjistit"
    return ip

def get_system_info():
    print(Fore.CYAN + Style.BRIGHT + "\n=== System Information ===\n")
    
    print(Fore.YELLOW + f"OS: {Fore.WHITE}{platform.system()} {platform.release()}")
    print(Fore.YELLOW + f"CPU: {Fore.WHITE}{platform.processor()}")
    print(Fore.YELLOW + f"Počet jader: {Fore.WHITE}{psutil.cpu_count(logical=True)}")
    print(Fore.YELLOW + f"RAM: {Fore.WHITE}{round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")
    
    print(Fore.YELLOW + f"IP adresa: {Fore.WHITE}{get_ip_address()}")
    
    boot_time_timestamp = psutil.boot_time()
    boot_time = datetime.datetime.fromtimestamp(boot_time_timestamp)
    uptime = datetime.datetime.now() - boot_time
    print(Fore.YELLOW + f"Uptime: {Fore.WHITE}{uptime.days} dní {uptime.seconds // 3600} hodin\n")

if __name__ == "__main__":
    get_system_info()
