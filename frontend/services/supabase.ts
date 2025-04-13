import { createClient } from '@supabase/supabase-js'

// Puxa as variáveis do .env.local (precisa estar com prefixo NEXT_PUBLIC_)
const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL as string
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_KEY as string

// Cria o cliente do Supabase
const supabase = createClient(supabaseUrl, supabaseKey)
export default supabase

// Função para adicionar lembrete
export const addReminder = async (message: string) => {
  const { data, error } = await supabase
    .from('reminders')
    .insert([{ message, created_at: new Date() }])

  if (error) {
    console.error('Erro ao adicionar lembrete:', error)
    return null
  }
  return data
}

// Função para buscar lembretes
export const getReminders = async () => {
  const { data, error } = await supabase
    .from('reminders')
    .select('*')
    .order('created_at', { ascending: false })

  if (error) {
    console.error('Erro ao buscar lembretes:', error)
    return []
  }
  return data
}
