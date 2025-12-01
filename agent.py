from strands import Agent
from strands.models.ollama import OllamaModel

from tools import calculator_tool


import os

MODEL_NAME = os.getenv('OLLAMA_MODEL')

# Create an Ollama model instance
ollama_model = OllamaModel(
    host="http://localhost:11434",  # Ollama server address
    model_id=MODEL_NAME               # Specify which model to use
)

# Create an agent with tools from the community-driven strands-tools package
# as well as our custom letter_counter tool
agent = Agent(model=ollama_model,
              tools=[calculator_tool])

# Ask the agent a question that uses the available tools
message = """
quanto é 5 + 4?
"""
agent(message)