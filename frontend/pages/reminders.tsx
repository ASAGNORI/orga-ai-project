// pages/reminders.tsx
'use client'

import { useEffect, useState } from 'react'
import { addReminderWithLLama, getReminders } from '@/services/supabase'

export default function RemindersPage() {
  const [message, setMessage] = useState('')
  const [reminders, setReminders] = useState<any[]>([])

  const fetchData = async () => {
    const data = await getReminders()
    setReminders(data || [])
  }

  useEffect(() => {
    fetchData()
  }, [])

  const handleSubmit = async () => {
    await addReminderWithLLama(message)
    setMessage('')
    fetchData()
  }

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold">Lembretes</h1>
      <input
        value={message}
        onChange={(e) => setMessage(e.target.value)}
        placeholder="Novo lembrete"
        className="border p-2"
      />
      <button onClick={handleSubmit} className="ml-2 p-2 bg-blue-500 text-white rounded">
        Adicionar
      </button>

      <ul className="mt-4">
        {reminders.map((r) => (
          <li key={r.id}>{r.message} - {new Date(r.created_at).toLocaleString()}</li>
        ))}
      </ul>
    </div>
  )
}
