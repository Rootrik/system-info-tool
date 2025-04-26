# 🖥️ System Info Tool

A simple Python CLI tool that displays essential system information in a clean and colored format.

## 🚀 Features

- Operating system name and version
- CPU model and number of cores
- Total RAM
- Local IP address
- System uptime

## 🧰 Requirements

- Python 3.7+
- Works on Linux and Windows
- Recommended to use a virtual environment

## ⚙️ Installation

Create and activate a virtual environment:

python3 -m venv venv
source venv/bin/activate

Install dependencies:

pip install psutil colorama

## ▶️ Usage

Run the tool using:

python sysinfo.py

## 📌 Notes

- Tested on Parrot OS and Windows 11
- Displays local IP using socket logic (won't show public IP)
- Easy to expand with more system info (GPU, disk usage, etc.)

## 🧠 Author

Created by Rootrik 🔥  
Learning full-stack development & ethical hacking.
