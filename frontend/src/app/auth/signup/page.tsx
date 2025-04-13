import SignUpForm from '@/components/auth/SignUpForm'

export default function SignUpPage() {
  return (
    <div className="max-w-md mx-auto mt-8 p-6 bg-white rounded-lg shadow-md">
      <h1 className="text-2xl font-bold mb-6 text-center">Criar Conta</h1>
      <SignUpForm />
    </div>
  )
} 