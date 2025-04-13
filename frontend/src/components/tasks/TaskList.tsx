import { useTasks, Task } from '@/hooks/useTasks'
import AnimatedCard from '@/components/ui/AnimatedCard'
import { motion, AnimatePresence } from 'framer-motion'

const statusColors = {
  pending: 'bg-yellow-100 text-yellow-800',
  in_progress: 'bg-blue-100 text-blue-800',
  done: 'bg-green-100 text-green-800',
  overdue: 'bg-red-100 text-red-800',
}

const statusLabels = {
  pending: 'Pendente',
  in_progress: 'Em Progresso',
  done: 'Concluída',
  overdue: 'Atrasada',
}

export default function TaskList() {
  const { tasks, loading, error, updateTask, deleteTask } = useTasks()

  if (loading) {
    return (
      <div className="animate-pulse">
        {[...Array(3)].map((_, i) => (
          <div key={i} className="bg-gray-100 h-24 rounded-lg mb-4"></div>
        ))}
      </div>
    )
  }

  if (error) {
    return (
      <AnimatedCard className="p-4 bg-red-50">
        <p className="text-red-700">{error}</p>
      </AnimatedCard>
    )
  }

  if (tasks.length === 0) {
    return (
      <AnimatedCard className="p-8">
        <div className="text-center text-gray-500">
          <svg
            className="mx-auto h-12 w-12 text-gray-400"
            fill="none"
            viewBox="0 0 24 24"
            stroke="currentColor"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={2}
              d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2"
            />
          </svg>
          <p className="mt-4">Nenhuma tarefa encontrada</p>
        </div>
      </AnimatedCard>
    )
  }

  const handleStatusChange = (task: Task, newStatus: Task['status']) => {
    updateTask(task.id, { status: newStatus })
  }

  const handleDelete = (taskId: string) => {
    if (window.confirm('Tem certeza que deseja excluir esta tarefa?')) {
      deleteTask(taskId)
    }
  }

  return (
    <div className="space-y-4">
      <AnimatePresence>
        {tasks.map((task, index) => (
          <motion.div
            key={task.id}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, x: -100 }}
            transition={{ duration: 0.3, delay: index * 0.1 }}
          >
            <AnimatedCard className="p-4">
              <div className="flex justify-between items-start">
                <h3 className="font-semibold">{task.title}</h3>
                <div className="flex items-center space-x-2">
                  <select
                    value={task.status}
                    onChange={(e) => handleStatusChange(task, e.target.value as Task['status'])}
                    className={`text-sm rounded-full px-3 py-1 ${statusColors[task.status]}`}
                  >
                    {Object.entries(statusLabels).map(([value, label]) => (
                      <option key={value} value={value}>
                        {label}
                      </option>
                    ))}
                  </select>
                  <motion.button
                    whileHover={{ scale: 1.1 }}
                    whileTap={{ scale: 0.95 }}
                    onClick={() => handleDelete(task.id)}
                    className="text-red-600 hover:text-red-800"
                  >
                    <svg
                      xmlns="http://www.w3.org/2000/svg"
                      className="h-5 w-5"
                      viewBox="0 0 20 20"
                      fill="currentColor"
                    >
                      <path
                        fillRule="evenodd"
                        d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                        clipRule="evenodd"
                      />
                    </svg>
                  </motion.button>
                </div>
              </div>
              {task.description && (
                <p className="text-gray-600 text-sm mt-2">{task.description}</p>
              )}
              {task.due_date && (
                <p className="text-sm text-gray-500 mt-2">
                  Prazo: {new Date(task.due_date).toLocaleDateString()}
                </p>
              )}
            </AnimatedCard>
          </motion.div>
        ))}
      </AnimatePresence>
    </div>
  )
} 