from fastapi import APIRouter
from pydantic import BaseModel
from models.image_generator import generate_image
from agents.prompt_refiner import refine_prompt
from agents.model_selector import select_model
from agents.gpu_monitor import get_gpu_status

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.get("/")
def root():
    return {"message": "Welcome to NeuroRender.ai!"}

@router.post("/generate")
def generate(req: PromptRequest):
    refined = refine_prompt(req.prompt)
    model_name = select_model(refined)
    gpu = get_gpu_status()
    image_path = generate_image(refined, model_name)
    return {
        "original": req.prompt,
        "refined": refined,
        "model": model_name,
        "gpu": gpu,
        "image_url": f"http://localhost:8000/image/{os.path.basename(image_path)}"

    }

@router.get("/gpu-status")
def gpu_status():
    try:
        status = get_gpu_status()
        return {"status": "available", "gpu": status}
    except Exception as e:
        return {"status": "unavailable", "error": str(e)}
