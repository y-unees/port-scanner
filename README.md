# Simple Port Scanner — Python

A lightweight TCP port scanner that detects basic open ports, performs banner grabbing as well as provides general verbosity. This tool is useful for basic network diagnosis, educational purposes and how port scanning is performed under the hood.
---
## Features

- Scan a **specific port**, **common ports**(1-1024) or **all the ports**(65535).
- Identifies **known** services based on ports.
- Attempts **banner grabbing** for open services
- Supports **verbosity flags** (`-v`, `-vv`) for more detailed output
- Lightweight and dependency free, uses only Python standard libraries

## Requirements

- Python 3.X
- Works on Linux [Not tested on Windows or Mac OS]
- Built primarily for Linux

## Process

The script follows a simple and systematic process to scan a given IP address:

1. **Argument Parsing**
   - Accepts the target IP and optional flags (`-p`, `-p-`, `-v`, `-vv`) using Python's `argparse`.

2. **Hostname Resolution**
   - Attempts to resolve the hostname of the target using reverse DNS (`gethostbyaddr`). If not found, it continues without it.

3. **Port Range Selection**
   - If no port is specified, it defaults to scanning ports 1 to 1024.
   - If `-p` is used, it scans only the specified port.
   - If `-p-` is used, it scans the entire range (1–65535).

4. **Socket Connection**
   - For each port in the range:
     - Tries to establish a TCP connection using `socket.connect_ex()`.
     - If the port is open (`result == 0`), it attempts to:
       - Identify the service (`getservbyport`)
       - Grab a banner (if any) from the service
     - If the connection times out, it's marked as **filtered**
     - Otherwise, it's marked as **closed**

5. **Verbosity Control**
   - If `-v` is used: only open ports are shown during the scan.
   - If `-vv` is used: open, closed, and filtered ports are shown in real-time.

6. **Summary Output**
   - After scanning, it prints:
     - Open ports and their banners (if available)
     - Totals for filtered and closed ports (only shown when scanning more than one port)
     - Hostname (if resolved)
     - Duration of the scan

## Installation & Setup

You can easily run this script on Kali Linux (or any Linux system) using the steps below.

1. **Clone the Repository**  
Use `git` to download the project from GitHub:
```bash
git clone https://github.com/your-username/port-scanner.git
```

2. **Navigate to project directory**
```
cd port-scanner
```

3. **Run the script**
Use Python3 to run the script
```
python3 scanner.py [target ip] [options] 
```
Example:
```
python3 scanner.py 10.0.2.5
```

4. **OPTIONAL: Make it Globally Executable:**

To run the script globally, follow the instructions.

**a. Copy it to */usr/local/bin***
```
sudo cp scanner.py /usr/local/bin/portscan
```

**b. Make it executable**
```
sudo chmod +x /usr/local/bin/portscan
```

**c. Now it can be run like this:**
```
portscan [target ip] 
```

## Usage

### Basic Port Scan
```
bash 
python3 scanner.py [ip]
```

### Specific Port Scan
```
bash
python3 scanner.py [ip] -p [port]
```

### All ports scan
```
bash
python3 scanner.py [ip] -p-
```

### Show verbose output
```
bash
python3 scanner.py [ip] -v
python3 scanner.py [ip] -vv
```

## Example Output
```
user@user:~$ python3 scanner.py 10.0.2.5
____________________________________________________________
Scanning target: 10.0.2.5
Started at: 2025-08-01 17:41:35.953041
____________________________________________________________

____________________________________________________________
Scan completed at: 2025-08-01 17:41:40.969050
Scan duration: 0:00:05.016009
____________________________________________________________
Hostname: Host name not found!

Total Open Ports: 12
  Port 21: ftp | 220 (vsFTPd 2.3.4)
  Port 22: ssh | SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1
  Port 23: telnet
  Port 25: smtp | 220 metasploitable.localdomain ESMTP Postfix (Ubuntu)
  Port 53: domain
  Port 80: http
  Port 111: sunrpc
  Port 139: netbios-ssn
  Port 445: microsoft-ds
  Port 512: exec | Where are you?
  Port 513: login
  Port 514: shell

Total Filtered Ports: 0
Total Closed Ports: 1012
```

## Notes

- Banner grabbing is passive and may not work on all services.
- Hostname resolution is attempted but may fail for internal/private IPs.
- Filtered ports are those that timeout (typically due to firewalls).

## Suggestions
📬 Email: [Mail](mailto:why.unees29@gmail.com)
Your feedback is much appreciated!

## Author 

**Unish Dhungana**  
🔗 GitHub: [@y-unees](https://github.com/y-unees)  
🌐 Website: [unishdhungana.com.np](https://www.unishdhungana.com.np)
