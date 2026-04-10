import socket
import time
import concurrent.futures

COMMON_PORT_SERVICES = {
    20: "FTP Data",
    21: "FTP Control",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    67: "DHCP Server",
    68: "DHCP Client",
    69: "TFTP",
    80: "HTTP",
    110: "POP3",
    119: "NNTP",
    123: "NTP",
    135: "MS RPC",
    137: "NetBIOS Name",
    138: "NetBIOS Datagram",
    139: "NetBIOS Session",
    143: "IMAP",
    161: "SNMP",
    179: "BGP",
    389: "LDAP",
    443: "HTTPS",
    445: "SMB",
    465: "SMTPS",
    514: "Syslog",
    587: "SMTP Submission",
    636: "LDAPS",
    873: "Rsync",
    993: "IMAPS",
    995: "POP3S",
    1433: "MSSQL",
    1521: "Oracle DB",
    1723: "PPTP",
    1883: "MQTT",
    2049: "NFS",
    2375: "Docker",
    3306: "MySQL",
    3389: "RDP",
    5060: "SIP",
    5432: "PostgreSQL",
    5672: "AMQP",
    5900: "VNC",
    6379: "Redis",
    8080: "HTTP Alt",
    8443: "HTTPS Alt",
    9000: "SonarQube / Web",
    9200: "Elasticsearch",
    27017: "MongoDB"
}

def build_scan_presets():
    return {
        "top100": {"label": "Top 100 Ports", "range": (1, 100)},
        "top1000": {"label": "Top 1000 Ports", "range": (1, 1000)},
        "web": {"label": "Web Ports", "range": (75, 9000)},
        "remote": {"label": "Remote Access Focus", "range": (20, 5900)},
        "database": {"label": "Database Focus", "range": (1433, 3306)},
        "full": {"label": "Full Scan (1-65535)", "range": (1, 65535)},
    }

def normalize_target(target):
    cleaned = target.replace("http://", "").replace("https://", "").strip("/")
    return cleaned

def resolve_target(target):
    cleaned = normalize_target(target)
    ip_address = socket.gethostbyname(cleaned)
    return cleaned, ip_address

def get_service_name(port):
    if port in COMMON_PORT_SERVICES:
        return COMMON_PORT_SERVICES[port]
    try:
        return socket.getservbyport(port)
    except Exception:
        return "Unknown"

def scan_single_port(ip, port, timeout):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(timeout)
            result = sock.connect_ex((ip, port))
            if result == 0:
                return {
                    "port": port,
                    "state": "open",
                    "service": get_service_name(port)
                }
    except Exception:
        return None
    return None

def run_port_scan(target, start_port, end_port, timeout=0.35, max_workers=300):
    started_at = time.time()

    try:
        cleaned_target, resolved_ip = resolve_target(target)
    except socket.gaierror:
        return {
            "target_input": target,
            "resolved_target": None,
            "resolved_ip": None,
            "open_ports": [],
            "closed_count": 0,
            "duration": 0,
            "error": "Invalid domain name or IP address."
        }

    total_ports = (end_port - start_port) + 1
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [
            executor.submit(scan_single_port, resolved_ip, port, timeout)
            for port in range(start_port, end_port + 1)
        ]

        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                open_ports.append(result)

    open_ports.sort(key=lambda x: x["port"])
    duration = round(time.time() - started_at, 2)
    closed_count = total_ports - len(open_ports)

    return {
        "target_input": target,
        "resolved_target": cleaned_target,
        "resolved_ip": resolved_ip,
        "open_ports": open_ports,
        "closed_count": closed_count,
        "duration": duration,
        "error": None
    }