// frontend/components/Sidebar.tsx
import Link from 'next/link'

export default function Sidebar() {
  return (
    <aside className="w-64 bg-white h-screen shadow-lg p-6 fixed top-0 left-0">
      <h1 className="text-2xl font-bold mb-8">ORGA.AI</h1>
      <nav className="flex flex-col gap-4">
        <Link href="/dashboard" className="hover:text-blue-700">📊 Dashboard</Link>
        <Link href="/chat" className="hover:text-blue-700">💬 Chat</Link>
        <Link href="/reminders" className="hover:text-blue-700">⏰ Lembretes</Link>
        <Link href="/tasks" className="hover:text-blue-700">✅ Tarefas</Link>
      </nav>
    </aside>
  )
}
