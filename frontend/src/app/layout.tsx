import type { Metadata } from 'next'
import { Inter } from 'next/font/google'
import Link from 'next/link'
import './globals.css'

const inter = Inter({ subsets: ['latin'] })

export const metadata: Metadata = {
  title: 'Orga AI - Assistente Inteligente',
  description: 'Um assistente inteligente para ajudar com suas tarefas diárias',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="pt-BR">
      <body className={inter.className}>
        <header className="bg-blue-600 text-white p-4">
          <div className="container mx-auto flex justify-between items-center">
            <Link href="/" className="text-xl font-bold">Orga AI</Link>
            <nav>
              <ul className="flex space-x-4">
                <li><Link href="/" className="hover:underline">Home</Link></li>
                <li><Link href="/reminder" className="hover:underline">Lembretes</Link></li>
              </ul>
            </nav>
          </div>
        </header>
        <main className="container mx-auto py-6">
          {children}
        </main>
        <footer className="bg-gray-100 p-4 mt-8">
          <div className="container mx-auto text-center text-gray-600">
            <p>&copy; {new Date().getFullYear()} Orga AI. Todos os direitos reservados.</p>
          </div>
        </footer>
      </body>
    </html>
  )
} 