'use client'

import { useEffect, useRef } from 'react'
import MindElixir from 'mind-elixir'
import { useAuth } from '@/contexts/AuthContext'
import { createClient } from '@/utils/supabase/client'

type MindMapData = {
  nodeData: {
    id: string
    topic: string
    root?: boolean
    children: any[]
  }
}

export default function MindMap() {
  const containerRef = useRef<HTMLDivElement>(null)
  const mindMapRef = useRef<any>(null)
  const { user } = useAuth()
  const supabase = createClient()

  useEffect(() => {
    if (!containerRef.current || !user) return

    const defaultData: MindMapData = {
      nodeData: {
        id: 'root',
        topic: 'Meu Mapa Mental',
        root: true,
        children: [],
      },
    }

    const options = {
      el: '#mindmap',
      direction: 2,
      draggable: true,
      contextMenu: true,
      toolBar: true,
      nodeMenu: true,
      keypress: true,
      locale: 'pt-br',
      theme: {
        primary: '#2563eb',
        secondary: '#e5e7eb',
        success: '#10b981',
      },
      data: defaultData,
    }

    mindMapRef.current = new MindElixir(options)
    
    // Load saved data or initialize with default
    loadMindMap()

    // Save on data change
    mindMapRef.current.bus.addListener('operation', () => {
      saveMindMap()
    })

    return () => {
      if (mindMapRef.current) {
        mindMapRef.current.destroy()
      }
    }
  }, [user])

  const loadMindMap = async () => {
    try {
      const { data, error } = await supabase
        .from('mind_maps')
        .select('data')
        .eq('user_id', user?.id)
        .single()

      if (error) throw error

      if (data) {
        mindMapRef.current.init(data.data)
      } else {
        // Initialize with default data
        mindMapRef.current.init({
          nodeData: {
            id: 'root',
            topic: 'Meu Mapa Mental',
            root: true,
            children: [],
          },
        })
        await saveMindMap()
      }
    } catch (error) {
      console.error('Error loading mind map:', error)
    }
  }

  const saveMindMap = async () => {
    if (!mindMapRef.current || !user) return

    try {
      const data = mindMapRef.current.getData()
      const { error } = await supabase
        .from('mind_maps')
        .upsert({
          user_id: user.id,
          data,
          updated_at: new Date().toISOString(),
        })

      if (error) throw error
    } catch (error) {
      console.error('Error saving mind map:', error)
    }
  }

  return (
    <div className="bg-white rounded-lg shadow-lg p-4 h-[600px]">
      <div id="mindmap" ref={containerRef} className="w-full h-full" />
    </div>
  )
}