### Run ollama
#### docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama


### Run openwebui

#### docker pull ghcr.io/open-webui/open-webui:main

#### docker run -d -p 3000:8080 -v open-webui:/app/backend/data --name open-webui ghcr.io/open-webui/open-webui:main


#### ollama localhost -> admin settings-> models -> pull models like gemma:2b
### fastAPI
#### pip install "fastapi[standard]"

#### pip install ollama

#### fastapi dev server.py

#### brew install huggingface-cli 
#### pip install -U "huggingface_hub"
#### huggingface-cli login # token from huggingface access token section 

#### pip install transformers
#### pip install torch