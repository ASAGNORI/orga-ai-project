'use client'

import { useState } from 'react'
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
import { Card, CardContent } from '@/components/ui/card'

export default function ReminderAgent() {
  const [message, setMessage] = useState('')
  const [response, setResponse] = useState('')
  const [loading, setLoading] = useState(false)

  const handleSend = async () => {
    if (!message) return

    setLoading(true)
    setResponse('')

    try {
      const res = await fetch('http://localhost:8001/api/v1/reminder', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: message }),
      })

      const data = await res.json()
      
      if (data.error) {
        console.error('Erro:', data.error)
        setResponse(`Erro: ${data.error}`)
      } else {
        setResponse(data.response)
      }
    } catch (err) {
      console.error('Erro ao processar lembrete:', err)
      setResponse('Erro ao processar lembrete. Tente novamente.')
    }

    setLoading(false)
  }

  return (
    <Card className="w-full max-w-xl mx-auto mt-6">
      <CardContent className="space-y-4 p-6">
        <h2 className="text-xl font-semibold">🧠 Agente de Lembretes Inteligente</h2>
        <Input
          placeholder="Ex: me avisa de tomar remédio amanhã"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
        />
        <Button onClick={handleSend} disabled={loading}>
          {loading ? 'Processando...' : 'Enviar'}
        </Button>
        {response && (
          <div className="mt-4 bg-gray-100 p-4 rounded">
            <pre className="text-sm whitespace-pre-wrap">{response}</pre>
          </div>
        )}
      </CardContent>
    </Card>
  )
} 