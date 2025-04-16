'use client'

import { useState, useEffect } from 'react'
import { supabase } from '@/services/supabase'
import { useSession } from '@supabase/auth-helpers-react'

interface Message {
  id: string
  content: string
  role: 'user' | 'assistant'
  timestamp: string
}

const ChatPanel = () => {
  const [input, setInput] = useState('')
  const [loading, setLoading] = useState(false)
  const [messages, setMessages] = useState<Message[]>([])
  const session = useSession()

  useEffect(() => {
    fetchHistory()
  }, [session])

  const fetchHistory = async () => {
    if (!session?.user?.id) return

    const { data, error } = await supabase
      .from('messages')
      .select('*')
      .eq('user_id', session.user.id)
      .order('created_at', { ascending: true })

    if (error) {
      console.error('Erro ao carregar histórico:', error)
    } else {
      setMessages(data as Message[])
    }
  }

  const handleSend = async () => {
    if (!input.trim() || !session?.user?.id) return

    setLoading(true)

    // Add a mensagem do usuário
    const userMessage: Message = {
      id: Date.now().toString(),
      content: input,
      role: 'user',
      timestamp: new Date().toISOString()
    }

    setMessages(prev => [...prev, userMessage])

    try {
      const res = await fetch('http://localhost:8000/api/v1/generate', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ input, model: 'llama3' })
      })

      const data = await res.json()

      const aiMessage: Message = {
        id: (Date.now() + 1).toString(),
        content: data.response,
        role: 'assistant',
        timestamp: new Date().toISOString()
      }

      setMessages(prev => [...prev, aiMessage])
      setInput('')

      // Salva no Supabase
      const userId = session?.user?.id || 'dev-user-id'
      await supabase.from('messages').insert([
        {
          user_id: userId,
          input_text: userMessage.content,
          result_text: aiMessage.content,
          role: 'assistant'
        }
      ])
 
 //     await supabase.from('messages').insert([
 //       {
 //         user_id: session.user.id,
 //         input_text: userMessage.content,
 //         result_text: aiMessage.content,
 //         role: 'assistant'
 //       }     
 //     ])

    } catch (err) {
      console.error('Erro ao enviar mensagem:', err)
    } finally {
      setLoading(false)
    }
  }
  
  return (
    <div className="p-4 max-w-3xl mx-auto">
      <div className="bg-white shadow rounded p-4 h-[60vh] overflow-y-scroll space-y-4">
        {messages.map((msg) => (
          <div
            key={msg.id}
            className={`p-3 rounded-lg ${
              msg.role === 'user' ? 'bg-blue-100 text-right' : 'bg-gray-100 text-left'
            }`}
          >
            <p className="text-sm text-gray-600">{msg.content}</p>
          </div>
        ))}
      </div>

      <div className="mt-4 flex items-center gap-2">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault()
              handleSend()
            }
          }}
          placeholder="Escreva uma pergunta para a IA..."
          rows={2}
          className="flex-1 p-2 border rounded-lg"
        />
        <button
          onClick={handleSend}
          disabled={loading}
          className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
        >
          {loading ? 'Enviando...' : 'Enviar'}
          
        </button>
      </div>
    </div>
  )
}

export default ChatPanel
