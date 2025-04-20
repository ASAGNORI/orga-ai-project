'use client'

import './globals.css'
import React, { ReactNode, useEffect } from 'react'
import { SessionContextProvider, useSessionContext } from '@supabase/auth-helpers-react'
import { createBrowserSupabaseClient } from '@supabase/auth-helpers-nextjs'
import { useState } from 'react'
import { usePathname, useRouter } from 'next/navigation'
import Sidebar from '../components/Sidebar'
import { AuthProvider } from '../lib/context/AuthContext'

// Component to handle authentication and redirection
function AuthGuard({ children }: { children: React.ReactNode }) {
  const { session, isLoading } = useSessionContext()
  const router = useRouter()
  const pathname = usePathname()
  
  // List of public routes that don't require authentication
  const publicRoutes = ['/auth', '/auth/callback']
  
  useEffect(() => {
    if (!isLoading) {
      // If user is not authenticated and trying to access a protected route
      if (!session && !publicRoutes.includes(pathname)) {
        router.push('/auth')
      }
      
      // If user is authenticated and trying to access auth pages
      if (session && publicRoutes.includes(pathname)) {
        router.push('/dashboard')
      }
    }
  }, [session, isLoading, pathname, router])
  
  // Show loading state while checking authentication
  if (isLoading) {
    return (
      <div className="flex min-h-screen items-center justify-center bg-gray-50">
        <div className="text-center">
          <h1 className="text-2xl font-bold mb-4">Loading...</h1>
        </div>
      </div>
    )
  }
  
  // If on a public route, just render the children
  if (publicRoutes.includes(pathname)) {
    return <>{children}</>
  }
  
  // For protected routes, check if user is authenticated
  if (!session) {
    return null // Will be redirected by the useEffect
  }
  
  // User is authenticated, show the layout with sidebar
  return (
    <div className="flex">
      <Sidebar />
      <main className="ml-64 w-full p-4 bg-gray-50 min-h-screen">
        {children}
      </main>
    </div>
  )
}

export default function RootLayout({ children }: { children: React.ReactNode }) {
  const [supabaseClient] = useState(() => createBrowserSupabaseClient())

  return (
    <html lang="en">
      <body>
        <SessionContextProvider supabaseClient={supabaseClient}>
          <AuthProvider>
            <AuthGuard>{children}</AuthGuard>
          </AuthProvider>
        </SessionContextProvider>
      </body>
    </html>
  )
}
