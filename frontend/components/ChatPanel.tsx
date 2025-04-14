'use client'
import React, { useState, useEffect } from 'react'
import { motion } from 'framer-motion'

interface Message {
  id: string
  content: string
  role: 'user' | 'assistant'
  timestamp: string
}

const ChatPanel: React.FC = () => {
  const [input, setInput] = useState('')
  const [response, setResponse] = useState('')
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [history, setHistory] = useState<Message[]>([])

  useEffect(() => {
    fetchHistory()
  }, [])

  const fetchHistory = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/v1/history')
      if (!response.ok) throw new Error('Failed to fetch history')
      const data = await response.json()
      setHistory(data)
    } catch (err) {
      setError('Failed to load chat history')
      console.error(err)
    }
  }

  const handleSend = async () => {
    if (!input.trim()) return

    setLoading(true)
    setError(null)

    try {
      const response = await fetch('http://localhost:8000/api/v1/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input: input, model: 'llama3' }),
      })

      if (!response.ok) throw new Error('Failed to send message')

      const data = await response.json()
      setResponse(data.response)
      setHistory(prev => [...prev, {
        id: Date.now().toString(),
        content: input,
        role: 'user',
        timestamp: new Date().toISOString()
      }, {
        id: (Date.now() + 1).toString(),
        content: data.response,
        role: 'assistant',
        timestamp: new Date().toISOString()
      }])
      setInput('')
    } catch (err) {
      setError('Failed to send message')
      console.error(err)
    } finally {
      setLoading(false)
    }
  }

  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      className="flex flex-col h-full max-w-2xl mx-auto p-4"
    >
      <div className="flex-1 overflow-y-auto mb-4 space-y-4">
        {history.map((message) => (
          <motion.div
            key={message.id}
            initial={{ opacity: 0, x: message.role === 'user' ? 20 : -20 }}
            animate={{ opacity: 1, x: 0 }}
            className={`p-4 rounded-lg ${
              message.role === 'user'
                ? 'bg-blue-100 ml-auto'
                : 'bg-gray-100'
            } max-w-[80%]`}
          >
            <p className="text-sm text-gray-600 mb-1">
              {new Date(message.timestamp).toLocaleTimeString()}
            </p>
            <p>{message.content}</p>
          </motion.div>
        ))}
      </div>

      {error && (
        <div className="bg-red-100 text-red-700 p-3 rounded-lg mb-4">
          {error}
        </div>
      )}

      <div className="flex gap-2">
        <textarea
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === 'Enter' && !e.shiftKey) {
              e.preventDefault()
              handleSend()
            }
          }}
          placeholder="Type your message..."
          className="flex-1 p-2 border rounded-lg resize-none"
          rows={3}
          disabled={loading}
        />
        <button
          onClick={handleSend}
          disabled={loading || !input.trim()}
          className={`px-4 py-2 rounded-lg ${
            loading || !input.trim()
              ? 'bg-gray-300 cursor-not-allowed'
              : 'bg-blue-500 hover:bg-blue-600 text-white'
          }`}
        >
          {loading ? 'Sending...' : 'Send'}
        </button>
      </div>
    </motion.div>
  )
}

export default ChatPanel 