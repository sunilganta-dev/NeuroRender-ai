
import os
import torch
from PIL import Image
from datetime import datetime
from diffusers import StableDiffusionPipeline

# Load model once at the top (optional: cache globally for reuse)
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float32)

# Use GPU if available
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe = pipe.to(device)

def generate_image(prompt: str, model_name: str = "stable-diffusion-v1-5") -> str:
    """
    Generates an image based on the prompt and returns the saved image path.
    """
    try:
        # Generate the image
        image = pipe(prompt).images[0]

        # Save the image to the 'data/' folder with timestamp
        os.makedirs("data", exist_ok=True)
        filename = f"data/image_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
        image.save(filename)

        return filename
    except Exception as e:
        print("Image generation error:", e)
        return ""
