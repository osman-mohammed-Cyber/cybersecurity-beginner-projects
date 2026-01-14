# ============================================
# Basic Network Analyzer (Educational Project)
# ============================================
# This tool resolves a hostname to an IP address
# and checks basic network reachability using ping.
# It is intended for learning purposes only.

import socket
import subprocess
import platform


def resolve_target(target):
    """
    Resolves a hostname or IP address to an IP address.
    Returns the resolved IP or None if resolution fails.
    """
    try:
        ip_address = socket.gethostbyname(target)
        return ip_address
    except socket.gaierror:
        return None


def ping_target(ip_address):
    """
    Sends a single ping request to the target IP.
    Returns True if reachable, False otherwise.
    """
    system_name = platform.system().lower()

    if system_name == "windows":
        command = ["ping", "-n", "1", ip_address]
    else:
        command = ["ping", "-c", "1", ip_address]

    result = subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    return result.returncode == 0


def main():
    print("=== Basic Network Analyzer ===")

    target = input("Enter a hostname or IP address: ").strip()

    if not target:
        print("Invalid input. Please enter a valid hostname or IP.")
        return

    ip_address = resolve_target(target)

    if ip_address is None:
        print("Failed to resolve the target. Please check the input.")
        return

    print(f"Resolved IP Address: {ip_address}")

    reachable = ping_target(ip_address)

    if reachable:
        status = "Reachable"
    else:
        status = "Unreachable"

    print("\n--- Analysis Result ---")
    print(f"Target   : {target}")
    print(f"IP       : {ip_address}")
    print(f"Status   : {status}")

    print("\nNote: This tool is for educational purposes only.")


if __name__ == "__main__":
    main()
