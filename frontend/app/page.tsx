import Link from "next/link";

export default function HomePage() {
  return (
    <div className="text-center mt-20">
      <h1 className="text-3xl font-bold mb-4">Bem-vindo ao ORGA.AI</h1>
      <p className="text-gray-600 mb-6">Organize sua vida com agentes inteligentes</p>
      <Link href="/chat">
        <button className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700">
          Ir para o Chat
        </button>
      </Link>
    </div>
  )
}