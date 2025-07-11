
"""
Utility to log GPU usage statistics.
"""

def log_gpu_info():
    from agents.gpu_monitor import get_gpu_status
    status = get_gpu_status()
    print("GPU Status:", status)
