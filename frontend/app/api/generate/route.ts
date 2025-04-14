import { NextResponse } from 'next/server'

export async function POST(request: Request) {
  try {
    const body = await request.json()
    
    const backendURL = 'http://localhost:8000/api/v1/generate'
    const result = await fetch(backendURL, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(body),
    })

    if (!result.ok) {
      throw new Error(`Backend responded with status: ${result.status}`)
    }

    const data = await result.json()
    return NextResponse.json(data)
  } catch (error) {
    console.error('Error in generate API route:', error)
    return NextResponse.json(
      { error: 'Failed to generate response' },
      { status: 500 }
    )
  }
} 