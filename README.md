# Agente Conversacional com Tool Matemática para vaga de estágio na DreamSquad

Este projeto implementa um agente conversacional equipado com uma tool personalizada para executar operações matemáticas utilizando **numexpr**. A opção por desenvolver essa implementação manual, em vez de usar a tool pronta do framework Strands, tem como objetivo demonstrar de forma explícita como o agente interpreta a consulta em linguagem natural, reestrutura a expressão fornecida pelo usuário e a converte em uma operação matemática válida e avaliável.

## Modelo Utilizado
O agente utiliza o modelo **Llama 3.1** via **Ollama**.

## Arquitetura 

A aplicação é divida em _src_ e _service_. O objetivo desta divisão é garantir separabilidade entre o código que garante o serviço do modelo como API e o código que efetivamente implementa o agente em si. Como consequência disso, é natural também desenvolver o agente utilizando modelos de resposta estruturados, que são facilitadores naturais de sistemas agênticos por se relacionarem muito positivamente com modelos de linguagem. Além disso, a divisão dentro da pasta _src_ ocorre em agente, tools e prompts que são os blocos básicos de construção do agente.


## Variáveis de Ambiente
OLLAMA_MODEL = nome do modelo

OLLAMA_PORT  = porta do servidor Ollama

## Execução Local
1. Instalar dependências: pip install -r requirements.txt

2. Garantir que o modelo Ollama está instalado: ollama pull [nome do modelo]

3. Iniciar o servidor do Ollama: ollama serve

4. Executar a aplicação: uvicorn app:app

## Teste da API
Enviar requisição POST para:
http://localhost:8080/chat

### Exemplo de corpo JSON:
{
"id": 123,
"query": "qual a raiz quadrada de 144?"
}

### Resposta esperada:
{
"user_query": "qual a raiz quadrada de 144?",
"response": "A raiz quadrada de 144 é 12."
}
