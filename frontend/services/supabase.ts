import { createClient } from '@supabase/supabase-js'

const supabaseUrl = process.env.NEXT_PUBLIC_SUPABASE_URL || ''
const supabaseKey = process.env.NEXT_PUBLIC_SUPABASE_KEY || ''

export const supabase = createClient(supabaseUrl, supabaseKey)

// Função para gerar resposta com o OLLAMA e salvar no Supabase
export const addReminderWithLLama = async (inputText: string) => {
  try {
    // 1. Envia o texto para a API do OLLAMA
    const response = await fetch(process.env.NEXT_PUBLIC_OLLAMA_API_URL || '', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ prompt: inputText }),
    });

    // 2. Verifica se a resposta do OLLAMA foi bem-sucedida
    if (!response.ok) {
      throw new Error('Erro ao gerar resposta com OLLAMA');
    }

    const result = await response.json();
    const resultJson = result;  // A resposta do OLLAMA

    // 3. Salva no Supabase
    const { data, error } = await supabase
      .from('reminders')
      .insert([
        {
          input_text: inputText,
          result_json: resultJson,  // Salva o JSON gerado pelo OLLAMA
          created_at: new Date(),
        },
      ]);

    if (error) {
      console.error('Erro ao adicionar lembrete:', error);
      return null;
    } else {
      return data;
    }
  } catch (error) {
    console.error('Erro ao processar lembrete com OLLAMA:', error);
  }
};
export const getReminders = async () => {
  const { data, error } = await supabase
    .from('reminders')
    .select('*')
    .order('created_at', { ascending: false })

  if (error) {
    console.error('Erro ao buscar lembretes:', error)
  } else {
    return data
  }
}