Advanced TCP Port Scanner Lab (Windows Side)

Files in this folder:
- advanced_port_scanner.py
- results\

Run these commands from this folder in Windows PowerShell:

1. Check Python:
python --version

If `python` hangs or opens the Microsoft Store alias on your machine, use:
& "C:\Users\kavin\AppData\Local\Programs\Python\Python313\python.exe" --version

2. Scan Windows localhost:
python advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024 --output results/windows_localhost.json --csv-output results/windows_localhost.csv

Interpreter fallback:
& "C:\Users\kavin\AppData\Local\Programs\Python\Python313\python.exe" advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024 --output results/windows_localhost.json --csv-output results/windows_localhost.csv

3. Scan WSL from Windows:
python advanced_port_scanner.py <wsl-ip> --start 1 --end 1024 --output results/wsl_from_windows.json --csv-output results/wsl_from_windows.csv

4. Scan a smaller range with a longer timeout:
python advanced_port_scanner.py <target-ip> --start 20 --end 100 --timeout 2

5. Start a simple Windows HTTP test server:
python -m http.server 8080

Then scan it from WSL:
python3 advanced_port_scanner.py <windows-ip> --start 8075 --end 8085 --output results/windows_http_from_wsl.json --csv-output results/windows_http_from_wsl.csv

Useful options:
- `--csv-output results/file.csv` saves a spreadsheet-friendly copy.
- `--no-color` disables ANSI color if your terminal renders it poorly.

Suggested workflow:
- Run the scanner against 127.0.0.1 on Windows.
- Start SSH and HTTP services in WSL.
- Scan the WSL IP from Windows.
- Save each result JSON inside results\.
- Compare findings with Nmap.

Use this only in your own lab and on systems you are authorized to test.
