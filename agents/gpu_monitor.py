# agents/gpu_monitor.py

import GPUtil

def get_gpu_status():
    """
    Returns basic GPU memory usage and availability.
    """
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            return {"status": "No GPU found"}
        
        gpu = gpus[0]  # Use the first GPU
        return {
            "id": gpu.id,
            "name": gpu.name,
            "memory_total": gpu.memoryTotal,
            "memory_used": gpu.memoryUsed,
            "memory_free": gpu.memoryFree,
            "load": gpu.load
        }
    except Exception as e:
        return {"error": str(e)}
