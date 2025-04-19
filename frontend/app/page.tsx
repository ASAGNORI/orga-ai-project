'use client';

import { useEffect, useState } from 'react';
import { checkHealth } from '@/lib/api';

interface HealthStatus {
  status: string;
}

export default function Home() {
  const [status, setStatus] = useState<string>('Loading...');
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const checkBackendStatus = async () => {
      try {
        const result = await checkHealth() as HealthStatus;
        setStatus(result.status);
        setError(null);
      } catch (err) {
        setError('Failed to connect to backend');
        console.error('Error:', err);
      }
    };

    checkBackendStatus();
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24 bg-gray-100">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm lg:flex">
        <div className="w-full">
          <h1 className="text-4xl font-bold mb-8 text-center">Orga.AI</h1>
          <div className="bg-white rounded-lg p-6 shadow-lg">
            <h2 className="text-2xl font-semibold mb-4 text-center">Backend Status</h2>
            <div className="text-center">
              {error ? (
                <p className="text-red-500 font-medium">{error}</p>
              ) : (
                <p className="text-green-500 font-medium">Status: {status}</p>
              )}
            </div>
          </div>
        </div>
      </div>
    </main>
  );
}