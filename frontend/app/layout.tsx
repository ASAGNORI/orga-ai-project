
'use client'

import './globals.css'
import { ReactNode } from 'react'
import { SessionContextProvider } from '@supabase/auth-helpers-react'
import { createBrowserSupabaseClient } from '@supabase/auth-helpers-nextjs'
import { useState } from 'react'
import Sidebar from '@/components/Sidebar'

export default function ClientProviders({ children }: { children: React.ReactNode }) {
  const [supabaseClient] = useState(() => createBrowserSupabaseClient())

  return (
    <SessionContextProvider supabaseClient={supabaseClient}>
      <div className="flex">
        <Sidebar />
        <main className="ml-64 w-full p-4 bg-gray-50 min-h-screen">
          {children}
        </main>
      </div>
    </SessionContextProvider>
  )
}
