# Orga.AI - Sua vida organizada com inteligência

## 📋 Visão Geral

Orga.AI é uma aplicação moderna de produtividade que combina gerenciamento de tarefas com inteligência artificial para otimizar seu fluxo de trabalho. A plataforma utiliza tecnologias de ponta como Next.js, FastAPI, Supabase e modelos de IA para oferecer uma experiência única de organização e automação.

## 🚀 Etapas de Desenvolvimento

### Etapa 1: Definição e Planejamento
- **Problema de nicho**: App para organização de tarefas e insights
- **Wireframe e roteiro**: Design da interface e planejamento de funcionalidades
- **MVP**: Desenvolvimento do produto mínimo viável
- **Lançamento**: Monitoramento e melhorias contínuas

### Etapa 2: Tecnologias e Decisões Técnicas
- **Frontend**: Next.js
- **Backend**: FastAPI
- **Banco de Dados**: Supabase
- **Automação**: N8N
- **IA**: Ollama (llama3)

## ✨ Funcionalidades Principais

### Funcionalidades-Chave (MVP)
- **Painel Kanban com IA**: Criação automática de cards a partir de e-mails, mensagens ou voz
- **To-do List com Prioridade Inteligente**: Organização automática por urgência, energia e tempo
- **Calendário Integrado**: Sincronização com Google Calendar e sugestões de reorganização
- **Alertas Inteligentes**: Notificações via WhatsApp ou e-mail baseadas em hábitos e prazos
- **Assistente IA**: 
  - Criação de tarefas por comando de voz ou texto
  - Sugestões de reorganização de agenda
  - Redação/resposta de e-mails e mensagens no WhatsApp com base em contexto
  - Geração de resumos semanais e planos de ação

### Dashboard de Acompanhamento com IA
- **Indicadores principais**:
  - Tarefas cumpridas e não cumpridas
  - Tarefas atrasadas
  - Metas alcançadas e pendentes
  - Tarefas em andamento (por status ou tag)
  - Horas de foco real (calculado via padrão de uso ou timer com IA)
- **Visão Gráfica**:
  - Gráfico da semana (atividades por dia, calor de produtividade)
  - Gráfico de foco (pomodoro, tempo de dedicação, interrupções)

### Funções Avançadas de Replanejamento com IA
- IA detecta sobrecarga, atraso, ou padrões negativos
  - Sugere redistribuição de tarefas
  - Proporcionalmente ajusta prazos com base na rotina
  - Prioriza metas críticas e envia alertas para realinhamento

## 🛠 Stack Tecnológica

### Frontend
- Next.js 14
- React 18
- TailwindCSS
- Framer Motion
- Supabase Client

### Backend
- FastAPI
- Python 3.11
- SQLAlchemy
- LlamaIndex
- Transformers
- Torch

### Infraestrutura
- Docker & Docker Compose
- Supabase (PostgreSQL)
- Kong API Gateway
- N8N (Automação)

### IA/Agente
- Ollama (llama3)
- Langchain
- RAG com dados do usuário
- Modelos de linguagem avançados

## 🚀 Como Executar

### Pré-requisitos
- Docker e Docker Compose
- Git
- Node.js 18+ (para desenvolvimento)
- Python 3.11+ (para desenvolvimento)

### Configuração do Ambiente

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/orga-ai.git
cd orga-ai
```

2. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

3. Inicie os containers:
```bash
docker compose up -d
```

4. Acesse as aplicações:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- Supabase Studio: http://localhost:54323
- N8N: http://localhost:5678

### Desenvolvimento

#### Frontend
```bash
cd frontend
npm install
npm run dev
```

#### Backend
```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # ou .venv\Scripts\activate no Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

## 📦 Estrutura do Projeto

```
orga-ai/
├── frontend/                # Aplicação Next.js
│   ├── app/                # Componentes e páginas
│   ├── components/         # Componentes reutilizáveis
│   ├── lib/                # Bibliotecas e utilitários
│   ├── services/           # Serviços e integrações
│   ├── public/             # Arquivos estáticos
│   ├── __tests__/          # Testes unitários
│   ├── e2e/                # Testes end-to-end
│   └── package.json        # Dependências Node.js
├── backend/                # API FastAPI
│   ├── app/               # Código fonte Python
│   │   ├── api/          # Rotas da API
│   │   ├── core/         # Configurações e utilitários
│   │   ├── config/       # Configurações de ambiente
│   │   ├── models/       # Modelos de dados
│   │   └── utils/        # Funções utilitárias
│   ├── tests/            # Testes
│   ├── ollama/           # Configurações do Ollama
│   └── requirements.txt   # Dependências Python
├── supabase/              # Configurações do Supabase
├── n8n/                   # Configurações do N8N
├── ollama/                # Configurações do Ollama
├── automation/            # Scripts de automação
├── scripts/               # Scripts utilitários
├── docs/                  # Documentação
└── docker-compose.yml     # Orquestração de containers
```

## 💰 Modelo de Negócio

### Planos de Assinatura

1. **Free Forever**
   - Tarefas ilimitadas
   - IA local (via Ollama)
   - Até 3 gatilhos ativos
   - Integração com Google Calendar
   - Painel básico de produtividade
   - Preço: R$ 0

2. **Pro (SaaS)**
   - IA turbinada (com RAG, contexto pessoal e histórico)
   - Replanejamento automático
   - Alertas dinâmicos
   - Painel completo
   - Relatórios e insights personalizados
   - Preço: R$ 29/mês

3. **Business/Team**
   - Colaboração entre times
   - Assistente de IA para gestão de equipe
   - Metas por grupo
   - Relatórios integrados
   - Alertas compartilháveis
   - Preço: R$ 69/mês/usuário

## 🗺 Roadmap

### Fase 1 - MVP (Concluído)
- [x] Autenticação básica
- [x] CRUD de tarefas
- [x] Interface responsiva
- [x] Integração com IA

### Fase 2 - Melhorias (Em Andamento)
- [ ] Sistema de tags
- [ ] Filtros avançados
- [ ] Exportação de dados
- [ ] Melhorias na IA

### Fase 3 - Enterprise
- [ ] SSO/SAML
- [ ] API GraphQL
- [ ] White-label
- [ ] Customização avançada

## 🤝 Contribuindo

1. Fork o projeto
2. Crie sua Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📧 Contato

- Website: [orga.ai](https://orga.ai)
- Email: contato@orga.ai
- Twitter: [@orga_ai](https://twitter.com/orga_ai)
- LinkedIn: [Orga.AI](https://linkedin.com/company/orga-ai)

---

Desenvolvido com ❤️ pela equipe Orga.AI

