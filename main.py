from fastapi import FastAPI
from agents.prompt_refiner import refine_prompt
from agents.gpu_monitor import get_gpu_status
from agents.model_selector import select_model
from models.image_generator import generate_image
from fastapi.staticfiles import StaticFiles

app = FastAPI()
app.mount("/data", StaticFiles(directory="data"), name="data")

@app.get("/")
def root():
    return {"message": "Welcome to NeuroRender.ai!"}

@app.post("/generate")
def generate(payload: dict):
    prompt = payload.get("prompt", "")
    refined = refine_prompt(prompt)
    gpu = get_gpu_status()
    model = select_model(gpu)
    image = generate_image(refined, model)
    return {
        "original": prompt,
        "refined": refined,
        "model": model,
        "gpu": gpu,
        "image_url": image
    }
