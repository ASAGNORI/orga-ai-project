import ProtectedRoute from '@/components/auth/ProtectedRoute'
import TaskList from '@/components/tasks/TaskList'
import CreateTaskForm from '@/components/tasks/CreateTaskForm'

export default function TasksPage() {
  return (
    <ProtectedRoute>
      <div className="max-w-4xl mx-auto">
        <div className="flex justify-between items-center mb-6">
          <h1 className="text-2xl font-bold">Minhas Tarefas</h1>
        </div>
        <div className="grid gap-6 md:grid-cols-[2fr,1fr]">
          <TaskList />
          <div>
            <h2 className="text-lg font-semibold mb-4">Nova Tarefa</h2>
            <CreateTaskForm />
          </div>
        </div>
      </div>
    </ProtectedRoute>
  )
} 