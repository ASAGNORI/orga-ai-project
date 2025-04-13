import Link from 'next/link'

export default function Home() {
  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-4">
      <h1 className="text-3xl font-bold mb-6">Orga AI - Assistente Inteligente</h1>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-4 max-w-4xl w-full">
        <Link href="/reminder" className="p-6 bg-white rounded-lg shadow hover:shadow-md transition-shadow">
          <h2 className="text-xl font-semibold mb-2">🧠 Agente de Lembretes</h2>
          <p className="text-gray-600">Crie lembretes inteligentes que se adaptam ao seu contexto</p>
        </Link>
        {/* Adicione mais cards de funcionalidades aqui */}
      </div>
    </div>
  )
} 