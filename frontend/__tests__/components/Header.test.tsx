import { render, screen } from '@testing-library/react'
import Header from '@/components/Header'

describe('Header', () => {
  it('renders the logo', () => {
    render(<Header />)
    const logo = screen.getByAltText('OrgaAI Logo')
    expect(logo).toBeInTheDocument()
  })

  it('renders navigation links', () => {
    render(<Header />)
    expect(screen.getByText('Dashboard')).toBeInTheDocument()
    expect(screen.getByText('Tasks')).toBeInTheDocument()
    expect(screen.getByText('Settings')).toBeInTheDocument()
  })
}) 