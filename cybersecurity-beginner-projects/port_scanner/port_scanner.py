import socket
import threading
from queue import Queue

# Ask the user for target information
target = input("Enter target IP or hostname: ")
start_port = int(input("Start port: "))
end_port = int(input("End port: "))

# Set a default timeout for socket connections (in seconds)
# This prevents the scanner from waiting too long on unresponsive ports
socket.setdefaulttimeout(0.3)

# Queue to store ports that need to be scanned
port_queue = Queue()

# List to store discovered open ports
open_ports = []


def scan_port():
    """
    Worker function that scans ports from the queue.
    Each thread runs this function to scan multiple ports concurrently.
    """
    while not port_queue.empty():
        port = port_queue.get()
        try:
            # Create a TCP socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # Attempt to connect to the target on the given port
            result = s.connect_ex((target, port))

            # If connection is successful, the port is open
            if result == 0:
                open_ports.append(port)

            # Close the socket after each attempt
            s.close()

        except:
            # Ignore errors to keep the scan running smoothly
            pass

        # Mark the current task as done
        port_queue.task_done()


# Add all ports in the selected range to the queue
for port in range(start_port, end_port + 1):
    port_queue.put(port)

# Create and start multiple threads for faster scanning
threads = []
for _ in range(50):  # Number of threads (balanced for speed and safety)
    t = threading.Thread(target=scan_port)
    threads.append(t)
    t.start()

# Wait for all threads to finish
for t in threads:
    t.join()

# Display scan results
print("\nScan completed.")

if open_ports:
    print("Open ports found:")
    for port in sorted(open_ports):
        print(f"- Port {port}")
else:
    print("No open ports found.")
