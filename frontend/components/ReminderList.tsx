// frontend/components/ReminderList.tsx
'use client'

import { useEffect, useState } from 'react'
import { getReminders } from '@/services/supabase'

export default function ReminderList() {
  const [reminders, setReminders] = useState<any[]>([])

  useEffect(() => {
    const fetch = async () => {
      const data = await getReminders()
      setReminders(data ?? [])
    }
    fetch()
  }, [])

  return (
    <div className="space-y-2">
      <h2 className="text-xl font-semibold">Histórico de Lembretes</h2>
      {reminders.length === 0 ? (
        <p className="text-gray-500">Nenhum lembrete encontrado.</p>
      ) : (
        reminders.map((r, i) => (
          <div key={i} className="bg-white p-4 rounded-lg shadow">
            <p className="text-sm text-gray-600">{new Date(r.created_at).toLocaleString()}</p>
            <p className="font-semibold">📝 {r.input_text}</p>
            <p className="text-gray-700">💡 {r.result_json?.response}</p>
          </div>
        ))
      )}
    </div>
  )
}
