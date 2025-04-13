'use client'

import { useEffect, useRef } from 'react'
import MindElixir from 'mind-elixir'

export default function MindmapCanvas() {
  const containerRef = useRef<HTMLDivElement>(null)

  useEffect(() => {
    if (containerRef.current) {
      const mind = new MindElixir({
        el: containerRef.current,
        direction: 2,
        data: {
          nodeData: {
            id: 'root',
            topic: 'Orga.AI',
            children: [],
          },
        },
      })
      mind.init()
    }
  }, [])

  return <div ref={containerRef} className="w-full h-[600px] bg-gray-100 rounded" />
} 