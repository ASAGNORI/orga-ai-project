import { useState, useEffect } from 'react'
import { createClient } from '@/utils/supabase/client'
import { useAuth } from '@/contexts/AuthContext'

export type Task = {
  id: string
  title: string
  description: string | null
  status: 'pending' | 'in_progress' | 'done' | 'overdue'
  due_date: string | null
  created_at: string
}

export function useTasks() {
  const [tasks, setTasks] = useState<Task[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)
  const { user } = useAuth()
  const supabase = createClient()

  useEffect(() => {
    if (user) {
      fetchTasks()
      // Subscribe to changes
      const channel = supabase
        .channel('tasks')
        .on(
          'postgres_changes',
          {
            event: '*',
            schema: 'public',
            table: 'tasks',
            filter: `user_id=eq.${user.id}`,
          },
          () => {
            fetchTasks()
          }
        )
        .subscribe()

      return () => {
        supabase.removeChannel(channel)
      }
    }
  }, [user])

  const fetchTasks = async () => {
    try {
      const { data, error } = await supabase
        .from('tasks')
        .select('*')
        .eq('user_id', user?.id)
        .order('created_at', { ascending: false })

      if (error) throw error
      setTasks(data)
    } catch (err) {
      setError('Error fetching tasks')
      console.error('Error:', err)
    } finally {
      setLoading(false)
    }
  }

  const createTask = async (title: string, description: string, dueDate: string | null) => {
    try {
      const { error } = await supabase.from('tasks').insert([
        {
          title,
          description,
          due_date: dueDate,
          user_id: user?.id,
          status: 'pending',
        },
      ])

      if (error) throw error
      await fetchTasks()
    } catch (err) {
      setError('Error creating task')
      console.error('Error:', err)
    }
  }

  const updateTask = async (id: string, updates: Partial<Task>) => {
    try {
      const { error } = await supabase
        .from('tasks')
        .update(updates)
        .eq('id', id)
        .eq('user_id', user?.id)

      if (error) throw error
      await fetchTasks()
    } catch (err) {
      setError('Error updating task')
      console.error('Error:', err)
    }
  }

  const deleteTask = async (id: string) => {
    try {
      const { error } = await supabase
        .from('tasks')
        .delete()
        .eq('id', id)
        .eq('user_id', user?.id)

      if (error) throw error
      await fetchTasks()
    } catch (err) {
      setError('Error deleting task')
      console.error('Error:', err)
    }
  }

  return {
    tasks,
    loading,
    error,
    createTask,
    updateTask,
    deleteTask,
  }
} 