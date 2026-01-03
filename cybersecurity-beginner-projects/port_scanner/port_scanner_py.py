import socket
import time

# ========= إدخال المستخدم =========
target = input("Enter target (IP or hostname): ")
start_port = int(input("Enter start port: "))
end_port = int(input("Enter end port: "))

# ========= إعدادات =========
timeout = 3
open_ports = []

print("\nScanning started...\n")

# نبدأ حساب الوقت
start_time = time.time()

# ========= فحص مجموعة بورتات =========
for port in range(start_port, end_port + 1):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)

        result = s.connect_ex((target, port))

        if result == 0:
            print(f"[OPEN]     Port {port}")
            open_ports.append(port)
        else:
            print(f"[CLOSED]   Port {port}")

        s.close()

    except socket.timeout:
        print(f"[FILTERED] Port {port} (No response - possible firewall)")

    except Exception as e:
        print(f"[ERROR]    Port {port}: {e}")

# ========= حساب الزمن =========
end_time = time.time()
total_time = end_time - start_time

# ========= النتيجة النهائية =========
print("\nScan finished!")
print(f"Time taken: {total_time:.2f} seconds")

if open_ports:
    print("Open ports found:", open_ports)
else:
    print("No open ports found.")
