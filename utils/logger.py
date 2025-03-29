import os, json
from datetime import datetime

os.makedirs("outputs", exist_ok=True)

def log_output(step, data):
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filepath = f"outputs/{timestamp}_{step}.json"
    with open(filepath, "w") as f:
        json.dump({step: data}, f, indent=2)
    return data