# agents/model_selector.py

def select_model(gpu_info: dict) -> str:
    """
    Selects a suitable model based on available GPU memory.
    """
    try:
        memory_free = gpu_info.get("memory_free", 0)

        if memory_free > 10000:
            return "stable-diffusion-xl"
        elif memory_free > 5000:
            return "stable-diffusion-v1-5"
        else:
            return "stable-diffusion-mini"
    except Exception as e:
        print("Model selection failed:", e)
        return "stable-diffusion-v1-5"
