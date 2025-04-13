# Orga.AI - Organização com IA

Este repositório contém a base para o desenvolvimento do Orga.AI, uma plataforma para organização pessoal com IA, Kanban, mapa mental, tarefas e foco.

## Tecnologias
- Supabase (DB + Auth com Google OAuth)
- Ollama + Langchain (IA local)
- N8N para automações (lembretes, reagendamentos)
- Next.js / React Native para UI
- Google Calendar + WhatsApp Integration

## Como usar
1. Suba a estrutura do Supabase com os scripts SQL na pasta `supabase/schema`.
2. Configure o modelo Ollama local conforme `ollama/config.txt`.
3. Importe o fluxo do N8N disponível em `automation/n8n/flow_task_reminder.json`.