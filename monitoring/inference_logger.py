
"""
Logs inference request and response times.
"""

import datetime

def log_inference(prompt: str, model: str, output_path: str):
    now = datetime.datetime.now()
    log = {
        "timestamp": now.isoformat(),
        "prompt": prompt,
        "model": model,
        "output": output_path
    }
    print("Inference Log:", log)
