
"""
Benchmark model generation time.
"""

import time
from models.image_generator import generate_image

def benchmark(prompt: str):
    start = time.time()
    path = generate_image(prompt, "stable-diffusion-v1-5")
    duration = time.time() - start
    print(f"Generated in {duration:.2f} seconds at {path}")

if __name__ == "__main__":
    benchmark("sunset over the mountains in anime style")
