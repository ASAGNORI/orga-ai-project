import { motion } from 'framer-motion'
import { ReactNode } from 'react'

type AnimatedCardProps = {
  children: ReactNode
  className?: string
  delay?: number
}

export default function AnimatedCard({ children, className = '', delay = 0 }: AnimatedCardProps) {
  return (
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.5, delay }}
      className={`bg-white rounded-lg shadow-lg hover:shadow-xl transition-shadow ${className}`}
    >
      {children}
    </motion.div>
  )
} 