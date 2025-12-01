from fastapi import APIRouter
from service.model import UserInput, ModelResponse
from src.agent import agent

# Cria o router
router = APIRouter()

@router.get('/health')
def health_check():
    return {"status": "ok"}

@router.post('/chat')
def chat(user_input: UserInput):
    user_query = user_input.query
    
    result = agent(prompt=user_query, 
                   structured_output_model=ModelResponse)
    
    json_result = {
                    "user_query": user_query,    
                    "response": result.structured_output.response
                   }
    
    return json_result
    
    
    