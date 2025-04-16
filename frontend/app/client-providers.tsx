'use client'

import { SessionContextProvider, useSessionContext } from '@supabase/auth-helpers-react'
import { createPagesBrowserClient } from '@supabase/auth-helpers-nextjs'
import { useState, useEffect } from 'react'
import Sidebar from '@/components/Sidebar'

export default function ClientProviders({ children }: { children: React.ReactNode }) {
  const [supabaseClient] = useState(() => createPagesBrowserClient())

  return (
    <SessionContextProvider supabaseClient={supabaseClient}>
      <SessionLogger />
      <div className="flex">
        <Sidebar />
        <main className="ml-64 w-full p-4 bg-gray-50 min-h-screen">
          {children}
        </main>
      </div>
    </SessionContextProvider>
  )
}

// Log para debug do estado de sessão
function SessionLogger() {
  const { session, isLoading } = useSessionContext()

  useEffect(() => {
    console.log('📡 Sessão:', session)
  }, [session])

  return null
}
