// components/LoginForm.tsx
'use client'

import { useState } from 'react'
import { supabase } from '@/services/supabase'

export default function LoginForm() {
  const [email, setEmail] = useState('')
  const [sent, setSent] = useState(false)

  const handleLogin = async () => {
    const { error } = await supabase.auth.signInWithOtp({ email })
    if (error) alert('Erro ao enviar link')
    else setSent(true)
  }

  return (
    <div className="p-4">
      <h2 className="text-xl font-bold mb-2">Login</h2>
      <input
        type="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        className="border p-2 w-full mb-2"
        placeholder="Digite seu e-mail"
      />
      <button onClick={handleLogin} className="bg-blue-600 text-white px-4 py-2 rounded">
        Enviar link mágico
      </button>

      {sent && <p className="mt-2 text-green-600">Verifique seu e-mail!</p>}
    </div>
  )
}
