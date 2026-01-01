from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List
import random
from mangum import Mangum

app = FastAPI()

# Define the expected request format
class PromptRequest(BaseModel):
    quantity: int
    category: str
    style: str
    tone: str
    format: str

# Fake premium prompt generator (replace with your real logic later)
def generate_prompts(quantity, category, style, tone):
    return [
        f"[{category.upper()}] ({style}, {tone}) Prompt #{i+1}: Create a scenario where XYZ happens..."
        for i in range(quantity)
    ]

@app.post("/generate-prompt-pack")
async def generate_prompt_pack(req: PromptRequest):
    prompts = generate_prompts(req.quantity, req.category, req.style, req.tone)
    return {
        "format": req.format,
        "prompts": prompts
    }

handler = Mangum(app)
