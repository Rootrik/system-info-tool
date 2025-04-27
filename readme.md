# System Info Tool

A professional, modular Python tool to display or export detailed system metrics via Command Line Interface (CLI).

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python) 
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20MacOS-lightgrey)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📋 Features

- View detailed system information (OS, CPU, Memory, Disk, Network)
- Export system info to **JSON** or **TXT** file
- Live monitoring of CPU and Memory usage
- Cross-platform support (Windows, Linux, macOS)
- User-friendly CLI with colored output

---

## 🚀 Installation

Clone the repository:

```
git clone https://github.com/Rootrik/system-info-tool.git
cd system-info-tool
```

Install required packages:

```
pip install -r requirements.txt
```

---

## 🛠️ Usage

| Command | Description |
|:--------|:------------|
| `python sysinfo.py --display` | Display all system information |
| `python sysinfo.py --export systeminfo.json` | Export info to JSON file |
| `python sysinfo.py --export report.txt` | Export info to TXT file |
| `python sysinfo.py --live` | Start live monitoring (every 2 sec) |
| `python sysinfo.py --live --interval 5` | Live monitoring with 5s interval |

View help:

```
python sysinfo.py --help
```

---

## 📦 Example Screenshots

**Display System Information:**

```
=== SYSTEM INFORMATION ===
system         : Windows
node_name      : UserPC
release        : 10
version        : 10.0.19045
machine        : AMD64
processor      : Intel(R) Core(TM) i7-9700K CPU @ 3.60GHz
...
```

**Live Monitoring:**

```
=== LIVE MONITORING ===
CPU Usage     : 12.5%
Memory Usage  : 37.8%
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 🤝 Credits

Developed with ❤️ by Rootrik
