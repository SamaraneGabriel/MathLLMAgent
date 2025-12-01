from strands import Agent
from strands.models.ollama import OllamaModel
from src.tools import calculator_tool

import os
from dotenv import load_dotenv

load_dotenv()

MODEL_NAME = os.getenv('OLLAMA_MODEL')
OLLAMA_PORT = os.getenv('OLLAMA_PORT')

import yaml
from pathlib import Path

base_path = Path(__file__).parent

yaml_path = base_path / "prompts.yaml"

with open(yaml_path, "r") as file:
    prompts = yaml.safe_load(file)


ollama_model = OllamaModel(
    host=f"http://localhost:{OLLAMA_PORT}",  
    model_id=MODEL_NAME               
)

agent = Agent(model=ollama_model,
              tools=[calculator_tool],
              system_prompt=prompts['system_prompt'],
              )
