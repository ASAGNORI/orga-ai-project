import { useState } from 'react'
import { useAuth } from '@/contexts/AuthContext'
import Link from 'next/link'

export default function UserMenu() {
  const { user, signOut } = useAuth()
  const [isOpen, setIsOpen] = useState(false)

  if (!user) {
    return (
      <div className="flex space-x-2">
        <Link
          href="/auth/login"
          className="px-4 py-2 text-sm font-medium text-white bg-blue-700 rounded-md hover:bg-blue-800"
        >
          Login
        </Link>
        <Link
          href="/auth/signup"
          className="px-4 py-2 text-sm font-medium text-blue-700 bg-white rounded-md hover:bg-gray-50"
        >
          Cadastro
        </Link>
      </div>
    )
  }

  return (
    <div className="relative">
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center space-x-2 text-sm focus:outline-none"
      >
        <div className="w-8 h-8 rounded-full bg-blue-700 flex items-center justify-center">
          {user.email?.[0].toUpperCase()}
        </div>
        <span>{user.email}</span>
      </button>

      {isOpen && (
        <div className="absolute right-0 mt-2 w-48 py-2 bg-white rounded-md shadow-xl z-20">
          <button
            onClick={() => signOut()}
            className="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 w-full text-left"
          >
            Sair
          </button>
        </div>
      )}
    </div>
  )
} 