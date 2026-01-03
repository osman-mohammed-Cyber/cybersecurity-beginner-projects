import socket
import time

# Educational Port Scanner


# Ask the user to enter the target host (IP address or domain name)
target_host = input("Enter target IP address or hostname: ")

# Ask the user to define the port range
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

# Timeout value in seconds to avoid waiting too long on unresponsive ports
TIMEOUT = 3

# List to store open ports for summary
open_ports = []

print("\nStarting scan on:", target_host)
print(f"Scanning ports from {start_port} to {end_port}")
print("-" * 40)

# Record the time when the scan starts
scan_start_time = time.time()

# Loop through the specified port range
for port in range(start_port, end_port + 1):
    try:
        # Create a new TCP socket
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # Set timeout to control how long we wait for a response
        sock.settimeout(TIMEOUT)

        # Attempt to connect to the target host and port
        result = sock.connect_ex((target_host, port))

        # If result is 0, the port is open
        if result == 0:
            print(f"[OPEN] Port {port}")
            open_ports.append(port)

        # Close the socket after each attempt
        sock.close()

    except socket.gaierror:
        print("Hostname could not be resolved.")
        break

    except socket.error:
        print("Connection error occurred.")
        break

# Record the time when the scan ends
scan_end_time = time.time()

# Calculate total scan duration
total_time = scan_end_time - scan_start_time

print("\nScan completed.")
print("-" * 40)
print(f"Total time taken: {total_time:.2f} seconds")

# Display summary of open ports
if open_ports:
    print("Open ports found:")
    for port in open_ports:
        print(f"- Port {port}")
else:
    print("No open ports were detected.")

print("\nNote:")
print("This tool is intended for educational use only.")
print("Scan only systems you own or have permission to test.")
