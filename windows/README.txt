Advanced TCP Port Scanner
Windows Usage Guide

This folder contains the Windows-side scanner for the Windows + WSL lab.

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
- `results\`

---

Python Check

From this folder in PowerShell:

```powershell
python --version
```

If `python` opens the Microsoft Store alias on your machine, use:

```powershell
& "C:\Users\kavin\AppData\Local\Programs\Python\Python313\python.exe" --version
```

---

Quick Start

If you are already inside the `windows` folder:

```powershell
python advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024
```

If you are in the repo root:

```powershell
& "C:\Users\kavin\AppData\Local\Programs\Python\Python313\python.exe" .\windows\advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024
```

---

Usage Examples

1. Scan Windows localhost

```powershell
python advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024 --output results/windows_localhost.json --csv-output results/windows_localhost.csv
```

Interpreter fallback:

```powershell
& "C:\Users\kavin\AppData\Local\Programs\Python\Python313\python.exe" advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024 --output results/windows_localhost.json --csv-output results/windows_localhost.csv
```

2. Scan WSL from Windows

Current example WSL IP:

```text
172.23.180.180
```

```powershell
python advanced_port_scanner.py 172.23.180.180 --start 1 --end 1024 --output results/wsl_from_windows.json --csv-output results/wsl_from_windows.csv
```

3. Scan a smaller range with a longer timeout

```powershell
python advanced_port_scanner.py 172.23.180.180 --start 20 --end 100 --timeout 2
```

4. Start a simple Windows HTTP test server

```powershell
python -m http.server 8080
```

Then scan it from WSL:

```bash
python3 advanced_port_scanner.py 172.23.176.1 --start 8075 --end 8085 --output results/windows_http_from_wsl.json --csv-output results/windows_http_from_wsl.csv
```

---

Useful Options

- `--output results/file.json` saves JSON results
- `--csv-output results/file.csv` saves CSV results
- `--no-color` disables ANSI color output
- `--timeout 2` increases the socket timeout

---

PowerShell Note

Do not type placeholder text like `<wsl-ip>` literally in PowerShell.
Replace it with the real IP address without angle brackets.

Wrong:

```powershell
python advanced_port_scanner.py <wsl-ip> --start 1 --end 1024
```

Correct:

```powershell
python advanced_port_scanner.py 172.23.180.180 --start 1 --end 1024
```

---

Suggested Workflow

- Scan `127.0.0.1` on Windows
- Start SSH in WSL
- Start `python3 -m http.server 8000` in WSL
- Scan the WSL IP from Windows
- Save JSON and CSV results in `results\`
- Compare findings with Nmap

---

Notes

- WSL IP addresses may change after restarts
- Windows Firewall can affect cross-environment scans
- Some open ports will not return a banner
