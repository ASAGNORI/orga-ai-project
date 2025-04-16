// frontend/services/supabase.ts
'use client'

import { createClient } from '@supabase/supabase-js'

// Carrega variáveis de ambiente com segurança
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_ANON_KEY
const ollamaUrl = process.env.NEXT_PUBLIC_OLLAMA_API_URL || 'http://localhost:8000/api/v1/generate'

if (!supabaseUrl || !supabaseKey) {
  throw new Error('Supabase URL e Key são obrigatórios. Verifique o .env.local!')
}

export const supabase = createClient(supabaseUrl, supabaseKey)

// ADD reminder using Llama3 and save to Supabase
export const addReminderWithLLama = async (inputText: string, userId?: string) => {
  try {
    // 1. Envia para o backend que chama o Ollama
    const llamaResponse = await fetch(ollamaUrl, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ input: inputText, model: 'llama3' })
    })

    if (!llamaResponse.ok) {
      throw new Error('Erro ao chamar o Ollama')
    }

    const { response } = await llamaResponse.json()

    // 2. Salva no Supabase
    const { data, error } = await supabase.from('reminders').insert([
      {
        input_text: inputText,
        result_json: { response },
        user_id: userId ?? null
      }
    ])

    if (error) throw error

    return { message: response, input: inputText }
  } catch (error) {
    console.error('Erro ao adicionar lembrete:', error)
    return null
  }
}

// Buscar lembretes do Supabase
export const getReminders = async () => {
  const { data, error } = await supabase
    .from('reminders')
    .select('*')
    .order('created_at', { ascending: false })

  if (error) console.error('Erro ao buscar lembretes:', error)
  return data
}