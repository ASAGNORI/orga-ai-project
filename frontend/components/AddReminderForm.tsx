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
    <form onSubmit={handleSubmit}>
      <textarea
        value={inputText}
        onChange={(e) => setInputText(e.target.value)}
        placeholder="Digite seu lembrete"
        rows={4}
      />
      <button type="submit" disabled={loading}>
        {loading ? 'Enviando...' : 'Adicionar Lembrete'}
      </button>

      {reminder && (
        <div>
          <h3>Lembrete Adicionado:</h3>
          <p>{reminder.input_text}</p>
          <pre>{JSON.stringify(reminder.result_json, null, 2)}</pre>
        </div>
      )}
    </form>
  );
};

export default AddReminderForm;
