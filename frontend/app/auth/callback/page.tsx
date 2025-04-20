'use client'

import React, { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { createClientComponentClient } from '@supabase/auth-helpers-nextjs'

export default function AuthCallbackPage() {
  const router = useRouter()
  const supabase = createClientComponentClient()

  useEffect(() => {
    const handleAuthCallback = async () => {
      const { data: { session }, error } = await supabase.auth.getSession()
      
      if (error) {
        console.error('Error during auth callback:', error)
        router.push('/auth?error=Authentication failed')
        return
      }

      if (session) {
        router.push('/dashboard')
      } else {
        router.push('/auth')
      }
    }

    handleAuthCallback()
  }, [router, supabase])

  return (
    <div className="flex min-h-screen items-center justify-center bg-gray-50">
      <div className="text-center">
        <h1 className="text-2xl font-bold mb-4">Processing authentication...</h1>
        <p className="text-gray-600">Please wait while we redirect you.</p>
      </div>
    </div>
  )
} 