from datetime import datetime

def get_time():
    return f"🕒 Il est {datetime.now().strftime('%H:%M:%S')}."

TOOLS = {
    "get_time": get_time,
}
