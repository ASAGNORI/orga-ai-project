// frontend/components/Sidebar.tsx
'use client'

import React from 'react'
import Link from 'next/link'
import { useAuthContext } from '../lib/context/AuthContext'

export default function Sidebar() {
  const { signOut, loading } = useAuthContext()

  const handleLogout = async () => {
    try {
      await signOut()
    } catch (error) {
      console.error('Error logging out:', error)
    }
  }

  return (
    <aside className="w-64 bg-white h-screen shadow-lg p-6 fixed top-0 left-0">
      <h1 className="text-2xl font-bold mb-8">ORGA.AI</h1>
      <nav className="flex flex-col gap-4">
        <Link href="/dashboard" className="hover:text-blue-700">📊 Dashboard</Link>
        <Link href="/chat" className="hover:text-blue-700">💬 Chat</Link>
        <Link href="/reminders" className="hover:text-blue-700">⏰ Lembretes</Link>
        <Link href="/tasks" className="hover:text-blue-700">✅ Tarefas</Link>
      </nav>
      
      <div className="mt-auto pt-8">
        <button
          onClick={handleLogout}
          disabled={loading}
          className="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-red-600 hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 disabled:opacity-50"
        >
          {loading ? 'Logging out...' : 'Logout'}
        </button>
      </div>
    </aside>
  )
}
