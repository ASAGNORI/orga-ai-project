import ReminderAgent from '@/components/ReminderAgent'
import MindmapCanvas from '@/components/MindmapCanvas'

export default function ReminderPage() {
  return (
    <div className="p-4">
      <h1 className="text-3xl font-bold mb-4">Orga.AI - Mapa Mental</h1>
      <ReminderAgent />
      <MindmapCanvas />
    </div>
  )
} 