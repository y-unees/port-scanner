import socket
from datetime import datetime
import argparse

def get_service(port):
    try:
        return socket.getservbyport(port)
    except OSError:
        return 'Unknown'

def get_hostname(target):
    try:
        return socket.gethostbyaddr(target)[0]
    except (socket.herror, socket.gaierror):
        return 'Host name not found!'

def grab_banner(s):
    try:
        return s.recv(1024).decode().strip()
    except Exception:
        return None

# ---- ARGUMENT PARSER ----
parser = argparse.ArgumentParser(description="Simple Port Scanner")
parser.add_argument("target", help="Target IP address or hostname")
parser.add_argument("-p", "--port", type=int, help="Scan a specific port")
parser.add_argument("-p-", "--port_range", action="store_true", help="Scan all 65535 ports")
parser.add_argument("-v", "--verbosity", action="count", default=0, help="Increase output verbosity")

args = parser.parse_args()

# ---- PORT RANGE ----
if args.port:
    start_port = end_port = args.port
elif args.port_range:
    start_port = 1
    end_port = 65535
else:
    start_port = 1
    end_port = 1024

target = args.target
start_time = datetime.now()

# ---- INFO HEADER ----
print('_' * 60)
print(f"Scanning target: {target}")
print(f"Started at: {start_time}")
print('_' * 60)

# ---- INIT RESULTS ----
open_ports = []
filtered_ports = []
closed_ports = []

# Resolve hostname once
hostname = get_hostname(target)

# ---- PORT SCAN LOOP ----
for port in range(start_port, end_port + 1):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(0.5)

    try:
        result = s.connect_ex((target, port))
        if result == 0:
            service = get_service(port)
            banner = grab_banner(s)
            open_ports.append((port, service, banner))
            if args.verbosity > 0:
                if banner:
                    print(f"[OPEN] Port {port} ({service}) - {banner}")
                else:
                    print(f"[OPEN] Port {port} ({service})")
        else:
            closed_ports.append(port)
            if args.verbosity > 1:
                print(f"[CLOSED] Port {port}")
    except socket.timeout:
        filtered_ports.append(port)
        if args.verbosity > 1:
            print(f"[FILTERED] Port {port}")
    finally:
        s.close()

end_time = datetime.now()
duration = end_time - start_time

# ---- SUMMARY OUTPUT ----
print('\n' + '_' * 60)
print(f"Scan completed at: {end_time}")
print(f"Scan duration: {duration}")
print('_' * 60)

print(f"Hostname: {hostname}")
print(f"\nTotal Open Ports: {len(open_ports)}")

for port, service, banner in open_ports:
    output = f"  Port {port}: {service}"
    if banner:
        output += f" | {banner}"
    print(output)

if start_port != end_port:
    print(f"\nTotal Filtered Ports: {len(filtered_ports)}")
    print(f"Total Closed Ports: {len(closed_ports)}")
