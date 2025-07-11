

"""
Run standalone generation from command line.
"""

from models.image_generator import generate_image

if __name__ == "__main__":
    prompt = input("Enter a prompt for image generation: ")
    path = generate_image(prompt, "stable-diffusion-v1-5")
    print("Image saved at:", path)
