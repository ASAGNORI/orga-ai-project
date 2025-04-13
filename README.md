# Orga AI Project

Um projeto de organização pessoal com IA integrada, usando Next.js, FastAPI, Supabase, N8N e Ollama.

## 🚀 Tecnologias

- Frontend: Next.js
- Backend: FastAPI
- Banco de Dados: Supabase
- Automação: N8N
- IA: Ollama (llama3)

## 📋 Pré-requisitos

- Node.js v18.17.0 ou superior
- Python 3.11 ou superior
- Docker
- Ollama

## 🔧 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/orga-ai-project.git
cd orga-ai-project
```

2. Instale as dependências do frontend:
```bash
cd frontend
npm install
```

3. Instale as dependências do backend:
```bash
cd ../backend
python -m venv venv
source venv/bin/activate  # No Windows: .\venv\Scripts\activate
pip install -r ../requirements.txt
```

4. Inicie o Supabase:
```bash
cd ../supabase
supabase start
```

## 🚀 Executando o projeto

1. Inicie o backend:
```bash
cd backend
source venv/bin/activate
uvicorn main:app --reload
```

2. Inicie o frontend:
```bash
cd frontend
npm run dev
```

3. Inicie o N8N:
```bash
n8n
```

4. Inicie o Ollama:
```bash
ollama run llama3
```

## 🌐 Endpoints

- Frontend: http://localhost:3000
- Backend: http://localhost:8000
- Supabase Studio: http://localhost:54323
- N8N: http://localhost:5678
- Ollama: http://localhost:11434/api/generate

## 📝 Estrutura do Projeto

```
orga-ai-project/
├── frontend/          # Next.js frontend
├── backend/           # FastAPI backend
├── supabase/          # Configurações do Supabase
├── automation/        # Workflows do N8N
└── docs/             # Documentação
```

## 🤝 Contribuindo

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes. 