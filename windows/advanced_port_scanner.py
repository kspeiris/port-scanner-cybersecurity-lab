import argparse
import concurrent.futures
import json
import socket
from datetime import datetime
from typing import Dict, List, Optional


COMMON_PORTS = {
    20: "FTP-Data",
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP",
    68: "DHCP",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    111: "RPCbind",
    119: "NNTP",
    123: "NTP",
    135: "MSRPC",
    137: "NetBIOS-NS",
    138: "NetBIOS-DGM",
    139: "NetBIOS-SSN",
    143: "IMAP",
    161: "SNMP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    587: "SMTP Submission",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle",
    2049: "NFS",
    3306: "MySQL",
    3389: "RDP",
    5432: "PostgreSQL",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
}


def resolve_target(target: str) -> str:
    try:
        return socket.gethostbyname(target)
    except socket.gaierror as exc:
        raise ValueError(f"Could not resolve target: {target}") from exc


def get_service_name(port: int) -> str:
    return COMMON_PORTS.get(port, "Unknown")


def grab_banner(host: str, port: int, timeout: float = 2.0) -> Optional[str]:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            sock.connect((host, port))

            if port in (80, 8080, 8000):
                request = f"HEAD / HTTP/1.0\r\nHost: {host}\r\n\r\n"
                sock.sendall(request.encode())
            elif port in (21, 22, 25, 110, 143):
                pass
            else:
                try:
                    sock.sendall(b"\r\n")
                except OSError:
                    pass

            data = sock.recv(1024)
            if data:
                banner = data.decode(errors="ignore").strip()
                return " ".join(banner.split())
    except (socket.timeout, ConnectionRefusedError, OSError):
        return None

    return None


def scan_port(host: str, port: int, timeout: float = 1.0) -> Optional[Dict]:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((host, port))

            if result == 0:
                service = get_service_name(port)
                banner = grab_banner(host, port, timeout)
                return {
                    "port": port,
                    "state": "open",
                    "service": service,
                    "banner": banner if banner else "Not available",
                }
    except OSError:
        return None

    return None


def scan_host(
    host: str,
    start_port: int,
    end_port: int,
    threads: int = 100,
    timeout: float = 1.0,
) -> List[Dict]:
    results: List[Dict] = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=threads) as executor:
        future_to_port = {
            executor.submit(scan_port, host, port, timeout): port
            for port in range(start_port, end_port + 1)
        }

        for future in concurrent.futures.as_completed(future_to_port):
            result = future.result()
            if result:
                results.append(result)

    results.sort(key=lambda item: item["port"])
    return results


def save_results(filename: str, target: str, ip: str, results: List[Dict]) -> None:
    output = {
        "target": target,
        "resolved_ip": ip,
        "scan_time": datetime.now().isoformat(),
        "open_ports": results,
    }

    with open(filename, "w", encoding="utf-8") as file_handle:
        json.dump(output, file_handle, indent=4)


def print_results(target: str, ip: str, results: List[Dict]) -> None:
    print("\n" + "=" * 72)
    print(f"Scan Results for: {target} ({ip})")
    print("=" * 72)
    print(f"{'PORT':<10}{'STATE':<10}{'SERVICE':<20}{'BANNER'}")
    print("-" * 72)

    if not results:
        print("No open ports found.")
        return

    for item in results:
        print(
            f"{item['port']:<10}{item['state']:<10}{item['service']:<20}{item['banner']}"
        )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Advanced TCP Port Scanner with Banner Grabbing"
    )
    parser.add_argument("target", help="Target IP address or hostname")
    parser.add_argument("--start", type=int, default=1, help="Start port")
    parser.add_argument("--end", type=int, default=1024, help="End port")
    parser.add_argument("--threads", type=int, default=100, help="Number of threads")
    parser.add_argument(
        "--timeout", type=float, default=1.0, help="Socket timeout in seconds"
    )
    parser.add_argument("--output", help="Save results to JSON file")

    args = parser.parse_args()

    try:
        ip = resolve_target(args.target)
    except ValueError as exc:
        print(exc)
        return

    print(f"[*] Scanning target : {args.target}")
    print(f"[*] Resolved IP    : {ip}")
    print(f"[*] Port range     : {args.start}-{args.end}")
    print(f"[*] Threads        : {args.threads}")
    print(f"[*] Timeout        : {args.timeout}s")

    start_time = datetime.now()
    results = scan_host(ip, args.start, args.end, args.threads, args.timeout)
    end_time = datetime.now()

    print_results(args.target, ip, results)
    print(f"\n[*] Scan duration: {end_time - start_time}")

    if args.output:
        save_results(args.output, args.target, ip, results)
        print(f"[+] Results saved to {args.output}")


if __name__ == "__main__":
    main()
