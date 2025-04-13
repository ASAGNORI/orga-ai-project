import { NextResponse } from 'next/server'
import { createClient } from '@supabase/supabase-js'

const supabase = createClient(
  process.env.NEXT_PUBLIC_SUPABASE_URL || 'http://127.0.0.1:54321',
  process.env.SUPABASE_SERVICE_ROLE_KEY || 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZS1kZW1vIiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImV4cCI6MTk4MzgxMjk5Nn0.EGIM96RAZx35lJzdJsyH-qQwv8Hdp7fsn3W0YpN81IU'
)

export async function POST(req: Request) {
  try {
    const { text } = await req.json()

    // Simulando resposta da IA (você pode plugar aqui LLM, N8N, etc)
    const response = `Ok, vou te lembrar: "${text}"`

    // Salvar no Supabase
    const { error } = await supabase.from('reminders').insert({
      input_text: text,
      result_json: response,
      created_at: new Date().toISOString(),
    })

    if (error) {
      console.error('Erro ao salvar no Supabase:', error)
      return NextResponse.json({ error: error.message }, { status: 500 })
    }

    return NextResponse.json({ response })
  } catch (error) {
    console.error('Erro ao processar requisição:', error)
    return NextResponse.json({ error: 'Erro ao processar requisição' }, { status: 500 })
  }
} 