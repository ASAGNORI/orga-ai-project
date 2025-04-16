'use client'

import ReminderList from '@/components/ReminderList'
import AddReminderForm from '@/components/AddReminderForm'

export default function RemindersPage() {
  return (
    <div className="max-w-3xl mx-auto space-y-8">
      <h1 className="text-2xl font-bold">Gerenciar Lembretes</h1>
      <AddReminderForm />
      <ReminderList />
    </div>
  )
}
