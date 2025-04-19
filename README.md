# Orga.AI - Sua vida organizada com inteligência

![Orga.AI Logo](https://via.placeholder.com/150x50?text=Orga.AI)

Orga.AI é uma aplicação de organização pessoal e profissional com inteligência artificial integrada, projetada para automatizar e otimizar a gestão de tarefas, calendário e comunicação.

## 🚀 Visão Geral

Orga.AI utiliza IA para aprender com os hábitos do usuário e oferecer sugestões personalizadas, transformando ideias em planos de ação estruturados. A aplicação combina um painel Kanban, lista de tarefas inteligente, calendário integrado e um assistente IA para criar uma experiência única de produtividade.

## ✨ Funcionalidades Principais

- **Kanban com IA**: Criação automática de cards a partir de e-mails, mensagens ou voz
- **To-do List com Prioridade Inteligente**: Organização automática por urgência, energia e tempo
- **Calendário Integrado**: Sincronização com Google Calendar e sugestões de reorganização
- **Alertas Inteligentes**: Notificações via WhatsApp ou e-mail baseadas em hábitos e prazos
- **Assistente IA**: Criação de tarefas por comando de voz ou texto, sugestões de reorganização
- **Dashboard de Acompanhamento**: Indicadores de produtividade e visualização de tarefas

## 🛠️ Stack Tecnológica

- **Frontend**: Next.js (web) + React Native (mobile)
- **Backend**: FastAPI (Python)
- **Banco de Dados**: PostgreSQL via Supabase
- **Automação**: N8N para workflows e integrações
- **IA**: Ollama (llama3) para processamento local de linguagem natural
- **Integrações**: Google Calendar, WhatsApp, Gmail/Outlook

## 🏗️ Arquitetura

```
orga-ai-project/
├── frontend/                 # Aplicação Next.js
│   ├── app/                  # Componentes e páginas
│   ├── components/           # Componentes reutilizáveis
│   ├── services/             # Serviços e integrações
│   ├── public/               # Arquivos estáticos
│   └── ...
├── backend/                  # API FastAPI
│   ├── app/                  # Código principal
│   │   ├── api/              # Endpoints da API
│   │   ├── core/             # Configurações e utilitários
│   │   ├── models/           # Modelos de dados
│   │   └── services/         # Lógica de negócio
│   └── ...
├── n8n/                      # Configurações do N8N
│   └── workflows/            # Fluxos de automação
└── docker-compose.yml        # Configuração de containers
```

## 🚀 Como Executar

### Pré-requisitos

- Docker e Docker Compose
- Node.js 18+
- Python 3.11+
- Conta no Supabase
- Chaves de API para serviços integrados (Google Calendar, WhatsApp, etc.)

### Configuração do Ambiente

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/orga-ai-project.git
   cd orga-ai-project
   ```

2. Configure as variáveis de ambiente:
   ```bash
   cp .env.example .env
   # Edite o arquivo .env com suas configurações
   ```

3. Configure o Supabase:
   ```bash
   # Execute os scripts SQL na pasta supabase/schema
   ```

4. Configure o Ollama:
   ```bash
   # Siga as instruções em ollama/config.txt
   ```

5. Configure o N8N:
   ```bash
   # Importe o fluxo em automation/n8n/flow_task_reminder.json
   ```

6. Inicie os containers:
   ```bash
   docker-compose up -d
   ```

7. Acesse a aplicação:
   - Frontend: http://localhost:3000
   - Backend API: http://localhost:8000
   - Supabase Studio: http://localhost:54323
   - N8N: http://localhost:5678

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

## 📋 Roadmap

### Fase 1: Fundamentos (Atual)
- [x] Configuração do ambiente de desenvolvimento
- [x] Implementação da autenticação básica
- [x] Criação da estrutura de banco de dados
- [ ] Desenvolvimento da interface básica

### Fase 2: Funcionalidades Core
- [ ] Implementação do Kanban e To-do List
- [ ] Integração com calendário
- [ ] Configuração básica do Ollama para processamento de tarefas

### Fase 3: IA e Automação
- [ ] Implementação do assistente IA
- [ ] Configuração de alertas inteligentes
- [ ] Integração com WhatsApp e e-mail

### Fase 4: Refinamento e Lançamento
- [ ] Testes de usabilidade
- [ ] Otimização de performance
- [ ] Preparação para lançamento

## 🤝 Contribuição

Contribuições são bem-vindas! Por favor, leia o [CONTRIBUTING.md](CONTRIBUTING.md) para obter detalhes sobre nosso código de conduta e o processo para enviar pull requests.

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 📞 Contato

- **Website**: [orga.ai](https://orga.ai)
- **Email**: contato@orga.ai
- **Twitter**: [@orga_ai](https://twitter.com/orga_ai)
- **LinkedIn**: [Orga.AI](https://linkedin.com/company/orga-ai)

---

Desenvolvido com ❤️ pela equipe Orga.AI

