from pydantic import BaseModel, Field
from typing import Optional

class UserInput(BaseModel):
    id: Optional[int] = None       
    query: str 
    

class ModelResponse(BaseModel):
    """Modelo padrão de resposta do agente."""
    response: str = Field(description="Respota do modelo")
