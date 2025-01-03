import socket
import requests
import time

# Configuration
SERVER_IP = "IP"  # Replace with your Rust server's IP
PORT = 26016  # Rust port to check
DISCORD_WEBHOOK_URL = "URL"  # Replace with your Discord webhook URL
CHECK_INTERVAL = 60  # Time in seconds between checks

def is_port_open(ip, port):
    """Check if a port is open on the given IP."""
    print(f"Checking port {port} on {ip}...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)  # Set timeout to prevent hanging
        result = sock.connect_ex((ip, port))
        sock.close()
        
        if result == 0:
            print(f"Port {port} on {ip} is open.")
            return True
        else:
            print(f"Port {port} on {ip} is closed or unreachable.")
            return False
    except socket.error as e:
        print(f"Socket error: {e}")
        return False

def send_discord_notification(message):
    """Send a notification to Discord."""
    print(f"Sending Discord notification: {message}")
    payload = {"content": message}
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("Notification sent to Discord.")
        else:
            print(f"Failed to send notification: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Error sending notification: {e}")

def main():
    server_down = False

    try:
        while True:
            if not is_port_open(SERVER_IP, PORT):
                if not server_down:
                    send_discord_notification(f"🚨 The Rust server is down!")
                    server_down = True
            else:
                if server_down:
                    print("Server is back online (no notification sent).")
                    server_down = False
            
            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\nMonitoring stopped by user. Exiting gracefully.")

if __name__ == "__main__":
    main()
