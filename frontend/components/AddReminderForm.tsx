// frontend/components/AddReminderForm.tsx
import { useState } from 'react';
import { addReminderWithLLama } from '@/services/supabase';

const AddReminderForm = () => {
  const [inputText, setInputText] = useState('');
  const [loading, setLoading] = useState(false);
  const [reminder, setReminder] = useState(null);

  const handleSubmit = async (event: React.FormEvent) => {
    event.preventDefault();

    if (!inputText.trim()) return;

    setLoading(true);

    const newReminder = await addReminderWithLLama(inputText);
    setLoading(false);

    if (newReminder) {
      setReminder(newReminder);
      setInputText('');
    }
  };

  return (
    <form onSubmit={handleSubmit} className="flex flex-col gap-4 bg-white p-4 rounded-lg shadow-md">
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Digite seu lembrete"
        rows={4}
        className="p-2 border border-gray-300 rounded-md resize-none"
      />
      <button
        type="submit"
        disabled={loading}
        className={`px-4 py-2 rounded-md text-white ${
          loading ? 'bg-gray-400' : 'bg-blue-600 hover:bg-blue-700'
        }`}
      >
        {loading ? 'Enviando...' : 'Adicionar Lembrete'}
      </button>

      {reminder && (
        <div className="mt-4 bg-green-100 p-3 rounded-md">
          <h3 className="font-semibold text-green-800">Lembrete Adicionado:</h3>
          <p className="text-sm">{reminder.message}</p>
          <pre className="text-xs text-gray-600 mt-2">{JSON.stringify(reminder, null, 2)}</pre>
        </div>
      )}
    </form>
  );
};

export default AddReminderForm;
