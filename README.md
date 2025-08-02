A basic Python-based penetration testing toolkit featuring:

- **Port Scanner:** Scan common ports on a target host to identify open services.
- **FTP Brute-Forcer:** Attempt to brute-force FTP login using a username and a password list.
- **Banner Grabber:** Retrieve and display service banners from specified ports.

## Features

- Easy-to-use command-line interface
- No external dependencies except Python standard libraries and `ftplib`

## Requirements

- Python 3.x

## Usage

1. **Clone or download this repository.**
2. **Run the tool:**
    ```sh
    python test.py
    ```
3. **Follow the prompts:**
    - Enter the target IP or hostname.
    - Choose a module:
        - `1` for Port Scanner
        - `2` for FTP Brute-Forcer (requires FTP username and a password list file)
        - `3` for Banner Grabber (requires port number)

## Example

```
===============================
  PENETRATION TESTING TOOl
===============================
[1] Port Scanner
[2] FTP Brute-Forcer
[3] Banner Grabber

Enter target IP or hostname: 192.168.1.1
Choose module: 1
[+] Scanning ports on 192.168.1.1...
[+] Port 22 is open
[+] Port 80 is open
```

## Disclaimer

This tool is for educational and authorized testing purposes only. Do not use it on systems you do not own or have explicit permission to test.
