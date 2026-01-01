from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class PromptRequest(BaseModel):
    quantity: int
    category: str
    style: str
    tone: str
    format: str

def generate_premium_prompts(quantity, category, style, tone):
    return [
        f"[{category.upper()}] ({style}, {tone}) Prompt #{{i+1}}: Write something unique about a future world where {{i+1}} is the key element."
        for i in range(quantity)
    ]

@app.post("/generate-prompt-pack")
async def generate_prompt_pack(request: PromptRequest):
    prompts = generate_premium_prompts(
        request.quantity, request.category, request.style, request.tone
    )
    return {
        "format": request.format,
        "prompts": prompts
    }

@app.get("/")
def read_root():
    return {{"message": "Prompt Generator API is live"}}
