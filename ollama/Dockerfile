# Imagem base com Python 3.11 (ou a versão que você estiver utilizando)
FROM python:3.11-slim

# Definir o diretório de trabalho dentro do contêiner
WORKDIR /app

# Copiar o arquivo requirements.txt (assumindo que você tenha um com as dependências do Ollama)
COPY requirements.txt .

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação para o contêiner
COPY . .

# Expor a porta em que o Ollama vai rodar
EXPOSE 5000

# Comando para rodar o Ollama
CMD ["python", "ollama_server.py"]  # Substitua pelo comando correto para rodar o Ollama

