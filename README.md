# Advanced Port Scanner Cybersecurity Lab

This repo is set up for a safe Windows + WSL networking lab using a Python TCP port scanner with basic banner grabbing.

Use it only on systems you own or are explicitly authorized to test.

## Project Layout

- `windows/advanced_port_scanner.py`: scanner for running from Windows terminals
- `wsl/advanced_port_scanner.py`: scanner for running inside WSL
- `windows/results/`: suggested JSON and CSV output folder for Windows-side runs
- `wsl/results/`: suggested JSON and CSV output folder for WSL-side runs

## Features

- TCP connect scan
- Common service name lookup
- Basic banner grabbing for selected services
- JSON export
- CSV export with `--csv-output`
- Optional ANSI colors with `--no-color` to disable
- Automatic output directory creation

## Quick Start

### Windows

Run from the `windows/` folder:

```bash
python advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024 --output results/windows_localhost.json --csv-output results/windows_localhost.csv
```

### WSL

Run from the `wsl/` folder:

```bash
python3 advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024 --output results/wsl_localhost.json --csv-output results/wsl_localhost.csv
```

## Suggested Lab Flow

1. Scan Windows localhost.
2. Scan WSL localhost.
3. Scan Windows from WSL.
4. Scan WSL from Windows.
5. Start `ssh` in WSL and rescan port `22`.
6. Start `python3 -m http.server 8000` in WSL and rescan around port `8000`.
7. Optionally start `python -m http.server 8080` on Windows and scan it from WSL.
8. Compare your findings with `nmap -sV`.

## Example Commands

### Windows scans WSL

```bash
python advanced_port_scanner.py <wsl-ip> --start 1 --end 1024 --output results/wsl_from_windows.json --csv-output results/wsl_from_windows.csv
```

### WSL scans Windows

```bash
python3 advanced_port_scanner.py <windows-ip> --start 1 --end 1024 --output results/windows_from_wsl.json --csv-output results/windows_from_wsl.csv
```

### Narrow scan with longer timeout

```bash
python3 advanced_port_scanner.py <target-ip> --start 20 --end 100 --timeout 2
```

## Notes

- `python` is usually correct on Windows and `python3` is usually correct in WSL.
- Some open services will not return a banner.
- WSL IP addresses may change after restarts.
- Windows Firewall may affect cross-environment scans.
