RustMonitor is a Python script that monitors the availability of your Rust game server by checking its port status. If the server goes down, it sends a notification to your Discord channel using a webhook. With RustMonitor, you can keep your server running smoothly and stay informed of any downtime.

## Features
* Port Availability Check: Monitors server IP and port for accessibility.
* Discord Notifications: Alerts sent to a Discord channel via webhook.
* Customizable Check Interval: Configure how often the script checks the server.
* Windows Task Scheduler Support: Easily set up the script to run continuously on Windows.

![Screenshot sent from Rust to the Discord channel](https://potaetobag.live/imgs/potaetobag-rustmonitor-discord.png)  

## Prerequisites
1. Install Python
* Download Python from the [official website](https://www.python.org/).
* During installation, ensure you check Add Python to PATH before proceeding.

2. Install Required Python Library
* Open Command Prompt (`Win + R`, type `cmd`, and press **Enter**).
* Install the requests library by running:
```
pip install requests
```

## How to Use
Edit the script:
Set `SERVER_IP` to your Rust server's IP address.
Adjust `PORT` if your server uses a non-default port (default is 26015).
Replace `DISCORD_WEBHOOK_URL` with your Discord webhook URL.

Step 1: Open Task Scheduler
* Press `Win + S`, type **Task Scheduler**, and open it.

Step 2: Create a New Task
* In **Task Scheduler**, click **Create Task** on the right-hand panel.

Step 3: General Settings
* Name the task (e.g., "RustMonitor").
* Select **Run whether user is logged on or not**.
* Check **Run with highest privileges**.

Step 4: Trigger
* Go to the **Triggers** tab and click New.
* Set the trigger to **At startup** or **Daily** with a specific time.
* Click **OK**.

Step 5: Action
* Go to the **Actions** tab and click **New**.
* Choose **Start a Program**.
* In the Program/script field, browse and select your `RustMonitor.py` file.
* Click **OK**.

Step 6: Conditions
* Optional: Adjust conditions like only running when the computer is idle.

Step 7: Save and Test
* Click **OK** to save the task.
* Right-click your task in **Task Scheduler** and select **Run** to test it.
