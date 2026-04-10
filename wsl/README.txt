Advanced TCP Port Scanner
WSL Usage Guide

This folder contains the WSL-side scanner for the Windows + WSL lab.

Use it only on systems you own or are authorized to test.

---

Features

- TCP port scanning
- Service identification using common ports
- Basic banner grabbing
- JSON output support
- CSV output support
- Optional color output with `--no-color` to disable

---

Files in This Folder

- `advanced_port_scanner.py`
- `results/`

---

Environment Setup

Check Python:

```bash
python3 --version
```

Install lab tools if needed:

```bash
sudo apt update
sudo apt install python3 python3-pip nmap openssh-server net-tools -y
```

---

Quick Start

From inside this `wsl` folder:

```bash
python3 advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024
```

---

Usage Examples

1. Scan WSL localhost

```bash
python3 advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024 --output results/wsl_localhost.json --csv-output results/wsl_localhost.csv
```

2. Scan Windows from WSL

Current example Windows IP:

```text
172.23.176.1
```

```bash
python3 advanced_port_scanner.py 172.23.176.1 --start 1 --end 1024 --output results/windows_from_wsl.json --csv-output results/windows_from_wsl.csv
```

3. Start SSH in WSL

```bash
sudo service ssh start
sudo service ssh status
```

4. Start a simple HTTP test server in WSL

```bash
python3 -m http.server 8000
```

5. Scan a smaller range with a longer timeout

```bash
python3 advanced_port_scanner.py 172.23.176.1 --start 20 --end 100 --timeout 2
```

6. Compare with Nmap

```bash
nmap -sV 172.23.176.1
```

---

Useful Options

- `--output results/file.json` saves JSON results
- `--csv-output results/file.csv` saves CSV results
- `--no-color` disables ANSI color output
- `--timeout 2` increases the socket timeout

---

Suggested Workflow

- Scan `127.0.0.1` in WSL
- Find the WSL IP using `ip a`
- Scan the Windows IP from WSL
- Start SSH and an HTTP server in WSL
- Scan the WSL IP from Windows
- Save JSON and CSV results in `results/`
- Compare findings with Nmap

---

Notes

- Replace the sample IPs if addresses change after a restart
- Some protocols will not return a readable banner
- WSL NAT networking can affect which services are reachable
