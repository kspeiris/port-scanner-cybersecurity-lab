Advanced TCP Port Scanner Lab (WSL Side)

Files in this folder:
- advanced_port_scanner.py
- results/

Run these commands from this folder inside WSL:

1. Check Python:
python3 --version

2. Install lab tools if needed:
sudo apt update
sudo apt install python3 python3-pip nmap openssh-server net-tools -y

3. Scan WSL localhost:
python3 advanced_port_scanner.py 127.0.0.1 --start 1 --end 1024 --output results/wsl_localhost.json

4. Scan Windows from WSL:
python3 advanced_port_scanner.py <windows-ip> --start 1 --end 1024 --output results/windows_from_wsl.json

5. Start SSH in WSL:
sudo service ssh start

6. Start a simple HTTP test server in WSL:
python3 -m http.server 8000

7. Scan a smaller range with a longer timeout:
python3 advanced_port_scanner.py <target-ip> --start 20 --end 100 --timeout 2

8. Compare with Nmap:
nmap -sV <target-ip>

Suggested workflow:
- Run the scanner against 127.0.0.1 in WSL.
- Find the WSL IP with `ip a`.
- Scan your Windows IP from WSL.
- Start SSH and a Python HTTP server in WSL.
- Scan the WSL IP from Windows.
- Save each result JSON inside results/.

Use this only in your own lab and on systems you are authorized to test.
