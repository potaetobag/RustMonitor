# ===========================================
# RustMonitor
# Version: 1.0
# Owner: potaetobag
# Description: Python script to monitor a Rust
#              Dedicated Server's RCON port and
#              send alerts via Discord webhook
#              when the server goes offline or
#              comes back online.
# ===========================================

import socket
import requests
import time

# Configuration
SERVER_IP = "127.0.0.1"  # Replace with your Rust server's IP
PORT = 28016  # Rust port to check (rcon.port)
DISCORD_WEBHOOK_URL = "URL"
CHECK_INTERVAL = 60  # Time in seconds between checks

def is_port_open(ip, port):
    """Check if a port is open on the given IP."""
    print(f"🔍 Checking port {port} on {ip}...")
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((ip, port))
        sock.close()

        if result == 0:
            print(f"✅ Port {port} on {ip} is open.")
            return True
        else:
            print(f"❌ Port {port} on {ip} is closed or unreachable.")
            return False
    except socket.error as e:
        print(f"⚠️ Socket error: {e}")
        return False

def send_discord_notification(message):
    """Send a notification to Discord."""
    print(f"📢 Sending Discord notification: {message}")
    payload = {"content": message}
    try:
        response = requests.post(DISCORD_WEBHOOK_URL, json=payload)
        if response.status_code == 204:
            print("✅ Notification sent to Discord.")
        else:
            print(f"❌ Failed to send notification: {response.status_code}, {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error sending notification: {e}")

def main():
    server_down = False

    try:
        while True:
            if not is_port_open(SERVER_IP, PORT):
                if not server_down:
                    send_discord_notification("🚨 The Rust server is down!")
                    server_down = True
            else:
                if server_down:
                    send_discord_notification("🚦 Server is back online! Players may now re-join. 🚦")
                    server_down = False

            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        print("\n🛑 Monitoring stopped by user. Exiting gracefully.")

if __name__ == "__main__":
    main()
